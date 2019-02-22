meta:
  id: game_server_message
  endian: le
  imports:
    - 12_gs_game_server_address
params:
  - id: code
    type: u2
seq:
  - id: content
    size-eos: true
    type:
      switch-on: code
      cases:
        12: gs_game_server_address
        _: unknown
types:
  unknown:
     seq:
      - id: payload
        size-eos: true