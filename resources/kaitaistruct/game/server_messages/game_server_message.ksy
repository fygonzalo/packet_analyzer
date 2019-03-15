meta:
  id: game_server_message
  endian: le
  imports:
    - 2_gs_character_info
    - 12_gs_game_server_address
    - 39_gs_friends_list
    - 64_gs_friends_black_list
    - 305_gs_map_world_leagues
params:
  - id: code
    type: u2
seq:
  - id: content
    size-eos: true
    type:
      switch-on: code
      cases:
        2: gs_character_info
        12: gs_game_server_address
        39: gs_friends_list
        64: gs_friends_black_list
        305: gs_map_world_leagues
        _: unknown
types:
  unknown:
     seq:
      - id: payload
        size-eos: true