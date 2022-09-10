from string import punctuation


with open('./data/stdin.txt', 'r', encoding='utf-8') as f:
    data = f.read()


punctuation = punctuation + '«—»'
# Замена не алфавита на пробел
for i in punctuation:
    if i in data:
        data = data.replace(i, ' ')

data = data.lower().split()

# Построение словаря, где ключ - текущее слово, а значение словарь со словами идущими после текущего слова
# в качестве ключа и количеством повторений в качестве значения. Пригодится для вычисления вероятности в generate.py

dict_of_words = {data[-2]:{data[-1]: 1}}
for i in range(len(data) - 1):
    if data[i] not in dict_of_words.keys():
        dict_of_words[data[i]] = {data[i+1]: 1}
    elif data[i+1] not in dict_of_words[data[i]].keys():
        dict_of_words[data[i]][data[i+1]] = 1
    else:
        dict_of_words[data[i]][data[i+1]] += 1