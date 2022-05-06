import re
var="dhoni is the best batsman"
data=re.match('dhoni',var)

print(data) # returns object <re.Match object; span=(0, 5), match='dhoni'>
print(data.group())  # returns the match :dhoni
print(data.span()) #index of the start and end of the match (0, 5)
print(data.start())#start position :0
print(data.end())#end position :5
print()
#match donent check the word in middle
string_inp="dhoni the best"
data=re.match('the',string_inp)
#print(data.group()) throws error

#search method is is used to search in between also
string_inp="dhoni is  the best"
data=re.search('the',string_inp)
print(data.group())  # gives the output : the
data1=re.search('Is',string_inp,re.I) #to make the search case in-sensitive we use the flag re.I(ignore)
print(data1.group())  # gives the output : is

#if the data is present on multiple lines first occurence is considered
string_inp="dhoni is dhoni the best among all"
data=re.search('dhoni',string_inp)
print(data.span())  #(0, 5)return the 1st occur of dhoni

#re.m
re.search(".*?",var)  #? quesition mark based aprroch to restrict greediness

#re.findall()
import re



var = """dhoni is better than Kohli
dhoni they both play for India
dhoni is senior"""
data = re.search("dhoni",var)
print(data)
print(data.group())
print(data.span())
print(data.start())
print(data.end())

var = """dhoni is better than Kohli
dhoni they both play for India
dhoni is senior"""
data = re.search("dhoni",var,re.M)
print(data)
print(data.group())
print(data.span())
print(data.start())
print(data.end())

var = "<html><body><head></head>"
data = re.search("<.*",var)
print(data.group())

var = "<html><body><head></head>"
data = re.search("<.*?",var)
print(data.group())

var = """dhoni is better than Kohli"""
data = re.search("(.*) is (.*)",var)
print(data.group())
print(data.group(1))
print(data.group(2))


# var = """dhoni is better than Kohli"""
data = re.search("(.*) is (.*?) (.*)",var)
print(data.group())
print(data.group(1))
print(data.group(2))
print(data.group(3))

var1 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
data = re.findall("\d{3}",var1)
print(data)

var2 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
data = re.findall("\d{1,3}",var2)
print(data)

var3 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
data = re.findall("\D{1,3}",var3)
print(data)

var4 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
data = re.findall("\w",var4)
print(data)
s
var5 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
data = re.findall("\w*",var5)
print(data)

var6 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
data = re.findall("\w+",var6)
print(data)

var7 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
data = re.findall("\W*",var7)
print(data)
#
var8 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
data = re.findall("\s{1,3}",var8)
print(data)

var9 = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
data = re.findall("\W",var9)
print(data)

var = "DHONI scored 183 against SRIlankas @20009 with 7,5 Avg per over"
data = re.findall("\S{1,4}",var)
print(data)




