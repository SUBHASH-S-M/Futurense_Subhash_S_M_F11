import pandas as pd
with open("document_1.txt","r") as file1:
    l1=file1.readlines()
with open("document_2.txt","r") as file2:
    l2=file2.readlines()
f1_list=[]
f1=[]
f2=[]
f2_list=[]
for word in range(len(l1)):
    q=l1[word]
    f1.append(q)
for word in range(len(l2)):
    q=l2[word]
    f2.append(q)
ll=[]
words1=[]
words2=[]
mismatch1=[]
mismatch2=[]
lineno=[]
for i in range (len(f2)):
    z=f2[i]
    z=z.split()
    words1.extend(z)
    y=f1[i]
    y=y.split()
    words2.extend(y)
    print(words1)
    print(words2)
    for j in range(len(words1)):
        if(len(words1)==len(words2)):
            if words1[j]!=words2[j]:
                mismatch1.append(words1[j])
                mismatch2.append(words2[j])
                lineno.append(i+1)

        else:
            print("total number of words is different")

    words1=[]
    words2=[]

df = pd.DataFrame(list(zip(mismatch1, mismatch2,lineno)),
               columns =['word_in_1st_file', 'word_in_2st_file','lineno'])
print(df)
df.to_csv(r'final1.txt', header=None, index=None, sep='\t', mode='a')