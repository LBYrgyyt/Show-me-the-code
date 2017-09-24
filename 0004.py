#纯英文文本词频统计

def multiple_replace(file):
    file.replace("'",' ')
    file.replace(".",' ')
    file.replace("\n",' ')
    file.replace(",",' ')
    file.replace("?",' ')
    return file

dic = {}
s = set()

with open("D:\EN.txt",'r') as f:
    F = f.read()
    file = multiple_replace(F).split(' ')
    for fi in file:
        s.add(fi)
    dic = dict.fromkeys(s,0)
    for i in file:
        dic[i] +=1
    #print(sorted(dic.values(),reverse=True))
    for i in dic:
        print(i+":"+str(dic[i]))
