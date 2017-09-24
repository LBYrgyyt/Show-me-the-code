import re,collections  
def get_words(file):  
    with open (file) as f:  
        words_box=[]  
        for line in f:                           
            if re.match(r'[a-zA-Z0-9]*',line):#避免中文影响  
                words_box.extend(line.strip().split())                 
    return collections.Counter(words_box)

print(get_words("D:\EN.txt"))
