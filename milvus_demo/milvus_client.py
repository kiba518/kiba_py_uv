# pip install pymilvus
from pymilvus import FieldSchema, CollectionSchema, DataType, Collection, utility,connections,Index
import random

class MilvusClient:
    collection_name = "my_13"
    alias = "ai_platform"
    conn = None
    # 向量库名：milvus 集合名：ai_platform 用户名:admin 密码:admin 向量维度：128
    def init_collection(self):
        self.conn = connections.connect(
            alias=self.alias,
            # host="10.1.100.37",
            host="127.0.0.1",
            port="19530"
        )

    def __init__(self,_connections = None ):
        if _connections is None:
            self.init_collection()




    def get_collection(self):
        """创建集合.
        """
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),  # ID自增
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=128)
        ]

        schema = CollectionSchema(fields, description="示例向量集合")

        # 创建集合
        if self.collection_name in utility.list_collections(using=self.alias):
            print("集合已存在，直接获取")
            collection = Collection(name=self.collection_name, using=self.alias)
            return collection
        else:
            print("集合不存在，创建新集合")
            collection = Collection(name=self.collection_name,schema=schema, using=self.alias)
            return collection


    def insert(self,collection=None,vectors=None):
        """
        插入测试数据.
        参数：
        vectors (List[List[float]]): 二维向量列表
        """
        if collection is None:
            collection = Collection(name=self.collection_name, using=self.alias)
        if vectors is None:
            vectors = [[random.random() for _ in range(128)] for _ in range(10)]   # 生成 10 个随机 128 维向量

        insert_result = collection.insert([
            vectors  # embedding
        ])
        print("插入成功，IDs：", insert_result.primary_keys)
        return insert_result

    def create_index(self,collection=None):
        """
        创建索引.
        """
        if collection is None:
            raise Exception("请先创建集合")
        # 创建索引
        index_params = {
            "index_type": "IVF_FLAT",
            "metric_type": "L2",
            "params": {"nlist": 128}
        }
        collection.create_index(field_name="embedding", index_params=index_params)



    def query_data(self,collection=None):
        # 先加载集合到内存
        collection.load()

        query_vectors = [[random.random() for _ in range(128)]]

        results = collection.search(
            data=query_vectors,
            anns_field="embedding",
            param={"metric_type": "L2", "params": {"nprobe": 10}},
            limit=3
        )

        for hits in results:
            for hit in hits:
                print(f"id: {hit.id}, distance: {hit.distance}")

    def delete_vectors(self, expr):
        """
        删除集合中符合条件的向量

        参数：
        expr (str): 删除条件表达式，例如 "id in [1,2,3]" 或 "id > 5"
        调用：client.delete_vectors("id in [1,2]")
        """
        if self.conn is None:
            raise Exception("请先创建集合")
        res = self.conn.delete(expr)
        print(f"已删除符合条件的数据: {expr}")
        return res

    # def drop_connection(self, connection=None):
    #     """
    #     删除整个集合
    #
    #     警告：该操作不可恢复，会删除集合及其所有数据
    #     """
    #     if connection is None:
    #         # 如果集合对象未获取，也可以直接 drop
    #         connection =  self.conn
    #     connection.drop()
    #     connection = None
    #     print(f"断开连接")