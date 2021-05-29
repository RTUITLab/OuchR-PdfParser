import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import json
import difflib

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

    for word in word_list:
        sum = 0
        for ww in sentens:
            sum += similarity(word, ww)
            arr[word] = sum

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

    read_file = read_file.replace("&nbsp", "\n")
    text = nltk.word_tokenize(read_file)

    wordsFiltered = []

    for w in text:
        if w not in stopWords:
            wordsFiltered.append(w)

    cit = find_country(wordsFiltered,["Ангарск","Балаково","Владимир","Волгодонск","Глазов","Димитровград","Екатеринбург","Зеленогорск","Казань","Ковров","Москва","Мурманск","Нижний Новгород","Новосибирск","Новоуральск","Подольск","Ростов-на-Дону","Санкт-Петербург","Саров","Северск","Томск","Уфа","Электросталь","Вся Россия"])
    #print("Testt",len(text),text)
    with open('city.json', 'r', encoding='utf-8') as fp:
        city_data = fp.read()
        data = json.loads(city_data)

    for i in data:
        if cit == i['city']:
            #print(i['topics'])
            topics = i['topics']

    arr = {}
    for num,i in enumerate(topics,start=0):
        # print(line_numbers(read_file, i['skills']))
        arr[str(num)] = line_numbers(read_file, i['skills'])
    arr = sort(arr)
    # print(arr[-1])

    data_json = "["
    for i in range(len(arr)):
        data_json += str(topics[int(arr[len(arr)-i-1][0])])+','
    # data = [topics[int(arr[-1][0])],topics[int(arr[-1][0])],topics[int(arr[-1][0])],topics[int(arr[-1][0])]]
    data_json = data_json[0:-1]+']'
    return data_json

def sort(d):
    list_d = list(d.items())
    list_d.sort(key=lambda i: i[1])
    return list_d


ff = "NLTK.txt"
with open(ff, 'r', encoding='utf-8') as fh:
    tex = fh.read()
    getIntUrl(tex)