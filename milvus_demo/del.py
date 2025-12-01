from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
import numpy as np

import pymilvus
print(pymilvus.__file__)
print(pymilvus.__version__)

from pymilvus import MilvusClient, DataType


client = MilvusClient(
    uri="http://localhost:19530"

)

res = client.list_collections()

print(res)







client.drop_collection(
    collection_name="my_vectors"
    # collection_name="demo_collection"
)
res = client.list_collections()

print(res)