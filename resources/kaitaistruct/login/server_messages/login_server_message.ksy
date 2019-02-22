meta:
  id: login_server_message
  endian: le
  imports:
    - 0_ls_account_info
    - 4_ls_game_server_address
    - 5_ls_create_pin
    - 7_ls_change_pin
    - 8_ls_delete_pin
    - 12_ls_announcement
params:
  - id: code
    type: u2
seq:
  - id: content
    size-eos: true
    type:
      switch-on: code
      cases:
        0: ls_account_info
        4: ls_game_server_address
        5: ls_create_pin
        7: ls_change_pin
        8: ls_delete_pin
        12: ls_announcement
        _: unknown
types:
  unknown:
     seq:
      - id: payload
        size-eos: true