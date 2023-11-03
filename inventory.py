class InventoryRecord:
    def __init__(self, id, name, description, unit_price, quantity, inventory_value, reorder_level, reorder_time, quantity_reorder, discontinued):
        self.id = id
        self.name = name
        self.description = description
        self.unit_price = unit_price
        self.quantity = quantity
        self.inventory_value = inventory_value
        self.reorder_level = reorder_level
        self.reorder_time = reorder_time
        self.quantity_reorder = quantity_reorder
        self.discontinued = discontinued

    def __str__(self):
        return f'[id={self.id}, name={self.name}, description={self.description}, unit_price={self.unit_price}, quantity={self.quantity}, inventory_value={self.inventory_value}, reorder_level={self.reorder_level}, reorder_time={self.reorder_time}, quantity_reorder={self.quantity_reorder}, discontinued={self.discontinued}]'


    def getDict(self):
        result_dict = {}
        result_dict["id"] = self.id
        result_dict["name"] = self.name
        result_dict["description"] = self.description
        result_dict["unit_price"] = self.unit_price
        result_dict["quantity"] = self.quantity
        result_dict["inventory_value"] = self.inventory_value
        result_dict["reorder_level"] = self.reorder_level
        result_dict["reorder_time"] = self.reorder_time
        result_dict["quantity_reorder"] = self.quantity_reorder
        result_dict["discontinued"] = self.discontinued
        return result_dict

class InventoryService:
    def __init__(self, data):
        self.data = data  # Assuming 'data' is a list of InventoryRecord objects

    def searchByID(self, id):
        for record in self.data:
            if record.id == id:
                return record
        return None

    def search(self, key_name, key_value):
        for record in self.data:
            attr_value = getattr(record, key_name, None)
            if attr_value == key_value:
                return record
        return None

    def search_range(self, key_name, key_value_start, key_value_end):
        records = []
        for record in self.data:
            attr_value = getattr(record, key_name, None)
            if int(key_value_start) <= int(attr_value) <= int(key_value_end):
                records.append(record)
        print(records)
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