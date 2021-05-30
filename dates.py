import parsedatetime
p = parsedatetime.Calendar()

with open('NLTK.txt', 'r', encoding='utf-8') as fp:
    city_data = fp.read()


print(p.parse(city_data))
