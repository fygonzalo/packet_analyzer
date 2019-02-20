meta:
  id: packet
  endian: le
  imports:
    - server_messages/server_message
params:
  - id: source
    type: str
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
                  switch-on: _root.source
                  cases:
                    '"Server"': server_message(code)
                    '"Client"': client_message(code)