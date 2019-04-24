
import hashlib


def str_repr(d):
    s = ''
    for k in sorted(list(d.keys())):
        if type(d[k]) is dict:
            s += '' + str(k) + ': {' + str_repr(d[k]) + '}, '
        else:
            s += '' + str(k) + ': ' + str(d[k]) + ', '
    return s


def hash_dict(config, limit_chars=16):
    hash_object = hashlib.sha256(str_repr(config).encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig[:limit_chars]