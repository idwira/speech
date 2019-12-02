newfile = open('hmmdefsnew','w+')
with open("protobaru.txt") as fproto:
    proto = fproto.read()
print(proto)
with open('hmmdefs', 'r') as f:
    for file in f:
        if("#" not in file and "\"" not in file):
            newfile.write("~h \"" + file[:-1] +"\"\n" + proto+"\n")
newfile.close()

