import os
print('current working directory is', os.getcwd())

print('current working directory is', os.getcwd())

with open('passage.txt', 'r') as file:
    passage = file.read()

    a=passage.split()

    # Write your code here
    # You should save processed text into a variable called passage_without_stop_words

    # Helpful functions:
    f=[]
    f.append(x for x in a if x not in ['The','is','at','and','or','but','a'])

