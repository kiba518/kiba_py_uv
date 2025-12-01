# pip install pymilvus

from milvus_demo.milvus_client import MilvusClient

client = MilvusClient()
collection = client.get_collection()
client.create_index(collection)
client.insert(collection)
client.query_data(collection)




