meta:
  id: gc_auth_info
  endian: le
seq:
  - id: unk1 # Related to network connection?
    size: 17
  - id: account_id
    type: u4
  - id: character_id
    type: u4
  - id: stage
    type: u4
  - id: session_id # not confirmed
    type: u4