# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import model_pb2 as model__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bquery.proto\x12\rjaeger.api_v2\x1a\x0bmodel.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"\xcf\x01\n\x0fGetTraceRequest\x12R\n\x08trace_id\x18\x01 \x01(\x0c\x42@\xc8\xde\x1f\x00\xda\xde\x1f-github.com/jaegertracing/jaeger/model.TraceID\xe2\xde\x1f\x07TraceID\x12\x34\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12\x32\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\">\n\x12SpansResponseChunk\x12(\n\x05spans\x18\x01 \x03(\x0b\x32\x13.jaeger.api_v2.SpanB\x04\xc8\xde\x1f\x00\"\xd3\x01\n\x13\x41rchiveTraceRequest\x12R\n\x08trace_id\x18\x01 \x01(\x0c\x42@\xc8\xde\x1f\x00\xda\xde\x1f-github.com/jaegertracing/jaeger/model.TraceID\xe2\xde\x1f\x07TraceID\x12\x34\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12\x32\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\"\x16\n\x14\x41rchiveTraceResponse\"\xb6\x03\n\x14TraceQueryParameters\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x16\n\x0eoperation_name\x18\x02 \x01(\t\x12;\n\x04tags\x18\x03 \x03(\x0b\x32-.jaeger.api_v2.TraceQueryParameters.TagsEntry\x12<\n\x0estart_time_min\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12<\n\x0estart_time_max\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x39\n\x0c\x64uration_min\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x39\n\x0c\x64uration_max\x18\x07 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x14\n\x0csearch_depth\x18\x08 \x01(\x05\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"G\n\x11\x46indTracesRequest\x12\x32\n\x05query\x18\x01 \x01(\x0b\x32#.jaeger.api_v2.TraceQueryParameters\"\x14\n\x12GetServicesRequest\"\'\n\x13GetServicesResponse\x12\x10\n\x08services\x18\x01 \x03(\t\":\n\x14GetOperationsRequest\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x11\n\tspan_kind\x18\x02 \x01(\t\",\n\tOperation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tspan_kind\x18\x02 \x01(\t\"]\n\x15GetOperationsResponse\x12\x16\n\x0eoperationNames\x18\x01 \x03(\t\x12,\n\noperations\x18\x02 \x03(\x0b\x32\x18.jaeger.api_v2.Operation\"\x8a\x01\n\x16GetDependenciesRequest\x12\x38\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x36\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\"T\n\x17GetDependenciesResponse\x12\x39\n\x0c\x64\x65pendencies\x18\x01 \x03(\x0b\x32\x1d.jaeger.api_v2.DependencyLinkB\x04\xc8\xde\x1f\x00\x32\xad\x05\n\x0cQueryService\x12k\n\x08GetTrace\x12\x1e.jaeger.api_v2.GetTraceRequest\x1a!.jaeger.api_v2.SpansResponseChunk\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/traces/{trace_id}0\x01\x12t\n\x0c\x41rchiveTrace\x12\".jaeger.api_v2.ArchiveTraceRequest\x1a#.jaeger.api_v2.ArchiveTraceResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/archive/{trace_id}\x12g\n\nFindTraces\x12 .jaeger.api_v2.FindTracesRequest\x1a!.jaeger.api_v2.SpansResponseChunk\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/search:\x01*0\x01\x12g\n\x0bGetServices\x12!.jaeger.api_v2.GetServicesRequest\x1a\".jaeger.api_v2.GetServicesResponse\"\x11\x82\xd3\xe4\x93\x02\x0b\x12\t/services\x12o\n\rGetOperations\x12#.jaeger.api_v2.GetOperationsRequest\x1a$.jaeger.api_v2.GetOperationsResponse\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/operations\x12w\n\x0fGetDependencies\x12%.jaeger.api_v2.GetDependenciesRequest\x1a&.jaeger.api_v2.GetDependenciesResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/dependenciesB-\n\x17io.jaegertracing.api_v2Z\x06\x61pi_v2\xc8\xe2\x1e\x01\xd0\xe2\x1e\x01\xe0\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027io.jaegertracing.api_v2Z\006api_v2\310\342\036\001\320\342\036\001\340\342\036\001'
  _globals['_GETTRACEREQUEST'].fields_by_name['trace_id']._loaded_options = None
  _globals['_GETTRACEREQUEST'].fields_by_name['trace_id']._serialized_options = b'\310\336\037\000\332\336\037-github.com/jaegertracing/jaeger/model.TraceID\342\336\037\007TraceID'
  _globals['_GETTRACEREQUEST'].fields_by_name['start_time']._loaded_options = None
  _globals['_GETTRACEREQUEST'].fields_by_name['start_time']._serialized_options = b'\220\337\037\001'
  _globals['_GETTRACEREQUEST'].fields_by_name['end_time']._loaded_options = None
  _globals['_GETTRACEREQUEST'].fields_by_name['end_time']._serialized_options = b'\220\337\037\001'
  _globals['_SPANSRESPONSECHUNK'].fields_by_name['spans']._loaded_options = None
  _globals['_SPANSRESPONSECHUNK'].fields_by_name['spans']._serialized_options = b'\310\336\037\000'
  _globals['_ARCHIVETRACEREQUEST'].fields_by_name['trace_id']._loaded_options = None
  _globals['_ARCHIVETRACEREQUEST'].fields_by_name['trace_id']._serialized_options = b'\310\336\037\000\332\336\037-github.com/jaegertracing/jaeger/model.TraceID\342\336\037\007TraceID'
  _globals['_ARCHIVETRACEREQUEST'].fields_by_name['start_time']._loaded_options = None
  _globals['_ARCHIVETRACEREQUEST'].fields_by_name['start_time']._serialized_options = b'\220\337\037\001'
  _globals['_ARCHIVETRACEREQUEST'].fields_by_name['end_time']._loaded_options = None
  _globals['_ARCHIVETRACEREQUEST'].fields_by_name['end_time']._serialized_options = b'\220\337\037\001'
  _globals['_TRACEQUERYPARAMETERS_TAGSENTRY']._loaded_options = None
  _globals['_TRACEQUERYPARAMETERS_TAGSENTRY']._serialized_options = b'8\001'
  _globals['_TRACEQUERYPARAMETERS'].fields_by_name['start_time_min']._loaded_options = None
  _globals['_TRACEQUERYPARAMETERS'].fields_by_name['start_time_min']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_TRACEQUERYPARAMETERS'].fields_by_name['start_time_max']._loaded_options = None
  _globals['_TRACEQUERYPARAMETERS'].fields_by_name['start_time_max']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_TRACEQUERYPARAMETERS'].fields_by_name['duration_min']._loaded_options = None
  _globals['_TRACEQUERYPARAMETERS'].fields_by_name['duration_min']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _globals['_TRACEQUERYPARAMETERS'].fields_by_name['duration_max']._loaded_options = None
  _globals['_TRACEQUERYPARAMETERS'].fields_by_name['duration_max']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _globals['_GETDEPENDENCIESREQUEST'].fields_by_name['start_time']._loaded_options = None
  _globals['_GETDEPENDENCIESREQUEST'].fields_by_name['start_time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_GETDEPENDENCIESREQUEST'].fields_by_name['end_time']._loaded_options = None
  _globals['_GETDEPENDENCIESREQUEST'].fields_by_name['end_time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_GETDEPENDENCIESRESPONSE'].fields_by_name['dependencies']._loaded_options = None
  _globals['_GETDEPENDENCIESRESPONSE'].fields_by_name['dependencies']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYSERVICE'].methods_by_name['GetTrace']._loaded_options = None
  _globals['_QUERYSERVICE'].methods_by_name['GetTrace']._serialized_options = b'\202\323\344\223\002\024\022\022/traces/{trace_id}'
  _globals['_QUERYSERVICE'].methods_by_name['ArchiveTrace']._loaded_options = None
  _globals['_QUERYSERVICE'].methods_by_name['ArchiveTrace']._serialized_options = b'\202\323\344\223\002\025\"\023/archive/{trace_id}'
  _globals['_QUERYSERVICE'].methods_by_name['FindTraces']._loaded_options = None
  _globals['_QUERYSERVICE'].methods_by_name['FindTraces']._serialized_options = b'\202\323\344\223\002\014\"\007/search:\001*'
  _globals['_QUERYSERVICE'].methods_by_name['GetServices']._loaded_options = None
  _globals['_QUERYSERVICE'].methods_by_name['GetServices']._serialized_options = b'\202\323\344\223\002\013\022\t/services'
  _globals['_QUERYSERVICE'].methods_by_name['GetOperations']._loaded_options = None
  _globals['_QUERYSERVICE'].methods_by_name['GetOperations']._serialized_options = b'\202\323\344\223\002\r\022\013/operations'
  _globals['_QUERYSERVICE'].methods_by_name['GetDependencies']._loaded_options = None
  _globals['_QUERYSERVICE'].methods_by_name['GetDependencies']._serialized_options = b'\202\323\344\223\002\017\022\r/dependencies'
  _globals['_GETTRACEREQUEST']._serialized_start=161
  _globals['_GETTRACEREQUEST']._serialized_end=368
  _globals['_SPANSRESPONSECHUNK']._serialized_start=370
  _globals['_SPANSRESPONSECHUNK']._serialized_end=432
  _globals['_ARCHIVETRACEREQUEST']._serialized_start=435
  _globals['_ARCHIVETRACEREQUEST']._serialized_end=646
  _globals['_ARCHIVETRACERESPONSE']._serialized_start=648
  _globals['_ARCHIVETRACERESPONSE']._serialized_end=670
  _globals['_TRACEQUERYPARAMETERS']._serialized_start=673
  _globals['_TRACEQUERYPARAMETERS']._serialized_end=1111
  _globals['_TRACEQUERYPARAMETERS_TAGSENTRY']._serialized_start=1068
  _globals['_TRACEQUERYPARAMETERS_TAGSENTRY']._serialized_end=1111
  _globals['_FINDTRACESREQUEST']._serialized_start=1113
  _globals['_FINDTRACESREQUEST']._serialized_end=1184
  _globals['_GETSERVICESREQUEST']._serialized_start=1186
  _globals['_GETSERVICESREQUEST']._serialized_end=1206
  _globals['_GETSERVICESRESPONSE']._serialized_start=1208
  _globals['_GETSERVICESRESPONSE']._serialized_end=1247
  _globals['_GETOPERATIONSREQUEST']._serialized_start=1249
  _globals['_GETOPERATIONSREQUEST']._serialized_end=1307
  _globals['_OPERATION']._serialized_start=1309
  _globals['_OPERATION']._serialized_end=1353
  _globals['_GETOPERATIONSRESPONSE']._serialized_start=1355
  _globals['_GETOPERATIONSRESPONSE']._serialized_end=1448
  _globals['_GETDEPENDENCIESREQUEST']._serialized_start=1451
  _globals['_GETDEPENDENCIESREQUEST']._serialized_end=1589
  _globals['_GETDEPENDENCIESRESPONSE']._serialized_start=1591
  _globals['_GETDEPENDENCIESRESPONSE']._serialized_end=1675
  _globals['_QUERYSERVICE']._serialized_start=1678
  _globals['_QUERYSERVICE']._serialized_end=2363
# @@protoc_insertion_point(module_scope)
