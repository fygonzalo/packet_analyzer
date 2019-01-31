meta:
  id: packet
  endian: le
seq:
  - id: header
    type: packet_header
  - id: messages
    type: message_container
    repeat: eos
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
  message_container:
    seq:
      - id: length
        type: u2
      - id: body
        type: message_body
        size: length
    types:
      message_body:
        seq:
          - id: code
            type: u2
          - id: content
            type:
              switch-on: code
              cases:
                0: account_info
                2: auth_info
                4: auth_character_delete_client
                5: auth_create_pin_server
                7: auth_create_pin_client
                #7: auth_change_pin_server
                8: auth_delete_pin_server 
                9: auth_change_pin_client
                10: auth_delete_pin_client
                _: unknown_content
        types:
          unknown_content:
            seq:
              - id: unknown
                size-eos: true
          account_info:
            seq:
              - id: error_code # 0 means no error
                type: u2
              - id: flags # Pin. What more?
                type: u2
              - id: character_1
                type: character_info
              - id: unk4
                type: u1
              - id: character_2
                type: character_info
              - id: unk5
                type: u1
              - id: character_3
                type: character_info
              - id: birthday_month
                size: 3
              - id: birthday_day
                size: 3
              - id: blood_type
                size: 3
              - id: chars_hp_full
                type: u4
                repeat: expr
                repeat-expr: 3
              - id: chars_mp_full
                type: u4
                repeat: expr
                repeat-expr: 3
              - id: chars_skills
                type: u4
                repeat: expr
                repeat-expr: 18
              - id: char_slots
                type: u4
              - id: branch_count
                type: u4
              - id: unk3
                size: 51
              - id: branch_status
                type: u4
                repeat: expr
                repeat-expr: branch_count
            types:
              character_info:
                seq:
                  - id: level
                    type: u4
                  - id: faction
                    type: u1
                  - id: shape
                    type: u1
                  - id: hair_style
                    type: u1
                  - id: height
                    type: u1
                  - id: hair_color
                    type: u1
                  - id: skin_color
                    type: u1
                  - id: map
                    type: u4
                  - id: unk1
                    size: 16
                  - id: character_id
                    type: u4
                  - id: nickname
                    type: strz
                    encoding: ISO-8859-1
                    size: 17
                  - id: account_id
                    type: u4
                  - id: username
                    type: strz
                    encoding: ISO-8859-1
                    size: 21
                  - id: equip_head
                    type: u4
                  - id: equip_body
                    type: u4
                  - id: equip_right_hand
                    type: u4
                  - id: equip_left_hand
                    type: u4
                  - id: equip_hands
                    type: u4
                  - id: equip_feet
                    type: u4
                  - id: equip_backpack
                    type: u4
                  - id: equip_ride
                    type: u4
                  - id: hp_left
                    type: u4
                  - id: unk3
                    size: 4
                  - id: mp_left
                    type: u4
                  - id: unk4
                    size: 4
                  - id: title
                    type: strz
                    encoding: ISO-8859-1
                    size: 12
                  - id: unk5
                    size: 5
          auth_info:
            seq:
              - id: username
                type: strz
                size: 21
                encoding: ISO-8859-1
              - id: unk1
                size: 50
              - id: unk2
                type: u2
              - id: unk3
                size: 16 # Based on unk2 ?
          auth_delete_pin_client:
            seq:
             - id: pin # MD5 Hash
               size: 32
          auth_delete_pin_server:
            seq:
             - id: result # Success[1] or Fail[0] to delete Pin
               size: 1
          auth_create_pin_client:
            seq:
             - id: password # MD5 Hash
               size: 33 # Last byte is a filler Real value 32
             - id: pin # MD5 Hash
               size: 33 # Last byte is a filler Real value 32
          auth_create_pin_server:
            seq:
             - id: result # Success[1] or Fail[0] to create Pin
               size: 1
          auth_change_pin_client:
            seq:
             - id: old_pin # MD5 Hash
               size: 33 # Last byte is a filler Real value 32
             - id: new_pin # MD5 Hash
               size: 33 # Last byte is a filler Real value 32
          #auth_change_pin_server:
          #  seq:
          #   - id: result # Success[1] or Fail[0] to create Pin
          #     size: 1
          auth_character_delete_client:
            seq:
             - id: unk1 # MD5 Hash
               size: 4 # Last byte is a filler Real value 32
             - id: animation # MD5 Hash
               size: 24 # Last byte is a filler Real value 32
             - id: unk2
               size: 6