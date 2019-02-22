meta:
  id: lc_auth_info
  endian: le
seq:
  - id: username
    type: strz
    size: 21
    encoding: ISO-8859-1
  - id: unk1 # Probably password
    size: 50
  - id: unk2
    type: u2
  - id: unk3
    size: unk2 # Based on unk2 ?