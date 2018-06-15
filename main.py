
from cc_markov import MarkovChain
from fetch_data import fetch_data


url='http://songmeanings.com/songs/view/3530822107859540342/'
text=fetch_data(url)
MarkovChain.add_string(text)
result=MarkovChain.generate_text()
print(result)