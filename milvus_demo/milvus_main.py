# pip install pymilvus

from pymilvus import connections

connections.connect(
    alias="ai_platform",
    # host="10.1.100.37",
    host="127.0.0.1",
    port="19530"
)
#向量库名：milvus 集合名：ai_platform 用户名:admin 密码:admin 向量维度：128

from pymilvus import FieldSchema, CollectionSchema, DataType, Collection, utility

# 定义字段


print("创建集合开始")
def create_collection():
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True), # ID自增
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=128)
    ]

    schema = CollectionSchema(fields, description="示例向量集合")
    # 创建集合
    Collection(name="my_vectors", schema=schema, using="ai_platform")

print("创建开始")
create_collection()

print("插入数据开始")
import random

def insert(collection):
    # 生成 10 个随机 128 维向量
    vectors = [[random.random() for _ in range(128)] for _ in range(10)]

    insert_result = collection.insert([
        vectors                  # embedding
    ])
    return insert_result

# 获取已存在的集合
collection = Collection(name="my_vectors", using="ai_platform")
insert_result = insert(collection)
print("插入成功，IDs：", insert_result.primary_keys)


print("创建索引开始")
from pymilvus import Index
def create_index():
    # 创建索引
    index_params = {
        "index_type": "IVF_FLAT",
        "metric_type": "L2",
        "params": {"nlist": 128}
    }

    collection.create_index(field_name="embedding", index_params=index_params)

create_index()
print("创建索引开始结束")

print("查询数据开始")


def query_data():
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


query_data()
print("查询数据结束")
