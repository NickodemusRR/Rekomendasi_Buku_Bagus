import numpy as np 
import pandas as pd 
import random

books = pd.read_csv('books.csv')
ratings = pd.read_csv('ratings.csv')

# print(books.head(2))
# print(ratings.head(2))

# print(books.info())

# get column with type object
features = books[['authors', 'original_title', 'title', 'language_code']]
features = features.fillna('None')
features['all'] = features['authors'] + ' ' + features['original_title'] + ' ' + features['title'] + ' ' + features['language_code']

# print(features.isnull().sum())

from sklearn.feature_extraction.text import CountVectorizer
model = CountVectorizer()
model = CountVectorizer(tokenizer=lambda x: x.split(' '))
matrixFeature = model.fit_transform(features['all'])

features = model.get_feature_names()
numFeatures = len(features)
# print(numFeatures)

from sklearn.metrics.pairwise import cosine_similarity
score = cosine_similarity(matrixFeature)

# Asumsi buku dengan bintang 5 adalah buku yang paling disukai user

# ===== Andi =======
indexAndi = books[books['original_title'] == 'The Hunger Games'].index.values[0]
# print(indexAndi)

daftarScoreA = list(enumerate(score[indexAndi]))
# print(daftarScore)

sortDaftarScoreA = sorted(
    daftarScoreA,
    key = lambda j: j[1],
    reverse = True
)
# print(sortDaftarScore[1:6])

similarBooksA = []
for i in sortDaftarScoreA:
    if i[1] > 0.5:
        similarBooksA.append(i)
# print(similarBooks[1:6])

recommendA = random.choices(similarBooksA, k=5)

print('1. Buku bagus untuk Andi:')
for i in recommendA:
    print('-',
        books.iloc[i[0]]['title'],
        )

# ===== Budi =======
indexBudi = books[books['original_title'] == 'Harry Potter and the Philosopher\'s Stone'].index.values[0]
daftarScoreB = list(enumerate(score[indexBudi]))
sortDaftarScoreB = sorted(
    daftarScoreB,
    key = lambda j: j[1],
    reverse = True
)
similarBooksB = []
for i in sortDaftarScoreB:
    if i[1] > 0.5:
        similarBooksB.append(i)
recommendB = random.choices(similarBooksB, k=5)

print('2. Buku bagus untuk Budi:')
for i in recommendB:
    print('-',
        books.iloc[i[0]]['title'],
        )

# ===== Ciko =======
indexCiko = books[books['original_title'] == 'Robots and Empire'].index.values[0]
daftarScoreC = list(enumerate(score[indexCiko]))
sortDaftarScoreC = sorted(
    daftarScoreC,
    key = lambda j: j[1],
    reverse = True
)
similarBooksC = []
for i in sortDaftarScoreC:
    if i[1] > 0.5:
        similarBooksC.append(i)
recommendC = random.choices(similarBooksC, k=5)

print('3. Buku bagus untuk Ciko:')
for i in recommendC:
    print('-',
        books.iloc[i[0]]['title'],
        )

# ===== Dedi =======
indexDedi = books[books['original_title'] == 'A History of God: The 4,000-Year Quest of Judaism, Christianity, and Islam'].index.values[0]
daftarScoreD = list(enumerate(score[indexDedi]))
sortDaftarScoreD = sorted(
    daftarScoreD,
    key = lambda j: j[1],
    reverse = True
)
similarBooksD = []
for i in sortDaftarScoreD:
    if i[1] > 0.5:
        similarBooksD.append(i)
recommendD = random.choices(similarBooksD, k=5)

print('4. Buku bagus untuk Dedi:')
for i in recommendD:
    print('-',
        books.iloc[i[0]]['title'],
        )

# ===== Ello =======
indexEllo = books[books['original_title'] == 'The Story of Doctor Dolittle'].index.values[0]
daftarScoreE = list(enumerate(score[indexEllo]))
sortDaftarScoreE = sorted(
    daftarScoreE,
    key = lambda j: j[1],
    reverse = True
)
similarBooksE = []
for i in sortDaftarScoreE:
    if i[1] > 0.5:
        similarBooksE.append(i)
recommendE = random.choices(similarBooksE, k=5)

print('5. Buku bagus untuk Ello:')
for i in recommendE:
    print('-',
        books.iloc[i[0]]['title'],
        )