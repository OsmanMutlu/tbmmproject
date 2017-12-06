# -*- coding: utf-8 -*-
import nltk
import json
import pandas as pd
import codecs
import re

keyword = 'yardım'
interested_words = ['sosyal','vakfı','vakıf','yoksul','muhtaç']
negative_words = ['hükümet','afganistan','bosna','yardımcı']
data = []
#stopwords = []
	
with codecs.open('items.jl', encoding="utf-8") as f:
	for line in f:
		data.append(json.loads(line))

# with codecs.open('stopwords', encoding="utf-8") as f:
	# for line in f:
		# stopwords.append(line)

#stopwords = [word.replace("\r\n","") for word in stopwords]

#nltk'nin word_tokenize fonksiyonu için 'punkt' paketi gerekli, eğer sizde mevcut değilse bir sonraki satırı uncomment edin.
#nltk.download('punkt')

tokenized_sentences = [nltk.word_tokenize(x['name']) for x in data]

# for tokenlist in tokenized_sentences:
	# for token in tokenlist:
		# if any(token==word for word in stopwords):
			# del token

for i, tokenlist in enumerate(tokenized_sentences):
	weight = 0
	for j, text in enumerate(tokenlist):
		if any(re.match(word, text, re.IGNORECASE) != None for word in negative_words):
			continue
		elif re.match(keyword, text, re.IGNORECASE) != None:
			weight += 10
		elif any(re.match(word, text, re.IGNORECASE) != None for word in interested_words):
			if j != len(tokenlist)-1 and re.match(keyword, tokenlist[j+1], re.IGNORECASE) != None:
				weight += 10
			else:
				weight += 2
	data[i]['weight'] = weight

sorted_data = pd.DataFrame(data).sort_values(by='weight', ascending=False)
with codecs.open('results.jl', 'w', encoding='utf-8') as file:
	sorted_data.to_json(file, orient='records', lines=True, force_ascii=False)

# Html çok çirkin, style'la uğraşmak lazım
# with codecs.open('results.html', 'w', encoding='utf-8') as file:
	# sorted_data.to_html(file,index=False)
