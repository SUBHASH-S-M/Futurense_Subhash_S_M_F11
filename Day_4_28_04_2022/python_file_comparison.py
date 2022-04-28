file1 = open('document_1.txt', 'r')
file2=open('document_2.txt', 'r')
# This will print every line one by one in the file


def return_content(doc):
    contents_in_file= []
    for each_line in doc:
        #var=each_line.strip().split()

        if(len(each_line)>0):
            each_line=each_line.strip()
            #print(each_line, len(each_line))
            contents_in_file.append(each_line.strip())
    return contents_in_file
doc1=[]#line_num,extra_words,not present
doc2=[]
f1=return_content(file1)
f2=return_content(file2)
for i in range(min(len(f1),len(f2))):
    word1=set(f1[i].split(" "))
    word2=set(f2[i].split(" "))
    doc1.append([i+1,word1.difference(word2)])
    doc2.append([i+1,word2.difference(word1)])

if(len(f1)!=len(f2)):
    if(len(f1)>len(f2)):
        doc1.append([len(f1),''])
        doc2.append([len(f1), f1[len(f1) - 1]])
    else:
        doc1.append([len(f2),f2[len(f2)-1]])
        doc2.append([len(f2), set()])

prompt="Nothing is misisng from this file for this line"
temp=[]
for i in range(len(doc1)):
    val=[]
    line_number=doc1[i][0]
    word_1=doc1[i][1]
    word_2=doc2[i][1]
    #print(word_1,len(word_1),word_2,len(word_2))
    if(len(word_1) == 0 and len(word_2)==0):
        val.extend([line_number,"Both are same","Both are same"])
        #print(line_number,1)
    elif (len(word_1) == 0):
        val.extend([line_number, prompt,word_2])
        #print(line_number, 2)

    elif(len(word_2)==0):
        val.extend([line_number,word_1,prompt])
        #print(line_number, 3)
    else:
        x="".join(list(word_2))
        val.extend([line_number,"".join(list(word_1)),x])
        #print(line_number, 4)
    temp.append(val)
line_no=[]
flist1=[]
flist2=[]
for i in range(len(temp)):
    line_no.append(temp[i][0])
    flist2.append(temp[i][2])
    flist1.append(temp[i][1])


# Import pandas package
import pandas as pd

# Define a dictionary containing employee data
data = {'Line_number':line_no,
        'File Number 1':flist1,
        'FIle Number 2':flist2}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
print(df)
df.to_csv('file_comparison.csv')














