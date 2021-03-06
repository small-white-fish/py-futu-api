# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Qot_GetCodeChange.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import Qot_Common_pb2 as Qot__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Qot_GetCodeChange.proto',
  package='Qot_GetCodeChange',
  syntax='proto2',
  serialized_pb=_b('\n\x17Qot_GetCodeChange.proto\x12\x11Qot_GetCodeChange\x1a\x0c\x43ommon.proto\x1a\x10Qot_Common.proto\"\xfc\x01\n\x0e\x43odeChangeInfo\x12\x0c\n\x04type\x18\x01 \x02(\x05\x12&\n\x08security\x18\x02 \x02(\x0b\x32\x14.Qot_Common.Security\x12-\n\x0frelatedSecurity\x18\x03 \x02(\x0b\x32\x14.Qot_Common.Security\x12\x12\n\npublicTime\x18\x04 \x01(\t\x12\x17\n\x0fpublicTimestamp\x18\x05 \x01(\x01\x12\x15\n\reffectiveTime\x18\x06 \x01(\t\x12\x1a\n\x12\x65\x66\x66\x65\x63tiveTimestamp\x18\x07 \x01(\x01\x12\x0f\n\x07\x65ndTime\x18\x08 \x01(\t\x12\x14\n\x0c\x65ndTimestamp\x18\t \x01(\x01\">\n\nTimeFilter\x12\x0c\n\x04type\x18\x01 \x02(\x05\x12\x11\n\tbeginTime\x18\x02 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x03 \x01(\t\"\x8f\x01\n\x03\x43\x32S\x12\x13\n\x0bplaceHolder\x18\x01 \x01(\x05\x12*\n\x0csecurityList\x18\x02 \x03(\x0b\x32\x14.Qot_Common.Security\x12\x35\n\x0etimeFilterList\x18\x03 \x03(\x0b\x32\x1d.Qot_GetCodeChange.TimeFilter\x12\x10\n\x08typeList\x18\x04 \x03(\x05\"@\n\x03S2C\x12\x39\n\x0e\x63odeChangeList\x18\x01 \x03(\x0b\x32!.Qot_GetCodeChange.CodeChangeInfo\".\n\x07Request\x12#\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x16.Qot_GetCodeChange.C2S\"g\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12#\n\x03s2c\x18\x04 \x01(\x0b\x32\x16.Qot_GetCodeChange.S2C*\x8e\x02\n\x0e\x43odeChangeType\x12\x19\n\x15\x43odeChangeType_Unkown\x10\x00\x12\x1c\n\x18\x43odeChangeType_GemToMain\x10\x01\x12\x19\n\x15\x43odeChangeType_Unpaid\x10\x02\x12\x1c\n\x18\x43odeChangeType_ChangeLot\x10\x03\x12\x18\n\x14\x43odeChangeType_Split\x10\x04\x12\x18\n\x14\x43odeChangeType_Joint\x10\x05\x12\x1d\n\x19\x43odeChangeType_JointSplit\x10\x06\x12\x1d\n\x19\x43odeChangeType_SplitJoint\x10\x07\x12\x18\n\x14\x43odeChangeType_Other\x10\x08*|\n\x0eTimeFilterType\x12\x19\n\x15TimeFilterType_Unknow\x10\x00\x12\x19\n\x15TimeFilterType_Public\x10\x01\x12\x1c\n\x18TimeFilterType_Effective\x10\x02\x12\x16\n\x12TimeFilterType_End\x10\x03\x42G\n\x13\x63om.futu.openapi.pbZ0github.com/futuopen/ftapi4go/pb/qotgetcodechange')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Qot__Common__pb2.DESCRIPTOR,])

_CODECHANGETYPE = _descriptor.EnumDescriptor(
  name='CodeChangeType',
  full_name='Qot_GetCodeChange.CodeChangeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CodeChangeType_Unkown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CodeChangeType_GemToMain', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CodeChangeType_Unpaid', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CodeChangeType_ChangeLot', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CodeChangeType_Split', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CodeChangeType_Joint', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CodeChangeType_JointSplit', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CodeChangeType_SplitJoint', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CodeChangeType_Other', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=763,
  serialized_end=1033,
)
_sym_db.RegisterEnumDescriptor(_CODECHANGETYPE)

CodeChangeType = enum_type_wrapper.EnumTypeWrapper(_CODECHANGETYPE)
_TIMEFILTERTYPE = _descriptor.EnumDescriptor(
  name='TimeFilterType',
  full_name='Qot_GetCodeChange.TimeFilterType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TimeFilterType_Unknow', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TimeFilterType_Public', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TimeFilterType_Effective', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TimeFilterType_End', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1035,
  serialized_end=1159,
)
_sym_db.RegisterEnumDescriptor(_TIMEFILTERTYPE)

TimeFilterType = enum_type_wrapper.EnumTypeWrapper(_TIMEFILTERTYPE)
CodeChangeType_Unkown = 0
CodeChangeType_GemToMain = 1
CodeChangeType_Unpaid = 2
CodeChangeType_ChangeLot = 3
CodeChangeType_Split = 4
CodeChangeType_Joint = 5
CodeChangeType_JointSplit = 6
CodeChangeType_SplitJoint = 7
CodeChangeType_Other = 8
TimeFilterType_Unknow = 0
TimeFilterType_Public = 1
TimeFilterType_Effective = 2
TimeFilterType_End = 3



_CODECHANGEINFO = _descriptor.Descriptor(
  name='CodeChangeInfo',
  full_name='Qot_GetCodeChange.CodeChangeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Qot_GetCodeChange.CodeChangeInfo.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='security', full_name='Qot_GetCodeChange.CodeChangeInfo.security', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relatedSecurity', full_name='Qot_GetCodeChange.CodeChangeInfo.relatedSecurity', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publicTime', full_name='Qot_GetCodeChange.CodeChangeInfo.publicTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publicTimestamp', full_name='Qot_GetCodeChange.CodeChangeInfo.publicTimestamp', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='effectiveTime', full_name='Qot_GetCodeChange.CodeChangeInfo.effectiveTime', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='effectiveTimestamp', full_name='Qot_GetCodeChange.CodeChangeInfo.effectiveTimestamp', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='Qot_GetCodeChange.CodeChangeInfo.endTime', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTimestamp', full_name='Qot_GetCodeChange.CodeChangeInfo.endTimestamp', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=331,
)


_TIMEFILTER = _descriptor.Descriptor(
  name='TimeFilter',
  full_name='Qot_GetCodeChange.TimeFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Qot_GetCodeChange.TimeFilter.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beginTime', full_name='Qot_GetCodeChange.TimeFilter.beginTime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='Qot_GetCodeChange.TimeFilter.endTime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=395,
)


_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Qot_GetCodeChange.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='placeHolder', full_name='Qot_GetCodeChange.C2S.placeHolder', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='securityList', full_name='Qot_GetCodeChange.C2S.securityList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeFilterList', full_name='Qot_GetCodeChange.C2S.timeFilterList', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='typeList', full_name='Qot_GetCodeChange.C2S.typeList', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=398,
  serialized_end=541,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Qot_GetCodeChange.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='codeChangeList', full_name='Qot_GetCodeChange.S2C.codeChangeList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=543,
  serialized_end=607,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Qot_GetCodeChange.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Qot_GetCodeChange.Request.c2s', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=609,
  serialized_end=655,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Qot_GetCodeChange.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Qot_GetCodeChange.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Qot_GetCodeChange.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Qot_GetCodeChange.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Qot_GetCodeChange.Response.s2c', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=657,
  serialized_end=760,
)

_CODECHANGEINFO.fields_by_name['security'].message_type = Qot__Common__pb2._SECURITY
_CODECHANGEINFO.fields_by_name['relatedSecurity'].message_type = Qot__Common__pb2._SECURITY
_C2S.fields_by_name['securityList'].message_type = Qot__Common__pb2._SECURITY
_C2S.fields_by_name['timeFilterList'].message_type = _TIMEFILTER
_S2C.fields_by_name['codeChangeList'].message_type = _CODECHANGEINFO
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['CodeChangeInfo'] = _CODECHANGEINFO
DESCRIPTOR.message_types_by_name['TimeFilter'] = _TIMEFILTER
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['CodeChangeType'] = _CODECHANGETYPE
DESCRIPTOR.enum_types_by_name['TimeFilterType'] = _TIMEFILTERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CodeChangeInfo = _reflection.GeneratedProtocolMessageType('CodeChangeInfo', (_message.Message,), dict(
  DESCRIPTOR = _CODECHANGEINFO,
  __module__ = 'Qot_GetCodeChange_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCodeChange.CodeChangeInfo)
  ))
_sym_db.RegisterMessage(CodeChangeInfo)

TimeFilter = _reflection.GeneratedProtocolMessageType('TimeFilter', (_message.Message,), dict(
  DESCRIPTOR = _TIMEFILTER,
  __module__ = 'Qot_GetCodeChange_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCodeChange.TimeFilter)
  ))
_sym_db.RegisterMessage(TimeFilter)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Qot_GetCodeChange_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCodeChange.C2S)
  ))
_sym_db.RegisterMessage(C2S)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Qot_GetCodeChange_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCodeChange.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Qot_GetCodeChange_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCodeChange.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Qot_GetCodeChange_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetCodeChange.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pbZ0github.com/futuopen/ftapi4go/pb/qotgetcodechange'))
# @@protoc_insertion_point(module_scope)
