from nltk.corpus import stopwords

print(stopwords.words('english'))

with open('passage.txt', 'r') as file:

    passage = file.read()
    a = passage.split()
    f = [x for x in a if x not in stopwords.words('english')]
    print(' '.join(f))