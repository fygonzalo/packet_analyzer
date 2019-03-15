meta:
  id: ls_game_server_address
  endian: le
seq:
  - id: unk1
    size: 2
  - id: session_id # Related to 2_gc_auth_info. Not confirmed.
    type: u4
  - id: unk4 # Seems to be 2. Related to client "state machine"?
    size: 1
  - id: ip
    type: strz
    encoding: ISO-8859-1
    size: 16
  - id: port
    type: u2
  - id: unk2
    size-eos: true