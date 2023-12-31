# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finventory.proto\"\xdc\x01\n\x0fInventoryRecord\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x12\n\nunit_price\x18\x04 \x01(\t\x12\x10\n\x08quantity\x18\x05 \x01(\t\x12\x17\n\x0finventory_value\x18\x06 \x01(\t\x12\x15\n\rreorder_level\x18\x07 \x01(\t\x12\x14\n\x0creorder_time\x18\x08 \x01(\t\x12\x18\n\x10quantity_reorder\x18\t \x01(\t\x12\x14\n\x0c\x64iscontinued\x18\n \x01(\t\"\x1f\n\x11SearchByIDRequest\x12\n\n\x02id\x18\x01 \x01(\t\"6\n\x12SearchByIDResponse\x12 \n\x06record\x18\x01 \x01(\x0b\x32\x10.InventoryRecord\"4\n\rSearchRequest\x12\x10\n\x08key_name\x18\x01 \x01(\t\x12\x11\n\tkey_value\x18\x02 \x01(\t\"2\n\x0eSearchResponse\x12 \n\x06record\x18\x01 \x01(\x0b\x32\x10.InventoryRecord\"V\n\x12SearchRangeRequest\x12\x10\n\x08key_name\x18\x01 \x01(\t\x12\x17\n\x0fkey_value_start\x18\x02 \x01(\t\x12\x15\n\rkey_value_end\x18\x03 \x01(\t\"8\n\x13SearchRangeResponse\x12!\n\x07records\x18\x01 \x03(\x0b\x32\x10.InventoryRecord\";\n\x13\x44istributionRequest\x12\x10\n\x08key_name\x18\x01 \x01(\t\x12\x12\n\npercentile\x18\x02 \x01(\x01\"%\n\x14\x44istributionResponse\x12\r\n\x05value\x18\x01 \x01(\x01\"[\n\rUpdateRequest\x12\x10\n\x08key_name\x18\x01 \x01(\t\x12\x11\n\tkey_value\x18\x02 \x01(\t\x12\x10\n\x08val_name\x18\x03 \x01(\t\x12\x13\n\x0bval_val_new\x18\x04 \x01(\t\"!\n\x0eUpdateResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\x92\x02\n\tInventory\x12\x35\n\nSearchByID\x12\x12.SearchByIDRequest\x1a\x13.SearchByIDResponse\x12)\n\x06Search\x12\x0e.SearchRequest\x1a\x0f.SearchResponse\x12\x38\n\x0bSearchRange\x12\x13.SearchRangeRequest\x1a\x14.SearchRangeResponse\x12>\n\x0fGetDistribution\x12\x14.DistributionRequest\x1a\x15.DistributionResponse\x12)\n\x06Update\x12\x0e.UpdateRequest\x1a\x0f.UpdateResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_INVENTORYRECORD']._serialized_start=20
  _globals['_INVENTORYRECORD']._serialized_end=240
  _globals['_SEARCHBYIDREQUEST']._serialized_start=242
  _globals['_SEARCHBYIDREQUEST']._serialized_end=273
  _globals['_SEARCHBYIDRESPONSE']._serialized_start=275
  _globals['_SEARCHBYIDRESPONSE']._serialized_end=329
  _globals['_SEARCHREQUEST']._serialized_start=331
  _globals['_SEARCHREQUEST']._serialized_end=383
  _globals['_SEARCHRESPONSE']._serialized_start=385
  _globals['_SEARCHRESPONSE']._serialized_end=435
  _globals['_SEARCHRANGEREQUEST']._serialized_start=437
  _globals['_SEARCHRANGEREQUEST']._serialized_end=523
  _globals['_SEARCHRANGERESPONSE']._serialized_start=525
  _globals['_SEARCHRANGERESPONSE']._serialized_end=581
  _globals['_DISTRIBUTIONREQUEST']._serialized_start=583
  _globals['_DISTRIBUTIONREQUEST']._serialized_end=642
  _globals['_DISTRIBUTIONRESPONSE']._serialized_start=644
  _globals['_DISTRIBUTIONRESPONSE']._serialized_end=681
  _globals['_UPDATEREQUEST']._serialized_start=683
  _globals['_UPDATEREQUEST']._serialized_end=774
  _globals['_UPDATERESPONSE']._serialized_start=776
  _globals['_UPDATERESPONSE']._serialized_end=809
  _globals['_INVENTORY']._serialized_start=812
  _globals['_INVENTORY']._serialized_end=1086
# @@protoc_insertion_point(module_scope)
