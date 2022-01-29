import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    for c in s:
        if c not in digitmapping and c not in "qwertyuiopasdfghjklzxcvbnm":
            raise ValueError
        if c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
            crypted+=digitmapping[c]

    return crypted

def decode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    uncrypted = ""
    digitmapping = dict(zip('!"#€%&/()=1234567890', '1234567890!"#€%&/()='))
    if len(s) > 1000:
        raise ValueError
    for c in s:
        if c not in digitmapping and c not in "QWERTYUIOPASDFGHJKLZXCVBNM":
            raise ValueError
        if c.isalpha():
            if c.isupper():
                c=c.lower()
            # Rot13 the character for maximum security
            uncrypted+=codecs.decode(c,'rot13')
        elif c in digitmapping:
            uncrypted+=digitmapping[c]

    return uncrypted

