import matplotlib.pyplot as plt
import wikipedia
from wordcloud import WordCloud, STOPWORDS

text = wikipedia.page('korea').content + wikipedia.page('Japan').content
s_word = STOPWORDS.union({'south', 'north', 'korean', 'world', 'country', 'one'})
wordcloud1 = WordCloud(width=1280, height=720, stopwords=s_word).generate(text)
plt.figure(figsize=(20, 10))
plt.imshow(wordcloud1)
plt.show()
