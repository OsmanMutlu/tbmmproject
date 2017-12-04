import nltk
import json

keyword = 'yardım'
interested_words = ['sosyal','vakfı','vakıf','yoksul','muhtaç']
negative_words = ['hükümet','afganistan','bosna','yardımcı']
data = []
	
with open('items.jl') as f:
    for line in f:
        data.append(json.loads(line))

tk = [nltk.word_tokenize(x['name']) for x in data]
for i in range(0,len(tk)-1):
	weight = 0
	for x in range(0,len(tk[i])-1):
		text = tk[i][x]
		text = text.lower()
		if any(word in text for word in negative_words):
			continue
		elif text.find(keyword) != -1:
			weight += 10
		elif any(word in text for word in interested_words):
			tk[i][x+1] = tk[i][x+1].lower()
			if (x != len(tk[i])-1) and (tk[i][x+1].find(keyword) != -1):
				weight += 10
			else:
				weight += 2
	data[i]['weight'] = weight
	
file = open('items2.jl', 'w')
for x in data:
	line = json.dumps(x,ensure_ascii=False) + "\n"
	file.write(line)
