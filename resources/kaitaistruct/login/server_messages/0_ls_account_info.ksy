meta:
  id: ls_account_info
  endian: le
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
      - id: stage
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