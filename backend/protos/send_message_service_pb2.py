# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/send_message_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/send_message_service.proto',
  package='send_message_service',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!protos/send_message_service.proto\x12\x14send_message_service\"X\n\nSMSRequest\x12\x18\n\x0brecipientID\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x0e\n\x0c_recipientIDB\n\n\x08_message\"\'\n\x0bSMSResponse\x12\x10\n\x03ref\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x06\n\x04_ref2c\n\x0bSendMessage\x12T\n\x0bsendTextSMS\x12 .send_message_service.SMSRequest\x1a!.send_message_service.SMSResponse\"\x00\x62\x06proto3'
)




_SMSREQUEST = _descriptor.Descriptor(
  name='SMSRequest',
  full_name='send_message_service.SMSRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='recipientID', full_name='send_message_service.SMSRequest.recipientID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='send_message_service.SMSRequest.message', index=1,
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
    _descriptor.OneofDescriptor(
      name='_recipientID', full_name='send_message_service.SMSRequest._recipientID',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_message', full_name='send_message_service.SMSRequest._message',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=59,
  serialized_end=147,
)


_SMSRESPONSE = _descriptor.Descriptor(
  name='SMSResponse',
  full_name='send_message_service.SMSResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ref', full_name='send_message_service.SMSResponse.ref', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='_ref', full_name='send_message_service.SMSResponse._ref',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=149,
  serialized_end=188,
)

_SMSREQUEST.oneofs_by_name['_recipientID'].fields.append(
  _SMSREQUEST.fields_by_name['recipientID'])
_SMSREQUEST.fields_by_name['recipientID'].containing_oneof = _SMSREQUEST.oneofs_by_name['_recipientID']
_SMSREQUEST.oneofs_by_name['_message'].fields.append(
  _SMSREQUEST.fields_by_name['message'])
_SMSREQUEST.fields_by_name['message'].containing_oneof = _SMSREQUEST.oneofs_by_name['_message']
_SMSRESPONSE.oneofs_by_name['_ref'].fields.append(
  _SMSRESPONSE.fields_by_name['ref'])
_SMSRESPONSE.fields_by_name['ref'].containing_oneof = _SMSRESPONSE.oneofs_by_name['_ref']
DESCRIPTOR.message_types_by_name['SMSRequest'] = _SMSREQUEST
DESCRIPTOR.message_types_by_name['SMSResponse'] = _SMSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SMSRequest = _reflection.GeneratedProtocolMessageType('SMSRequest', (_message.Message,), {
  'DESCRIPTOR' : _SMSREQUEST,
  '__module__' : 'protos.send_message_service_pb2'
  # @@protoc_insertion_point(class_scope:send_message_service.SMSRequest)
  })
_sym_db.RegisterMessage(SMSRequest)

SMSResponse = _reflection.GeneratedProtocolMessageType('SMSResponse', (_message.Message,), {
  'DESCRIPTOR' : _SMSRESPONSE,
  '__module__' : 'protos.send_message_service_pb2'
  # @@protoc_insertion_point(class_scope:send_message_service.SMSResponse)
  })
_sym_db.RegisterMessage(SMSResponse)



_SENDMESSAGE = _descriptor.ServiceDescriptor(
  name='SendMessage',
  full_name='send_message_service.SendMessage',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=190,
  serialized_end=289,
  methods=[
  _descriptor.MethodDescriptor(
    name='sendTextSMS',
    full_name='send_message_service.SendMessage.sendTextSMS',
    index=0,
    containing_service=None,
    input_type=_SMSREQUEST,
    output_type=_SMSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SENDMESSAGE)

DESCRIPTOR.services_by_name['SendMessage'] = _SENDMESSAGE

# @@protoc_insertion_point(module_scope)
