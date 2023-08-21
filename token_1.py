import nltk 
texto = "40. Work accidents involving exposure to contaminated biological materials, such as blood and body fluids, are frequent among health care professionals as a function of the peculiar characteristics of the procedures they perform while delivering care to patients and the working conditions under which they perform their work."
token = nltk.word_tokenize(texto, language="english")

#tirar símbolos
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
Tokens = tokenizer.tokenize(texto)

#tirar símbolos e numerais
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'[A-z]\w*')
tokens = tokenizer.tokenize(texto)

#frequência sem distinção de maiúsculo e minúsculo
frequencia = nltk.FreqDist(w.lower() for w in tokens)
a = frequencia.most_common()


#quantidade de tokens
print(len(token))

#quandidade de símbolos 
print(len(token)-len(Tokens))

#quandidade de símbolos e numerais
print(len(token)-len(tokens))

#palavra mais frequente
print(a[0][0])
