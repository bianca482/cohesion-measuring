from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STRING: _ClassVar[ValueType]
    BOOL: _ClassVar[ValueType]
    INT64: _ClassVar[ValueType]
    FLOAT64: _ClassVar[ValueType]
    BINARY: _ClassVar[ValueType]

class SpanRefType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHILD_OF: _ClassVar[SpanRefType]
    FOLLOWS_FROM: _ClassVar[SpanRefType]
STRING: ValueType
BOOL: ValueType
INT64: ValueType
FLOAT64: ValueType
BINARY: ValueType
CHILD_OF: SpanRefType
FOLLOWS_FROM: SpanRefType

class KeyValue(_message.Message):
    __slots__ = ("key", "v_type", "v_str", "v_bool", "v_int64", "v_float64", "v_binary")
    KEY_FIELD_NUMBER: _ClassVar[int]
    V_TYPE_FIELD_NUMBER: _ClassVar[int]
    V_STR_FIELD_NUMBER: _ClassVar[int]
    V_BOOL_FIELD_NUMBER: _ClassVar[int]
    V_INT64_FIELD_NUMBER: _ClassVar[int]
    V_FLOAT64_FIELD_NUMBER: _ClassVar[int]
    V_BINARY_FIELD_NUMBER: _ClassVar[int]
    key: str
    v_type: ValueType
    v_str: str
    v_bool: bool
    v_int64: int
    v_float64: float
    v_binary: bytes
    def __init__(self, key: _Optional[str] = ..., v_type: _Optional[_Union[ValueType, str]] = ..., v_str: _Optional[str] = ..., v_bool: bool = ..., v_int64: _Optional[int] = ..., v_float64: _Optional[float] = ..., v_binary: _Optional[bytes] = ...) -> None: ...

class Log(_message.Message):
    __slots__ = ("timestamp", "fields")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    fields: _containers.RepeatedCompositeFieldContainer[KeyValue]
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., fields: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ...) -> None: ...

class SpanRef(_message.Message):
    __slots__ = ("trace_id", "span_id", "ref_type")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    REF_TYPE_FIELD_NUMBER: _ClassVar[int]
    trace_id: bytes
    span_id: bytes
    ref_type: SpanRefType
    def __init__(self, trace_id: _Optional[bytes] = ..., span_id: _Optional[bytes] = ..., ref_type: _Optional[_Union[SpanRefType, str]] = ...) -> None: ...

class Process(_message.Message):
    __slots__ = ("service_name", "tags")
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    tags: _containers.RepeatedCompositeFieldContainer[KeyValue]
    def __init__(self, service_name: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ...) -> None: ...

class Span(_message.Message):
    __slots__ = ("trace_id", "span_id", "operation_name", "references", "flags", "start_time", "duration", "tags", "logs", "process", "process_id", "warnings")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_NAME_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    trace_id: bytes
    span_id: bytes
    operation_name: str
    references: _containers.RepeatedCompositeFieldContainer[SpanRef]
    flags: int
    start_time: _timestamp_pb2.Timestamp
    duration: _duration_pb2.Duration
    tags: _containers.RepeatedCompositeFieldContainer[KeyValue]
    logs: _containers.RepeatedCompositeFieldContainer[Log]
    process: Process
    process_id: str
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, trace_id: _Optional[bytes] = ..., span_id: _Optional[bytes] = ..., operation_name: _Optional[str] = ..., references: _Optional[_Iterable[_Union[SpanRef, _Mapping]]] = ..., flags: _Optional[int] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., logs: _Optional[_Iterable[_Union[Log, _Mapping]]] = ..., process: _Optional[_Union[Process, _Mapping]] = ..., process_id: _Optional[str] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class Trace(_message.Message):
    __slots__ = ("spans", "process_map", "warnings")
    class ProcessMapping(_message.Message):
        __slots__ = ("process_id", "process")
        PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
        PROCESS_FIELD_NUMBER: _ClassVar[int]
        process_id: str
        process: Process
        def __init__(self, process_id: _Optional[str] = ..., process: _Optional[_Union[Process, _Mapping]] = ...) -> None: ...
    SPANS_FIELD_NUMBER: _ClassVar[int]
    PROCESS_MAP_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    spans: _containers.RepeatedCompositeFieldContainer[Span]
    process_map: _containers.RepeatedCompositeFieldContainer[Trace.ProcessMapping]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, spans: _Optional[_Iterable[_Union[Span, _Mapping]]] = ..., process_map: _Optional[_Iterable[_Union[Trace.ProcessMapping, _Mapping]]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class Batch(_message.Message):
    __slots__ = ("spans", "process")
    SPANS_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    spans: _containers.RepeatedCompositeFieldContainer[Span]
    process: Process
    def __init__(self, spans: _Optional[_Iterable[_Union[Span, _Mapping]]] = ..., process: _Optional[_Union[Process, _Mapping]] = ...) -> None: ...

class DependencyLink(_message.Message):
    __slots__ = ("parent", "child", "call_count", "source")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_NUMBER: _ClassVar[int]
    CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    child: str
    call_count: int
    source: str
    def __init__(self, parent: _Optional[str] = ..., child: _Optional[str] = ..., call_count: _Optional[int] = ..., source: _Optional[str] = ...) -> None: ...
