from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np


def wc(string):
    maskarr = np.array(Image.open("wc1.png"))
    cloud = WordCloud(background_color="white", max_words=50, mask=maskarr, stopwords=set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("wc1.png")


data = open("ques.txt").read()
data = data.lower()
wc(data)
