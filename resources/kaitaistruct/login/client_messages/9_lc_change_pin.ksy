meta:
  id: lc_change_pin
  endian: le
seq:
  - id: old_pin # MD5 Hash
    size: 33 # Last byte is a null terminator
    type: strz
    encoding: ISO-8859-1
  - id: new_pin # MD5 Hash
    size: 33 # Last byte is a null terminator
    type: strz
    encoding: ISO-8859-1