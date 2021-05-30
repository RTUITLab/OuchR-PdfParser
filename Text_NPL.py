import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import json
import difflib
import semantic
import re

def similarity(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    if matcher.ratio() > 0:
        # print(s1,s2,matcher.ratio())
        return (matcher.ratio() / (len(s1)*len(s2)))
    return 0.0

def line_numbers(sentens, word_list):
    sum = 0
    arr = {}
    test = 0
    word_list = ' '.join(word_list)
    for ww in sentens:
        sum += similarity(word_list, ww)
        arr[word_list] = sum

    for i in arr.values():
        test += i
    test = test/len(arr)

    return test

def find_country(file, word_list):
    results = {word:[] for word in word_list}
    for num, line in enumerate(file, start=1):
        for word in word_list:
            if word in line:
                return word
    return "Вся Россия"


def init():
    nltk.download('punkt')
    nltk.download("stopwords")


def getIntUrl(text):
    stopWords = set(stopwords.words("russian"))
    read_file = text
    text = nltk.word_tokenize(read_file)
    clastered_text = " ".join(semantic.main(read_file))

    wordsFiltered = []

    for w in text:
        if w not in stopWords:
            wordsFiltered.append(w)

    cit = find_country(clastered_text,["Ангарск","Москва","Вся Россия"])
    #print("Testt",len(text),text)
    with open('city.json', 'r', encoding='utf-8') as fp:
        city_data = fp.read()
        data = json.loads(city_data)

    for i in data:
        if cit == i['city']:
            #print(i['topics'])
            topics = i['topics']

    comp = clastered_text.split('Навыки')[1]
    for i in topics:
        i['Competencies'] = re.sub(r'\s+', ' ', comp)

    arr = {}
    for num,i in enumerate(topics,start=0):
        # print(line_numbers(read_file, i['skills']))
        arr[str(num)] = line_numbers(clastered_text, i['skills'])
    arr = sort(arr)
    # print(arr[-1])
    data_json = []
    for i in range(len(arr)):
        data_json.append(topics[int(arr[len(arr)-i-1][0])])
    return data_json

def sort(d):
    list_d = list(d.items())
    list_d.sort(key=lambda i: i[1])
    return list_d

# ff = "NLTK.txt"
# with open(ff, 'r', encoding='utf-8') as fh:
#     tex = fh.read()
#     print(getIntUrl(tex))