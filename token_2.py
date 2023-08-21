import tokenize
import nltk
from nltk.tokenize import RegexpTokenizer
poem = "40. Work accidents involving exposure to contaminated biological materials, such as blood and body fluids, are frequent among health care professionals as a function of the peculiar characteristics of the procedures they perform while delivering care to patients and the working conditions under which they perform their work."

# Passando o padrao (pattern) -> desconsidera espaço
tokenizer = RegexpTokenizer(r'\w+')

# Esta fazendo split e separando o poem
token = tokenizer.tokenize(poem)

# Sao os stopwords
stopwords = nltk.corpus.stopwords.words('english')

# Tira os stopwords baseado na variavel token
tokenSemStopWord = [w.lower() for w in token if w not in stopwords]

# Freq recebe as tuplas (palavra, vezes) e ordenamento recebe as tuplas mais frequentes em ordem
freq = nltk.FreqDist(tokenSemStopWord)
ordenamento = freq.most_common()

#classe gramatical
U = nltk.pos_tag(token)

#quantidade de classes gramaticais
i=0
O=[]
for i in range(len(U)):
    O.append(U[i][-1])
    i=i+1
FREQ = nltk.FreqDist(O)
ORDEM = FREQ.most_common()
print(ORDEM)
