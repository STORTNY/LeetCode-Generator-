def leet_encode(msg):
    leet_dict = {
        'a': ['4', '@', '^','aye','q','	ɐ'],
        'b': ['8', '6','13','|3','P>','|:','!3','(3','/3',')3','ꞛ'],
        'c': ['(', '<', '{', '[','Ⓒ'],
        'd': ['|)','[)','I>'],
        'e': ['3', '&', '€'],
        'f': ['|=', '|#', '/='],
        'g': ['9', '6', '&','C-','(y,'],
        'h': ['#', '4', '|-|'],
        'i': ['1', '|', '!'],
        'j': ['_|', '_/', '</',';'],
        'k': ['X', '|<', '|{'],
        'l': ['1', '|', '7'],
        'm': ['|v|','[V]','|\/|','(u)','(v)','^^'],
        'n': ['^/','|v', '</>','{\}'],
        'o': ['0', '8', '*','()','¤'],
        'p': ['|*', '|°', '|"','|7'],
        'q': ['(_,)', '()_', '0_','0.'],
        'r': ['2', '|?', '|z','12','ᴚ','ꓤ','ɹ'],
        's': ['$', '5', 'z'],
        't': ['7', '+', '†'],
        'z': ['2', '5', '7']
    }

    def leet(current_str, rem_chars):
        if not rem_chars:
            return [current_str]

        char = rem_chars[0]
        rest_chars = rem_chars[1:]

        if char.lower() in leet_dict:
            leeted = []
            for leet_variant in leet_dict[char.lower()]:
                leeted.extend(leet(current_str + leet_variant, rest_chars))
            return leeted
        else:
            return leet(current_str + char, rest_chars)

    return leet("", msg)


msging = input("msg= ")

res = leet_encode(msging)

print(res)
