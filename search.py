import nltk
import pandas

keyword = 'yardım'
interested_words = ['sosyal','vakfı','vakıf','yoksul','muhtaç']
negative_words = ['hükümet','afganistan','bosna']
weights = []

df = pandas.read_json("items.jl", lines = True)

tk = [nltk.word_tokenize(x) for x in df['name']]
df['tokenized'] = pandas.Series(tk)

for item in df['tokenized']:
	weight = 0
	for i in range(0,len(item)):
		item[i] = item[i].lower()
		if item[i].find(keyword) != -1:
			weight += 10
		elif any(word in item[i] for word in interested_words):
			weight += 4
		elif any(word in item[i] for word in negative_words):
			weight -= 4
	weights.append(weight)

df['weight'] = pandas.Series(weights)
df = df.sort_values('weight', ascending=False)
print(df)