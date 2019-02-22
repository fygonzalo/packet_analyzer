meta:
  id: ls_game_server_address
  endian: le
seq:
  - id: unk1
    size: 7
  - id: ip
    type: strz
    encoding: ISO-8859-1
    size: 16
  - id: port
    type: u2
  - id: unk2
    size-eos: true