# Milvus setup
from pymilvus import connections, Collection, FieldSchema, DataType, CollectionSchema
from milvus import Milvus
import json

# Connect to the Milvus server
connections.connect(
    alias="default",
    host="localhost",
    port=19530
)

# Create a collection for geospatial embeddings
collection_name = "geospatial_embeddings"
collection = Collection(name=collection_name)

# If the collection doesn't exist, create it
if not collection.has():
    book_id = FieldSchema(
        name="id",
        dtype=DataType.INT64,
        is_primary=True,
    )
    geospatial_embedding = FieldSchema(
        name="embedding",
        dtype=DataType.FLOAT_VECTOR,
        dim=2
    )

    schema = CollectionSchema(
        fields=[book_id, geospatial_embedding],
        description="Geospatial Embeddings Collection"
    )
    collection.create(schema)

# Load vectors from the JSON file
json_file = "out.json"
with open(json_file, "r") as file:
    data = json.load(file)

# Insert the vectors into the collection
for item in data:
    embedding = item['embedding']
    collection.insert(data=[embedding])

# Perform a geospatial search (similar to your previous search)
query_embedding = [query_latitude, query_longitude]
results = collection.search(query_embedding, top_k=10)

# Iterate through the results
for result in results:
    # You can use the IDs returned from the search to link back to your original data
    retrieved_id = result.id
    # Do something with the retrieved_id!!!!
    print(retrieved_id)

# Disconnect from the Milvus server
connections.disconnect(alias="default")
