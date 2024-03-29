cell = {
       'L' : '\n',
       'S' : '⠀',
       'l' : '⠠',
       'k' : '⠐',
       'kl' : '⠰',
       'j' : '⠈',
       'jl' : '⠨',
       'jk' : '⠘',
       'jkl' : '⠸',
       's' : '⠄',
       'sl' : '⠤',
       'sk' : '⠔',
       'skl' : '⠴',
       'sj' : '⠌',
       'sjl' : '⠬',
       'sjk' : '⠜',
       'sjkl' : '⠼',
       'd' : '⠂',
       'dl' : '⠢',
       'dk' : '⠒',
       'dkl' : '⠲',
       'dj' : '⠊',
       'djl' : '⠪',
       'djk' : '⠚',
       'djkl' : '⠺',
       'ds' : '⠆',
       'dsl' : '⠦',
       'dsk' : '⠖',
       'dskl' : '⠶',
       'dsj' : '⠎',
       'dsjl' : '⠮',
       'dsjk' : '⠞',
       'dsjkl' : '⠾',
       'f' : '⠁',
       'fl' : '⠡',
       'fk' : '⠑',
       'fkl' : '⠱',
       'fj' : '⠉',
       'fjl' : '⠩',
       'fjk' : '⠙',
       'fjkl' : '⠹',
       'fs' : '⠅',
       'fsl' : '⠥',
       'fsk' : '⠕',
       'fskl' : '⠵',
       'fsj' : '⠍',
       'fsjl' : '⠭',
       'fsjk' : '⠝',
       'fsjkl' : '⠽',
       'fd' : '⠃',
       'fdl' : '⠣',
       'fdk' : '⠓',
       'fdkl' : '⠳',
       'fdj' : '⠋',
       'fdjl' : '⠫',
       'fdjk' : '⠛',
       'fdjkl' : '⠻',
       'fds' : '⠇',
       'fdsl' : '⠧',
       'fdsk' : '⠗',
       'fdskl' : '⠷',
       'fdsj' : '⠏',
       'fdsjl' : '⠯',
       'fdsjk' : '⠟',
       'fdsjkl' : '⠿',
       'LfjB' : '{plover:toggle_dict:-cell.py,+braille.py}'
}

LONGEST_KEY = 1

def lookup(stroke):
    if stroke[0] not in cell:
        if stroke == ('B',):
            raise KeyError
        else:
            return '{&[' + stroke[0] + ']}'
    output = cell[stroke[0]]
    if 'toggle_dict' in output:
        return output
    else:
        return '{&' + cell[stroke[0]] + '}'
