newfile = open('hmmdefsnew','w+')
with open("proto") as fproto:
    proto = fproto.read()
print(proto)
with open('../monophones0', 'r') as f:
    for file in f:
        if("#" not in file and "\"" not in file):
            newfile.write("~h \"" + file[:-1] +"\"\n" + proto+"\n")
newfile.close()

