# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Classes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Classes.proto',
  package='Gerenciador',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rClasses.proto\x12\x0bGerenciador\"\xf9\x01\n\x04Time\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\x0f\n\x07tecnico\x18\x02 \x01(\t\x12\x0e\n\x06pontos\x18\x03 \x01(\x05\x12\x10\n\x08qtdJogos\x18\x04 \x01(\x05\x12/\n\x07\x61tletas\x18\x05 \x03(\x0b\x32\x1e.Gerenciador.Time.AtletasEntry\x1a\x43\n\x0c\x41tletasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.Gerenciador.Atleta:\x02\x38\x01\x1a:\n\x07Tecnico\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\r\n\x05idade\x18\x02 \x01(\x05\x12\x12\n\nqtdTitulos\x18\x03 \x01(\x05\"\xd9\x01\n\x06\x41tleta\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12,\n\x07posicao\x18\x02 \x01(\x0e\x32\x1b.Gerenciador.Atleta.Posicao\x12\x11\n\tnumCamisa\x18\x03 \x01(\x05\x12\x12\n\nqtdTitulos\x18\x04 \x01(\x05\x12\x0c\n\x04time\x18\x05 \x01(\t\x12\r\n\x05idade\x18\x06 \x01(\x05\"O\n\x07Posicao\x12\x0b\n\x07GOLEIRO\x10\x00\x12\x0c\n\x08ZAGUEIRO\x10\x01\x12\x0b\n\x07LATERAL\x10\x02\x12\x0e\n\nMEIO_CAMPO\x10\x03\x12\x0c\n\x08\x41TACANTE\x10\x04\"T\n\x07Message\x12\r\n\x05\x65rror\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x0e\n\x06objRef\x18\x03 \x01(\t\x12\x10\n\x08methodID\x18\x04 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x05 \x01(\x0c\x62\x06proto3')
)



_ATLETA_POSICAO = _descriptor.EnumDescriptor(
  name='Posicao',
  full_name='Gerenciador.Atleta.Posicao',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GOLEIRO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZAGUEIRO', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LATERAL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEIO_CAMPO', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATACANTE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=421,
  serialized_end=500,
)
_sym_db.RegisterEnumDescriptor(_ATLETA_POSICAO)


_TIME_ATLETASENTRY = _descriptor.Descriptor(
  name='AtletasEntry',
  full_name='Gerenciador.Time.AtletasEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Gerenciador.Time.AtletasEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Gerenciador.Time.AtletasEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=220,
)

_TIME_TECNICO = _descriptor.Descriptor(
  name='Tecnico',
  full_name='Gerenciador.Time.Tecnico',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nome', full_name='Gerenciador.Time.Tecnico.nome', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='idade', full_name='Gerenciador.Time.Tecnico.idade', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qtdTitulos', full_name='Gerenciador.Time.Tecnico.qtdTitulos', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=222,
  serialized_end=280,
)

_TIME = _descriptor.Descriptor(
  name='Time',
  full_name='Gerenciador.Time',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nome', full_name='Gerenciador.Time.nome', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tecnico', full_name='Gerenciador.Time.tecnico', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pontos', full_name='Gerenciador.Time.pontos', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qtdJogos', full_name='Gerenciador.Time.qtdJogos', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='atletas', full_name='Gerenciador.Time.atletas', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TIME_ATLETASENTRY, _TIME_TECNICO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=280,
)


_ATLETA = _descriptor.Descriptor(
  name='Atleta',
  full_name='Gerenciador.Atleta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nome', full_name='Gerenciador.Atleta.nome', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='posicao', full_name='Gerenciador.Atleta.posicao', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numCamisa', full_name='Gerenciador.Atleta.numCamisa', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qtdTitulos', full_name='Gerenciador.Atleta.qtdTitulos', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='Gerenciador.Atleta.time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='idade', full_name='Gerenciador.Atleta.idade', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ATLETA_POSICAO,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=500,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='Gerenciador.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='Gerenciador.Message.error', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='Gerenciador.Message.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objRef', full_name='Gerenciador.Message.objRef', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='methodID', full_name='Gerenciador.Message.methodID', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='Gerenciador.Message.args', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=502,
  serialized_end=586,
)

_TIME_ATLETASENTRY.fields_by_name['value'].message_type = _ATLETA
_TIME_ATLETASENTRY.containing_type = _TIME
_TIME_TECNICO.containing_type = _TIME
_TIME.fields_by_name['atletas'].message_type = _TIME_ATLETASENTRY
_ATLETA.fields_by_name['posicao'].enum_type = _ATLETA_POSICAO
_ATLETA_POSICAO.containing_type = _ATLETA
DESCRIPTOR.message_types_by_name['Time'] = _TIME
DESCRIPTOR.message_types_by_name['Atleta'] = _ATLETA
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Time = _reflection.GeneratedProtocolMessageType('Time', (_message.Message,), dict(

  AtletasEntry = _reflection.GeneratedProtocolMessageType('AtletasEntry', (_message.Message,), dict(
    DESCRIPTOR = _TIME_ATLETASENTRY,
    __module__ = 'Classes_pb2'
    # @@protoc_insertion_point(class_scope:Gerenciador.Time.AtletasEntry)
    ))
  ,

  Tecnico = _reflection.GeneratedProtocolMessageType('Tecnico', (_message.Message,), dict(
    DESCRIPTOR = _TIME_TECNICO,
    __module__ = 'Classes_pb2'
    # @@protoc_insertion_point(class_scope:Gerenciador.Time.Tecnico)
    ))
  ,
  DESCRIPTOR = _TIME,
  __module__ = 'Classes_pb2'
  # @@protoc_insertion_point(class_scope:Gerenciador.Time)
  ))
_sym_db.RegisterMessage(Time)
_sym_db.RegisterMessage(Time.AtletasEntry)
_sym_db.RegisterMessage(Time.Tecnico)

Atleta = _reflection.GeneratedProtocolMessageType('Atleta', (_message.Message,), dict(
  DESCRIPTOR = _ATLETA,
  __module__ = 'Classes_pb2'
  # @@protoc_insertion_point(class_scope:Gerenciador.Atleta)
  ))
_sym_db.RegisterMessage(Atleta)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'Classes_pb2'
  # @@protoc_insertion_point(class_scope:Gerenciador.Message)
  ))
_sym_db.RegisterMessage(Message)


_TIME_ATLETASENTRY._options = None
# @@protoc_insertion_point(module_scope)
