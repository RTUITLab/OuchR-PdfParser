#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
from nltk import *
from nltk.corpus import brown
stopwords= nltk.corpus.stopwords.words('russian')
file = open('NLTK.txt', 'r', encoding='utf-8')
read_file = file.read()
docs = nltk.sent_tokenize(read_file)
stem='russian'
#'danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian',
#'norwegian', 'porter', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish'