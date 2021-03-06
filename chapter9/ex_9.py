import matplotlib.pyplot as plt
import wikipedia
from wordcloud import WordCloud, STOPWORDS

wiki = wikipedia.page('korea')
text = wiki.content
s_word = STOPWORDS.union({'south', 'north', 'korean', 'world', 'country'})
wordcloud1 = WordCloud(width=1280, height=720, stopwords=s_word).generate(text)
plt.figure(figsize=(20, 10))
plt.imshow(wordcloud1)
plt.show()
