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
    Collection(name="my_vectors5", schema=schema, using="ai_platform")

print("创建开始")
create_collection()


for collection_name in utility.list_collections(using="ai_platform"):
    print("name:"+collection_name)
