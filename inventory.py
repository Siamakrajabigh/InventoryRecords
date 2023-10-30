class InventoryRecord:
    def __init__(self, ID, key_name, key_value, val_name, val_value):
        self.id = ID
        self.key_name = key_name
        self.key_value = key_value
        self.val_name = val_name
        self.val_value = val_value

    def __str__(self):
        return f'[ID={self.id}, key=({self.key_name}, {self.key_value}),' + \
            f' val=({self.val_name}, {self.val_value})]'

    def getDict(self):
        result_dict = {}
        result_dict["id"] = self.id
        result_dict["key_name"] = self.key_name
        result_dict["key_value"] = self.key_value
        result_dict["val_name"] = self.val_name
        result_dict["val_value"] = self.val_value
        return result_dict

class InventoryService:
    def __init__(self, data):
        self.data = data  # Assuming 'data' is a list of InventoryRecord objects

    def searchByID(self, ID):
        for record in self.data:
            if record.id == ID:
                return record
        return None

    def search(self, key_name, key_value):
        for record in self.data:
            if record.key_name == key_name and record.key_value == key_value:
                return record
        return None

    def search_range(self, key_name, key_value_start, key_value_end):
        records = []
        for record in self.data:
            if record.key_name == key_name and key_value_start <= record.key_value <= key_value_end:
                records.append(record)
        return records

    def getDistribution(self, key_name, percentile):
        values = [record.val_value for record in self.data if record.key_name == key_name]
        if values:
            values.sort()
            index = int(percentile * len(values) / 100)
            return values[index]
        return None

    def update(self, key_name, key_value, val_name, val_val_new):
        for record in self.data:
            if record.key_name == key_name and record.key_value == key_value:
                setattr(record, val_name, val_val_new)
                return True
        return False