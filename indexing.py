#-------------------------------------------------------------------------
# AUTHOR: Jonathan Lee
# FILENAME: indexing.py
# SPECIFICATION: Read "collection.csv" output tf-idf
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {"I", "and", "She", "her", "They", "their"} #Pronouns and Conjunctions
for word in stopWords:
    for i in range(len(documents)):                     #Currently three strings in documents
        documents[i] = documents[i].replace(word, "")   #Remove instances of stopWords in documents

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
steeming = {"cats", "dogs","loves"}                     #Without NLTK library, I assume that we are to manually stem the words
for stem in steeming:
    for i in range(len(documents)):
        documents[i] = documents[i].replace("s", "")

#Identifying the index terms.
#--> add your Python code here
terms = []
for i in range(len(documents)):
    terms += documents[i].split()

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []
for i in range(3):
    row = []
    for j in range(1):
           count = documents[i].count("cat")
           row.append(count)
           count = documents[i].count("dog")
           row.append(count)
           count = documents[i].count("love")
           row.append(count)
           docTermMatrix.append(row)

tf = []

for i in range(len(docTermMatrix[0])):
    sum = 0
    for j in range(len(docTermMatrix[0])):
        sum += docTermMatrix[i][j]

    for k in range(len(docTermMatrix)):
        temp = docTermMatrix[i][k]/sum
        tf.append(temp)
    
idf = []

cat = 0
dog = 0
love = 0
for i in range(len(docTermMatrix[0])):
    cat += docTermMatrix[i][0]
    dog += docTermMatrix[i][1]
    love += docTermMatrix[i][2]


    

#Printing the document-term matrix.
#--> add your Python code here

