# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Classes.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rClasses.proto\x12\x0bGerenciador\"\xf9\x01\n\x04Time\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\x0f\n\x07tecnico\x18\x02 \x01(\t\x12\x0e\n\x06pontos\x18\x03 \x01(\x05\x12\x10\n\x08qtdJogos\x18\x04 \x01(\x05\x12/\n\x07\x61tletas\x18\x05 \x03(\x0b\x32\x1e.Gerenciador.Time.AtletasEntry\x1a\x43\n\x0c\x41tletasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.Gerenciador.Atleta:\x02\x38\x01\x1a:\n\x07Tecnico\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\r\n\x05idade\x18\x02 \x01(\x05\x12\x12\n\nqtdTitulos\x18\x03 \x01(\x05\"\xe6\x01\n\x06\x41tleta\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12,\n\x07posicao\x18\x02 \x01(\x0e\x32\x1b.Gerenciador.Atleta.Posicao\x12\x11\n\tnumCamisa\x18\x03 \x01(\x05\x12\x12\n\nqtdTitulos\x18\x04 \x01(\x05\x12\x0c\n\x04time\x18\x05 \x01(\t\x12\r\n\x05idade\x18\x06 \x01(\x05\"\\\n\x07Posicao\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0c\n\x08ZAGUEIRO\x10\x01\x12\x0b\n\x07LATERAL\x10\x02\x12\x0e\n\nMEIO_CAMPO\x10\x03\x12\x0c\n\x08\x41TACANTE\x10\x04\x12\x0b\n\x07GOLEIRO\x10\x05\"T\n\x07Message\x12\r\n\x05\x65rror\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x0e\n\x06objRef\x18\x03 \x01(\t\x12\x10\n\x08methodID\x18\x04 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x05 \x01(\x0c\x62\x06proto3')



_TIME = DESCRIPTOR.message_types_by_name['Time']
_TIME_ATLETASENTRY = _TIME.nested_types_by_name['AtletasEntry']
_TIME_TECNICO = _TIME.nested_types_by_name['Tecnico']
_ATLETA = DESCRIPTOR.message_types_by_name['Atleta']
_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
_ATLETA_POSICAO = _ATLETA.enum_types_by_name['Posicao']
Time = _reflection.GeneratedProtocolMessageType('Time', (_message.Message,), {

  'AtletasEntry' : _reflection.GeneratedProtocolMessageType('AtletasEntry', (_message.Message,), {
    'DESCRIPTOR' : _TIME_ATLETASENTRY,
    '__module__' : 'Classes_pb2'
    # @@protoc_insertion_point(class_scope:Gerenciador.Time.AtletasEntry)
    })
  ,

  'Tecnico' : _reflection.GeneratedProtocolMessageType('Tecnico', (_message.Message,), {
    'DESCRIPTOR' : _TIME_TECNICO,
    '__module__' : 'Classes_pb2'
    # @@protoc_insertion_point(class_scope:Gerenciador.Time.Tecnico)
    })
  ,
  'DESCRIPTOR' : _TIME,
  '__module__' : 'Classes_pb2'
  # @@protoc_insertion_point(class_scope:Gerenciador.Time)
  })
_sym_db.RegisterMessage(Time)
_sym_db.RegisterMessage(Time.AtletasEntry)
_sym_db.RegisterMessage(Time.Tecnico)

Atleta = _reflection.GeneratedProtocolMessageType('Atleta', (_message.Message,), {
  'DESCRIPTOR' : _ATLETA,
  '__module__' : 'Classes_pb2'
  # @@protoc_insertion_point(class_scope:Gerenciador.Atleta)
  })
_sym_db.RegisterMessage(Atleta)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'Classes_pb2'
  # @@protoc_insertion_point(class_scope:Gerenciador.Message)
  })
_sym_db.RegisterMessage(Message)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TIME_ATLETASENTRY._options = None
  _TIME_ATLETASENTRY._serialized_options = b'8\001'
  _TIME._serialized_start=31
  _TIME._serialized_end=280
  _TIME_ATLETASENTRY._serialized_start=153
  _TIME_ATLETASENTRY._serialized_end=220
  _TIME_TECNICO._serialized_start=222
  _TIME_TECNICO._serialized_end=280
  _ATLETA._serialized_start=283
  _ATLETA._serialized_end=513
  _ATLETA_POSICAO._serialized_start=421
  _ATLETA_POSICAO._serialized_end=513
  _MESSAGE._serialized_start=515
  _MESSAGE._serialized_end=599
# @@protoc_insertion_point(module_scope)
