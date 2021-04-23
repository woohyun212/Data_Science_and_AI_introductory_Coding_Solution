import matplotlib.pyplot as plt
import wikipedia
from wordcloud import WordCloud, STOPWORDS

wiki = wikipedia.page('MachineLearning')  # wikipedia.page('Python (programming language)')
text = wiki.content
s_word = STOPWORDS.union({'one', 'using', 'first', 'two', 'make', 'use'})
wordcloud1 = WordCloud(width=1280, height=720, stopwords=s_word).generate(text)
plt.figure(figsize=(20, 10))
plt.imshow(wordcloud1)
plt.show()
