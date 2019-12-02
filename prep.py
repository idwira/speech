dictionary = []
with open('dict.lexs') as f:
    for line in f.readlines():
        for phone in line.split()[1:]:
            dictionary += [phone]
        continue

dictionary = list(set(dictionary))
dictionary.sort()

proto = ''
with open('proto') as f:
    proto = f.read()

with open('monophones0', 'w') as f:
    for phone in dictionary:
        f.writelines(phone + '\n')