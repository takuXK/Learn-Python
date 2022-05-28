import jieba
from wordcloud import WordCloud
txt1 = '程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，它按照' 
txt2 = '特定规则组织计算机指令，使计算机能够自动进行各种运算处理。'
txt = txt1 + txt2
word = jieba.lcut(txt)
newtxt = ' '.join(word)
wordcloud = WordCloud(font_path="msyh.ttc").generate(newtxt)
wordcloud.to_file('词云中文例子图.png')