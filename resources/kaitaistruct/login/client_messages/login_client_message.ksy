meta:
  id: login_client_message
  endian: le
  imports:
    - 2_lc_auth_info
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
        _: unknown
types:
  unknown:
     seq:
      - id: payload
        size-eos: true