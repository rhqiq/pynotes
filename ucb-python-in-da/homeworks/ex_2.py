from numpy import random, allclose

A = {'key1': '1', 'key2': '', 'key3': '', 'key4': '', 'key5': '', 'key6': ''}


def rand_val(d):
    for key in d:
        d[key] = random.randint(0, 10)

    return d

B = rand_val(A)


def map_elem(d):
    for key, value in d.items():
        if value < 5:
            d[key] = value * value

    return d

C = map_elem(B)

C['key1'] = C.pop('key6')

C['key1'] = C['key5']
del C['key5']

print(A)
print(B)
print(C)

print(A == B == C)
