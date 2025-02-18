
image animated_ctc:
    yoffset 8
    xoffset 12
    "gui/ctc_1.png"
    pause 0.5
    "gui/ctc_2.png"
    pause 0.5
    repeat

define npc_name = "???"
define npc_name2 = "???"
define npc = Character("npc_name", ctc="animated_ctc", ctc_position="nestled", dynamic=True)
define npc2 = Character("npc_name2", ctc="animated_ctc", ctc_position="nestled", dynamic=True)

define sp_mn = Character("", ctc="animated_ctc", ctc_position="nestled")
define adh = Character("Andhra", ctc="animated_ctc", ctc_position="nestled")
define eka = Character("Eka", image="eka", ctc="animated_ctc", ctc_position="nestled")
define riz = Character("Rizky", image="rizky", ctc="animated_ctc", ctc_position="nestled")
define tia = Character("Tiara", image="tiara", ctc="animated_ctc", ctc_position="nestled")
define tam = Character("Tama", image="tama", ctc="animated_ctc", ctc_position="nestled")
define flo = Character("Flora", image="flora", ctc="animated_ctc", ctc_position="nestled")
define ina = Character("Intan", image="intan", ctc="animated_ctc", ctc_position="nestled")
define lut = Character("Luthfi", image="luthfi", ctc="animated_ctc", ctc_position="nestled")
define sty = Character("Setya", image="setya", ctc="animated_ctc", ctc_position="nestled")

# Special Characters
# Centered text dialogue, for dream sequences
define sp_n = Character(
    None,
    kind=centered,
    window_background = None, 
    what_size = 48, what_xalign=0.5, what_yalign=0, what_textalign=0.5, what_layout='subtitle',
    )

define sp_mic = Character(
    "Intercom",
    what_prefix="{b}{i}",
    what_suffix="{/i}{/b}",
    who_prefix="[[",
    who_suffix="]",
    ctc="animated_ctc", ctc_position="nestled"
)

# Future Andhra's narration 
define sp_adh = Character(
    None,
    what_prefix="{i}",
    what_suffix="{/i}",
    what_color="#b4d3e4",
    ctc="animated_ctc", ctc_position="nestled"
)