# colors
BLACK = (   0,   0,   0)
GREEN = (   0, 200,   0)
RED   = ( 255,   0,   0)
WHITE = ( 255, 255, 255)

FIELDS_X = 11
FIELDS_Y = 11
FIELD_SIZE_WIDTH = 64
FIELD_SIZE_HEIGHT = 64

size = (FIELDS_X*FIELD_SIZE_WIDTH, FIELDS_Y*FIELD_SIZE_HEIGHT)

PLAYER_BOMB_SIZE = 1
PLAYER_MAX_BOMBS = 1
PLAYER_RUNSPEED = 5

BOMB_TIMER = 90
EXPLOSION_EXPAND = 1
EXP_DURATION = 15

EXP_INITIAL = 6
# EXP_CENTER = "type_c"
EXP_CENTER_X = 4
EXP_CENTER_T = 5
EXP_CENTER_U = 0
EXP_CENTER_L = 3
EXP_CENTER_B = EXP_BRIDGE = 1
EXP_END = 2
EXP_UP = 360
EXP_RIGHT = -90
EXP_DOWN = 180
EXP_LEFT = 90

CENTER_DICTIONARY = {'1000': (EXP_CENTER_U, EXP_UP), '0100': (EXP_CENTER_U, EXP_RIGHT), '0010': (EXP_CENTER_U, EXP_DOWN), '0001': (EXP_CENTER_U, EXP_LEFT),
                     '1100': (EXP_CENTER_L, EXP_UP), '0110': (EXP_CENTER_L, EXP_RIGHT), '0011': (EXP_CENTER_L, EXP_DOWN), '1001': (EXP_CENTER_L, EXP_LEFT),
                     '1010': (EXP_CENTER_B, EXP_UP), '0101': (EXP_CENTER_B, EXP_RIGHT),
                     '1110': (EXP_CENTER_T, EXP_UP), '0111': (EXP_CENTER_T, EXP_RIGHT), '1011': (EXP_CENTER_T, EXP_DOWN), '1101': (EXP_CENTER_T, EXP_LEFT),
                     '1111': (EXP_CENTER_X, EXP_UP)}