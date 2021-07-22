KEYS = ('L', 'f', 'd', 's', 'j', 'k', 'l', 'B', 'S')

IMPLICIT_HYPHEN_KEYS = KEYS

KEYMAPS = {
        'Gemini PR': {
            'L': ('S1-', 'S2-'),
            'f': ('H-', 'R-'),
            'd': ('P-', 'W-'),
            's': ('T-', 'K-'),
            'j': ('-F', '-R'),
            'k': ('-P', '-B'),
            'l': ('-L', '-G'),
            'B': ('-T', '-S'),
            'S': ('A-', 'O-', '-E', '-U'),
        },
        'Keyboard': {
            'L': ('q', 'a', 'Return'),
            'f': ('r', 'f'),
            'd': ('e', 'd'),
            's': ('w', 's'),
            'j': ('u', 'j'),
            'k': ('i', 'k'),
            'l': ('o', 'l'),
            'B': ('p', ';', 'BackSpace'),
            'S': ('space', 'g', 'h', 'c', 'v', 'n', 'm'),
            'arpeggiate': ('g', 'h'),
            'no-op': ('x', 'b', ','),
        },
}

UNDO_STROKE_STENO = 'B'

NUMBERS = {}
SUFFIX_KEYS = ()
NUMBER_KEY = None
ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_WORDLIST = None
ORTHOGRAPHY_RULES_ALIASES = {}

DICTIONARIES_ROOT = 'asset:dictionaries'
DEFAULT_DICTIONARIES = (
        'numbers.json',
        'grade1-passage.json',
        'grade1.json',
        'caps.json',
        'brailly.py',
        'cell.py',
        'brf.py',
)
