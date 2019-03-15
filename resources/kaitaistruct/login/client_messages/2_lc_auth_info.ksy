meta:
  id: lc_auth_info
  endian: le
seq:
  - id: username
    type: strz
    size: 21
    encoding: ISO-8859-1
  - id: password
    size: 33
    type: strz
    encoding: ISO-8859-1
  - id: unk4 # Appears also in 2_gc_auth_info
    size: 17
    type: strz
    encoding: ISO-8859-1
  - id: unk2
    type: u2
  - id: unk3
    size: unk2 # Based on unk2 ?