meta:
  id: packet
  endian: le
  imports:
    - game/server_messages/game_server_message
    - game/client_messages/game_client_message
    - login/server_messages/login_server_message
    - login/client_messages/login_client_message
params:
  - id: network_source
    type: u4
  - id: server_type
    type: u4
seq:
  - id: header
    type: packet_header
  - id: content
    type: messages_list
types:
  packet_header:
    seq:
      - id: length
        type: u2
      - id: sequence
        type: s2
      - id: flags
        type: packet_flags
      - id: checksum
        type: s1
    types:
      packet_flags:
        seq:
          - id: compression
            type: b1
          - id: unknown
            type: b6
          - id: encryption
            type: b1
  messages_list:
    seq:
      - id: container
        type: message_container
        repeat: eos
    types:
      message_container:
        seq:
          - id: length
            type: u2
          - id: content
            type: message
            size: length
        types:
          message:
            seq:
              - id: code
                type: u2
              - id: content
                size-eos: true
                type:
                  switch-on: _root.network_source + (2 * _root.server_type)
                  cases:
                    0: game_server_message(code)
                    1: game_client_message(code)
                    2: login_server_message(code)
                    3: login_client_message(code)