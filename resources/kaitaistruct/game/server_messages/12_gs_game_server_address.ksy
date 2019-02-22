meta:
  id: gs_game_server_address
  endian: le
seq:
  - id: stage
    type: u4
    doc: stage to connect
  - id: port
    type: u2
  - id: ip
    type: strz
    encoding: ISO-8859-1
    size: 16
  - id: unk2
    size-eos: true