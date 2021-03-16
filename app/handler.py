from functions import *


def handler(data):
    funcs = [fun for r in data['rule'] for fun in globals() if fun.endswith(r)]
    results = {}
    for i in data['data']:
        for func in funcs:
            i = globals()[func](i)
        results.setdefault('result', []).append(i)
    return results
