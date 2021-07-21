brf = {
        'L' : '\n',
        'S' : ' ',
        'l' : ',',
        'k' : '\"',
        'kl' : ';',
        'j' : '@',
        'jl' : '.',
        'jk' : '^',
        'jkl' : '_',
        's' : '\'',
        'sl' : '-',
        'sk' : '9',
        'skl' : '0',
        'sj' : '/',
        'sjl' : '%',
        'sjk' : '>',
        'sjkl' : '#',
        'd' : '1',
        'dl' : '5',
        'dk' : '3',
        'dkl' : '4',
        'dj' : 'I',
        'djl' : '[',
        'djk' : 'J',
        'djkl' : 'W',
        'ds' : '2',
        'dsl' : '8',
        'dsk' : '6',
        'dskl' : '7',
        'dsj' : 'S',
        'dsjl' : '!',
        'dsjk' : 'T',
        'dsjkl' : ')',
        'f' : 'A',
        'fl' : '*',
        'fk' : 'E',
        'fkl' : ':',
        'fj' : 'C',
        'fjl' : '%',
        'fjk' : 'D',
        'fjkl' : '?',
        'fs' : 'K',
        'fsl' : 'U',
        'fsk' : 'O',
        'fskl' : 'Z',
        'fsj' : 'M',
        'fsjl' : 'X',
        'fsjk' : 'N',
        'fsjkl' : 'Y',
        'fd' : 'B',
        'fdl' : '<',
        'fdk' : 'H',
        'fdkl' : '\\',
        'fdj' : 'F',
        'fdjl' : '$',
        'fdjk' : 'G',
        'fdjkl' : ']',
        'fds' : 'L',
        'fdsl' : 'V',
        'fdsk' : 'R',
        'fdskl' : '(',
        'fdsj' : 'P',
        'fdsjl' : '&',
        'fdsjk' : 'Q',
        'fdsjkl' : '=',
        'LfdB' : '{plover:toggle_dict:-brf.py,+braille.py}'
}

LONGEST_KEY = 1

def lookup(stroke):
    if stroke[0] not in brf:
        if stroke == ('B',):
            raise KeyError
        else:
            return '{&[' + stroke[0] + ']}'
    output = brf[stroke[0]]
    if 'toggle_dict' in output:
        return output
    else:
        return '{&' + brf[stroke[0]] + '}'
