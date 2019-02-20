meta:
  id: auth_info
  endian: le
seq:
  - id: username
    type: strz
    size: 21
    encoding: ISO-8859-1
  - id: unk1
    size: 50
  - id: unk2
    type: u2
  - id: unk3
    size: 16 # Based on unk2 ?