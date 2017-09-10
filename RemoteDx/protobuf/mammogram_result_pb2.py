# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mammogram_result.proto

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




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mammogram_result.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x16mammogram_result.proto\"s\n\x0fMammogramResult\x12\x10\n\x08image_id\x18\x01 \x02(\t\x12\r\n\x05width\x18\x02 \x02(\x05\x12\x0e\n\x06height\x18\x03 \x02(\x05\x12\r\n\x05score\x18\x04 \x02(\x02\x12 \n\x06imtype\x18\x05 \x02(\x0e\x32\x10.ResultImageType*H\n\x0fResultImageType\x12\t\n\x05UINT8\x10\x00\x12\n\n\x06UINT16\x10\x01\x12\x0b\n\x07\x46LOAT32\x10\x02\x12\x07\n\x03RGB\x10\x03\x12\x08\n\x04RGBA\x10\x04')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_RESULTIMAGETYPE = _descriptor.EnumDescriptor(
  name='ResultImageType',
  full_name='ResultImageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UINT8', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT16', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT32', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RGB', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RGBA', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=143,
  serialized_end=215,
)
_sym_db.RegisterEnumDescriptor(_RESULTIMAGETYPE)

ResultImageType = enum_type_wrapper.EnumTypeWrapper(_RESULTIMAGETYPE)
UINT8 = 0
UINT16 = 1
FLOAT32 = 2
RGB = 3
RGBA = 4



_MAMMOGRAMRESULT = _descriptor.Descriptor(
  name='MammogramResult',
  full_name='MammogramResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_id', full_name='MammogramResult.image_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='MammogramResult.width', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='MammogramResult.height', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='MammogramResult.score', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imtype', full_name='MammogramResult.imtype', index=4,
      number=5, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=26,
  serialized_end=141,
)

_MAMMOGRAMRESULT.fields_by_name['imtype'].enum_type = _RESULTIMAGETYPE
DESCRIPTOR.message_types_by_name['MammogramResult'] = _MAMMOGRAMRESULT
DESCRIPTOR.enum_types_by_name['ResultImageType'] = _RESULTIMAGETYPE

MammogramResult = _reflection.GeneratedProtocolMessageType('MammogramResult', (_message.Message,), dict(
  DESCRIPTOR = _MAMMOGRAMRESULT,
  __module__ = 'mammogram_result_pb2'
  # @@protoc_insertion_point(class_scope:MammogramResult)
  ))
_sym_db.RegisterMessage(MammogramResult)


# @@protoc_insertion_point(module_scope)
