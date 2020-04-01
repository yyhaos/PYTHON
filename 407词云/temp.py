# -*- coding: utf-8 -*-
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
text2 = open('aa1.txt','rb')
text = text2.read()
print text
# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open(path.join(d, "407.png")))
import jieba
stopwords = set(STOPWORDS)
stopwords.add("said")
#print text
word_list = [" ".join(jieba.cut(text))]
text = ' '.join(word_list)
print text

wc = WordCloud(font_path='./font/simhei.ttf',width=1500,height=430,background_color="white",max_font_size=100, max_words=2000, mask=alice_mask,
stopwords=stopwords,)
wc.generate(text)

# store to file
wc.to_file(path.join(d, "Alice.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()