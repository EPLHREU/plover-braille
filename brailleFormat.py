def show(obj):
    temp = vars(obj)
    print('type: ' + str(type(obj)))
    for item in temp:
        print(item, ':', temp[item])

def reverse(lst):
    return [ele for ele in reversed(lst)]

def tr(letters):
    translateDict = {                            
            'f': '1',                                    
            'd': '2',                 
            's': '3',                     
            'j': '4',                      
            'k': '5',                              
            'l': '6',                                                       
            'B': 'B',                                   
            'L': 'L',                                             
            'S': 'S',                                             
            }                                     
    ret = ''
    for l in letters:
        if l in translateDict:
            ret = ret + translateDict[l]
        else:
            ret = ret + l
    return ret

alphabeticWordsigns = {
        '12': 'but', '14': 'can', '145': 'do', '15': 'every', '124': 'from', '1245': 'go',
        '125': 'have', '245': 'just', '13': 'knowledge', '123': 'like', '134': 'more', '1345': 'not',
        '1234': 'people', '12345': 'quite', '1235': 'rather', '234': 'so', '2345': 'that', '136': 'us',
        '1236': 'very', '1346': 'it', '13456': 'you', '1356': 'as', '2456': 'will', }
contractionsStrokes = {
        '16': 'child', '146': 'shall', '1456': 'this', '156': 'which', '1256': 'out', '34': 'still',
        '23': 'be', '26': 'enough', '2356': 'were', '236': 'his', '35': 'in', '356': 'was',
        "1/12" : "about", "1/12/1236" : "above", "1/14"  : "according", "1/14/1235" : "across", "1/124" : "after", "1/124/1345" : "afternoon",
        "1/124/2456" : "afterward", "1/1245" : "again", "1/1245/34" : "against", "1/123/134" : "almost", "1/123/1235" : "already", "1/123" : "also",
        "1/123/1456" : "although", "1/123/2345" : "altogether", "1/123/2456": "always", "23/13" :  "because", "23/124" : "before", "23/125" : "behind",
        "23/123" : "below", "23/1345": "beneath", "23/234" : "beside", "23/2345" : "between", "23/13456" : "beyond", "12/123" : "blind",
        "12/1235/123" : "braille", "16/1345" : "children", "25/14/1236" : "conceive", "25/14/1236/1245" : "conceiving", "14/145" : "could", "145/14/1236" : "deceive",
        "145/14/1236/1245" : "deceiving", "145/14/123" : "declare", "145/14/123/1245" : "declaring", "15/24" : "either", "124/34" : "first", "124/1235" : "friend",
        "1245/145" : "good", "1245/1235/2345" : "great", "125/12456/124" : "herself", "125/134" : "him", "125/134/124" : "himself", "24/134/134" : "immediate",
        "1346/234" : "its", "1346/124" : "itself", "123/1235" : "letter", "123/123" : "little", "134/16" : "much", "134/34" : "must",
        "134/13456/124" : "myself", "1345/15/14" : "necessary", "1345/15/24" : "neither", "5/135/124" : "oneself", "1256/1235/234" : "ourselves", "1234/145" : "paid",
        "1234/12456/14/1236" : "perceive", "1234/12456/14/1236/1245" : "perceiving", "1234/12456/125" : "perhaps", "12345/13" : "quick", "1235/14/1236" : "receive", "1235/14/1236/1245" : "receiving",
        "1235/245/14" : "rejoice", "1235/245/14/1245" : "rejoicing", "234/145" : "said", "146/145" : "should", "234/16" : "such", "2346/134/1236/234" : "themselves",
        "1456/13456/124" : "thyself", "2345/145" : "today", "2345/1245/1235" : "together", "2345/134" : "tomorrow", "2345/1345" : "tonight", "2456/145" : "would",
        "13456/1235" : "your", "13456/1235/124" : "yourself", "13456/1235/1236/234" : "youselves", }
contractionsStrokes.update(alphabeticWordsigns)

def ff(ctx, action):
    return action

def contains(text, substrings):
    for s in substrings:
        if s in text:
            return True
    return False

def format(ctx, cmdline):
    history = ctx.previous_translations
    rhistory = reverse(history)

    ret = ctx.new_action()
    ret.prev_attach = True
    ret.next_attach = True
    ret.glue = True

    if cmdline == '-|':
        ret.text = ' '
        ret.command = '-|'
        return ret

    starting = ['', ' ', '–', '—', '——', '(', '[', '{', '“', '“', '‘', '«', '"', '“', '\'', '[CS]', 'cw', 'cp', '[TNO]', '\\']
    ending = ['', ' ', '–', '—', '——', ',', ':', '.', '…', '!', '?', ')', ']', '}', '”', '”', '’', '»', '"', '\'', ('capital', 'terminator'), 'ctn', '\\']
    modifiers = ['\u0338', '\u0335', '\u0306', '\u0304', '\u0327', '\u0300', '\u0302', '\u030A', '\u0303', '\u0308', '\u0301', '\u030C']


    # modifiers code
    if len(history) > 1 and history[-1].formatting != None and history[-1].formatting[0].text != '' and type(history[-1].formatting[0].text) == str:
        lastChar = history[-1].formatting[0].text[-1] 
        if lastChar in modifiers:
            lastLastChar = history[-1].formatting[0].text[-2] 
            if lastLastChar == ' ':
                ret.prev_replace = lastChar
                ret.text = cmdline + lastChar
                return ff(ctx, ret)

    word = ''
    strokes = []
    found = False
    for h in reverse(ctx.previous_translations):
        if found == True:
            break
        if h.formatting == []:
            break
        text = h.formatting[0].text
        stroke = h.strokes[0].rtfcre
        if text == None:
            break
        for letter in reverse(text):
            if word == '' and letter == '“':
                word = word + letter
            if letter.lower() in starting or letter == "\n":
                found = True
                break
            if h.formatting[0].glue == False:
                found = True
                break
            word = word + letter.lower()
        strokes.append(stroke)
    word = word[::-1]
    strokes = tr("/".join(strokes[::-1][1:]))

    if len(ctx.previous_translations) < 2:
        previousText = ' '
    else:
        if ctx.previous_translations[-2].formatting == []:
            previousText = ' '
        if ctx.previous_translations[-2].formatting[0].text == None:
            previousText = ' '
        else:
            previousText = ctx.previous_translations[-1].formatting[0].text
            if previousText == None:
                previousText = ''
            else:
                previousText = previousText#.lower()

    g1 = False
    stop = False
    for h in reverse(ctx.previous_translations):
        text = h.formatting[0].text
        if text != '' and type(text) != None and text != None:
            for t in text:
                if t in starting:
                    stop = True
        if stop:
            break
        if h.rtfcre[0] == 'kl':
            g1 = True
            break

    if cmdline in ending and word != '': # standing alone
        ret.text = ''

        strokes = []
        found = False
        for h in reverse(ctx.previous_translations):
            if h.strokes == []:
                break
            stroke = h.strokes[0].rtfcre
            text = h.formatting[0].text
            if text == None:
                break
            for letter in text:
                if letter.lower() in starting or letter == "\n":
                    found = True
            if found == True:
                break
            strokes.append(stroke)

        cap = False
        if len(strokes) > 0 and strokes[-1] == 'l':
            cap = True
            strokes = strokes[:-1]

        if previousText == 'gg':
            ret.prev_replace = 'gg'
            ret.text = '′'
            word = word[:-2]
            strokes = strokes[1:]
        if previousText == 'GG':
            ret.prev_replace = 'GG'
            ret.text = '′'
            ret.command = 'plover:toggle_dict:-caps.json'
            word = word[:-2]
            strokes = strokes[1:]
        if previousText == '“':
            ret.prev_replace = '“'
            ret.text = 'his'
            word = word[:-1]
            strokes = strokes[1:]
        if previousText == 'cc':
            ret.prev_replace = 'cc'
            ret.text = ':'
            word = word[:-2]
            strokes = strokes[1:]
        if previousText == 'CC':
            ret.prev_replace = 'CC'
            ret.text = ':'
            ret.command = 'plover:toggle_dict:-caps.json'
            word = word[:-2]
            strokes = strokes[1:]
        if previousText == 'bb':
            ret.prev_replace = 'bb'
            ret.text = ';'
            word = word[:-2]
            strokes = strokes[1:]
        if previousText == 'BB':
            ret.prev_replace = 'BB'
            ret.text = ';'
            ret.command = 'plover:toggle_dict:-caps.json'
            word = word[:-2]
            strokes = strokes[1:]
        if previousText == 'ea':
            ret.prev_replace = 'ea'
            ret.text = ','
            word = word[:-2]
            strokes = strokes[1:]
        if previousText == 'EA':
            ret.prev_replace = 'EA'
            ret.text = ','
            ret.command = 'plover:toggle_dict:-caps.json'
            word = word[:-2]
            strokes = strokes[1:]

        strokes = tr("/".join(strokes[::-1]))
        if strokes in contractionsStrokes and g1 == False:
            apos = ['\'d', '\'ll', '\'re', '\'s', '\'t', '\'ve']
            lastWord = ctx.copy_last_action().word
            if lastWord not in apos:
                replace = contractionsStrokes[strokes]
                ret.prev_replace = word + ret.prev_replace
                if cmdline in ['\\']:
                    ret.word = word + cmdline
                else:
                    ret.word = cmdline #expansion[0][1]
                if lastWord.isupper():
                    ret.text = replace.upper() + ret.text + cmdline
                elif cap == True:
                    ret.text = replace.capitalize() + ret.text + cmdline
                else:
                    ret.text = replace + ret.text + cmdline
                ret.word_is_finished = True
                return ff(ctx, ret)
            else:
                ret.word = '\'' + cmdline
                ret.text = ret.text + cmdline
                ret.word_is_sinished = True
                return ff(ctx, ret)
        else:
            if cmdline == '\'':
                ret.text = ret.text + cmdline
                ret.word = cmdline
                ret.word_is_finished = True
            else:
                ret.text = ret.text + cmdline
            return ff(ctx, ret)

    if cmdline in ['ound', 'ance', 'sion', 'less', 'ount', 'ence', 'ong', 'ful', 'tion', 'ness', 'ment', 'ity']:
        if previousText.isalpha():
            if word != '' and word[0] in starting:
                word = word[1:]
            ret.word = word + cmdline
            ret.text = cmdline
            return ff(ctx, ret)
        elif cmdline in ['ence', 'ong', 'ful', 'tion', 'ness', 'ment', 'ity']:
            letters = {
                    'ence': 'e',
                    'ong': 'g',
                    'ful': 'l', 
                    'tion': 'n',
                    'ness': 's',
                    'ment': 't',
                    'ity': 'y',
                    }
            if word == '' or word[0] in starting:
                word = letters[cmdline]
                ret.word = word
                ret.text = word
                return ff(ctx, ret)

    if cmdline == 'gg': # gg ' were
## '(s) (s)were(s) gg 
        if word == '':
            ret.text = 'were'
            return ff(ctx, ret)
        else:
            ret.text = 'gg'
            return ff(ctx, ret)

    if cmdline == '?': # ? " his
## ? (s)" (s)his(s)
        if word == '':
            ret.text = '“'
            ret.word = '“'
            return ff(ctx, ret)
        else:
            ret.text = "?"
            ret.word = "?"
            return ff(ctx, ret)

    if cmdline == 'cc': # cc con :
## :(s) cc (s)con
        if word == '':
            ret.text = "con"
            return ff(ctx, ret)
        else:
            ret.text = "cc"
            return ff(ctx, ret)

    if cmdline == 'CC': # cc con :
## :(s) cc (s)con
        if word == '':
            ret.text = "CON"
            return ff(ctx, ret)
        else:
            ret.text = "CC"
            return ff(ctx, ret)

    if cmdline == '.': # . (s)dis 
        if word == '':
            ret.text = "dis"
            return ff(ctx, ret)
        else:
            ret.text = "."
            return ff(ctx, ret)

    if cmdline == 'bb': # bb be ; 
## ;(s) (s)be bb 
        if word == '':
            ret.text = 'be'
            return ff(ctx, ret)
        else:
            ret.text = "bb"
            return ff(ctx, ret)

    if cmdline == 'BB': # bb be ; 
## ;(s) (s)be bb 
        if word == '':
            ret.text = 'BE'
            return ff(ctx, ret)
        else:
            ret.text = "BB"
            return ff(ctx, ret)

    if cmdline == 'was': # was "
## "(s) (s)was(s)
        if word == '':
            ret.text = 'was'
            return ff(ctx, ret)
        else:
            ret.text = '”'
            return ff(ctx, ret)

    if cmdline in ending:
        ret.text = cmdline
        ret.word = cmdline
        ret.word_is_finished = True
        return ff(ctx, ret)

    if cmdline == "\n":
        ret.text = "\n"
        ret.word = ''
        return ff(ctx, ret)

    if cmdline in modifiers:
        ret.text = ' ' + cmdline
        return ff(ctx, ret)

    past = ctx.copy_last_action()
    if past.word == None:
        word = ''
    else:
        word = past.word

    ret.text = cmdline
    ret.word = word + cmdline
    return ff(ctx, ret)

# stand alone is needs a SPACE before or after:
# `B.C.` - cannot expand B - because . exist after space
