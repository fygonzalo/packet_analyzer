meta:
  id: login_client_message
  endian: le
  imports:
    - 2_lc_auth_info
    - 7_lc_create_pin
    - 9_lc_change_pin
    - 10_lc_delete_pin
params:
  - id: code
    type: u2
seq:
  - id: content
    size-eos: true
    type:
      switch-on: code
      cases:
        2: lc_auth_info
        7: lc_create_pin
        9: lc_change_pin
        10: lc_delete_pin
        _: unknown
types:
  unknown:
     seq:
      - id: payload
        size-eos: true