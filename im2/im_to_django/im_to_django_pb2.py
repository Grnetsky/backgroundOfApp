# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: im_to_django.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='im_to_django.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12im_to_django.proto\"\x19\n\x08rsp_data\x12\r\n\x05token\x18\x02 \x01(\t\"\t\n\x07\x61rticle\"/\n\x08req_data\x12\x12\n\nuser_exist\x18\x01 \x01(\x08\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x32\x31\n\x04name\x12)\n\x0ftokrn_interface\x12\t.rsp_data\x1a\t.req_data\"\x00\x62\x06proto3'
)




_RSP_DATA = _descriptor.Descriptor(
  name='rsp_data',
  full_name='rsp_data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='rsp_data.token', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=47,
)


_ARTICLE = _descriptor.Descriptor(
  name='article',
  full_name='article',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=58,
)


_REQ_DATA = _descriptor.Descriptor(
  name='req_data',
  full_name='req_data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_exist', full_name='req_data.user_exist', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='req_data.user_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['rsp_data'] = _RSP_DATA
DESCRIPTOR.message_types_by_name['article'] = _ARTICLE
DESCRIPTOR.message_types_by_name['req_data'] = _REQ_DATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

rsp_data = _reflection.GeneratedProtocolMessageType('rsp_data', (_message.Message,), {
  'DESCRIPTOR' : _RSP_DATA,
  '__module__' : 'im_to_django_pb2'
  # @@protoc_insertion_point(class_scope:rsp_data)
  })
_sym_db.RegisterMessage(rsp_data)

article = _reflection.GeneratedProtocolMessageType('article', (_message.Message,), {
  'DESCRIPTOR' : _ARTICLE,
  '__module__' : 'im_to_django_pb2'
  # @@protoc_insertion_point(class_scope:article)
  })
_sym_db.RegisterMessage(article)

req_data = _reflection.GeneratedProtocolMessageType('req_data', (_message.Message,), {
  'DESCRIPTOR' : _REQ_DATA,
  '__module__' : 'im_to_django_pb2'
  # @@protoc_insertion_point(class_scope:req_data)
  })
_sym_db.RegisterMessage(req_data)



_NAME = _descriptor.ServiceDescriptor(
  name='name',
  full_name='name',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=109,
  serialized_end=158,
  methods=[
  _descriptor.MethodDescriptor(
    name='tokrn_interface',
    full_name='name.tokrn_interface',
    index=0,
    containing_service=None,
    input_type=_RSP_DATA,
    output_type=_REQ_DATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NAME)

DESCRIPTOR.services_by_name['name'] = _NAME

# @@protoc_insertion_point(module_scope)
