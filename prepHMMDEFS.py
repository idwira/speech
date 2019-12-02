dictionary = []
with open('monophones0') as f:
    for line in f.readlines():
        dictionary += [line[:-1]]

dictionary = list(set(dictionary))
dictionary.sort()

proto = ''
with open('template_proto.txt') as f:
    proto = f.read()

with open('hmmdefs', 'w') as f:
    for phone in dictionary:
        f.writelines('~h ' + phone + '\n' + proto)