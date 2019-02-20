meta:
  id: server_message
  endian: le
  imports:
    - 0_account_info
params:
  - id: code
    type: u2
seq:
  - id: content
    size-eos: true
    type:
      switch-on: code
      cases:
        0: account_info
        _: unknown
types:
  unknown:
     seq:
      - id: payload
        size-eos: true