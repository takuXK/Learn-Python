from collections import Counter
def main():
    txt = GetTxt('hamlet.txt')
    txtlist = DealTxt(txt)
    summarize = CountTxt(txtlist)
    total = SortTxt(summarize)
    PrintTxt(total)

def GetTxt(filename):
    f = open(filename,'rt',encoding='utf-8')
    txt = f.read()
    f.close()
    return txt

def DealTxt(txt):
    txt = txt.lower()
    notation = '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~'
    for char in txt:
        if char in notation:
            txt.replace(char,' ')
    txtlist = txt.split()
    return txtlist

def CountTxt(txtlist):
    summarize = {}
    for word in txtlist:
        summarize[word] = summarize.get(word,0) + 1
    ####或者使用：####
    #sortls = Counter(txtlist).most_common(10)  此时返回元组数组
    #summarize = {x[0]:x[1] for x in sortls}
    return summarize

def SortTxt(summarize):
    total = list(summarize.items())
    total.sort(key=lambda x:x[1],reverse=True)
    return total

def PrintTxt(total):
    for element in total:
        print('{0:<10}{1:>10}'.format(element[0],element[1]))

main()