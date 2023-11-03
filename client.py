import grpc
import inventory_pb2 as pb2
import inventory_pb2_grpc as pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.InventoryStub(channel)

    # Example: Search by ID
    print("Example: Search By ID")
    request_msg = pb2.SearchByIDRequest(id="IN0001")
    assert(isinstance(request_msg, pb2.SearchByIDRequest))
    print(type(request_msg), request_msg)
    response = stub.SearchByID(request_msg)
    assert(isinstance(response, pb2.SearchByIDResponse))
    print (response)
    print("SearchByID Response:", response)

    # Example: Search
    print("Example: Search")
    response = stub.Search(pb2.SearchRequest(key_name="name", key_value="Item 7"))
    print("Search Response:", response.record)

    # Example: Search Range
    print("Example: Search Range")
    response = stub.SearchRange(pb2.SearchRangeRequest(key_name="quantity", key_value_start="5", key_value_end="15"))
    print("SearchRange Response:", response.records)

    # Example: Get Distribution
    response = stub.GetDistribution(pb2.DistributionRequest(key_name="Price", percentile=50))
    print("GetDistribution Response:", response.value)

    # Example: Update
    response = stub.Update(pb2.UpdateRequest(key_name="Category", key_value="Clothing", val_name="Price", val_val_new="60"))
    print("Update Response:", response.success)

if __name__ == '__main__':
    run()
