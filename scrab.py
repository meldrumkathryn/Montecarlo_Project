import pandas as pd
wordsdf = pd.read_csv('sgb-words.txt', header = None)
scrab_words_5l = list(wordsdf[0].values)