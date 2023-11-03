import grpc
from concurrent import futures
import inventory_pb2 as pb2
import inventory_pb2_grpc as pb2_grpc
import time
import pandas as pd

from inventory import InventoryService
from inventory import InventoryRecord

class InventoryServicer(pb2_grpc.InventoryServicer):
    def __init__(self, data):
        self.service = InventoryService(data)

    def SearchByID(self, request, context):
        record = self.service.searchByID(request.id) # type = InventoryRecord

        response = pb2.SearchByIDResponse(record=record.getDict())
        print('-'*10)
        print(response)
        print('-'*10)
        return response

    def Search(self, request, context):
        record = self.service.search(request.key_name, request.key_value)
        return pb2.SearchResponse(record=record.getDict())

    def SearchRange(self, request, context):
        records = self.service.search_range(request.key_name, request.key_value_start, request.key_value_end)
        response_records = [record.getDict() for record in records]

        response = pb2.SearchRangeResponse(records=response_records)
        return response


    def GetDistribution(self, request, context):
        value = self.service.getDistribution(request.key_name, request.percentile)
        return pb2.DistributionResponse(value=value)

    def Update(self, request, context):
        success = self.service.update(request.key_name, request.key_value, request.val_name, request.val_val_new)
        return pb2.UpdateResponse(success=success)


if __name__ == '__main__':
    # Assuming 'data' is a list of InventoryRecord objects
    # read from csv input and constrcut the objects -> memory

    # data = [
    #     InventoryRecord("IN0001", "Item 1", "Desc 1", "51", "25", "1275", "29", "13", "50", "nan"),
        
    #     # Add more records as needed...
    # ]
    df = pd.read_excel(r"/content/Inventory list with reorder highlighting.xlsx", header=2)
    data = []

    # Iterate through the rows of the DataFrame and create InventoryRecord objects
    for index, row in df.iterrows():
        record = InventoryRecord(
            id=str(row['Inventory ID']),
            name=str(row['Name']),
            description=str(row['Description']),
            unit_price=str(row['Unit Price']),
            quantity=str(row['Quantity in Stock']),
            inventory_value=str(row['Inventory Value']),
            reorder_level=str(row['Reorder Level']),
            reorder_time=str(row['Reorder Time in Days']),
            quantity_reorder=str(row['Quantity in Reorder']),
            discontinued=str(row['Discontinued?'])
        )
        data.append(record)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_InventoryServicer_to_server(InventoryServicer(data), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")


    # Set a flag to indicate when to exit
    exit_flag = False

    try:
        # Run the server for 60 seconds before exiting
        for _ in range(180):
            if exit_flag:
                break
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nServer interrupted by user")

    # Gracefully shutdown the server
    server.stop(0)
