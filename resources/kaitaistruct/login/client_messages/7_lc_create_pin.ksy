meta:
  id: lc_create_pin
  endian: le
seq:
  - id: password
    type: strz
    encoding: ISO-8859-1
    size: 33 # Last byte is a filler Real value 32
    doc: Password as MD5 Hash
  - id: pin
    type: strz
    encoding: ISO-8859-1
    size: 33 # Last byte is a filler Real value 32
    doc: Pin as MD5 Hash