#immutability


#docstring

#escape sequence


#raw_data
location="c:\newfolder\testing.txt"
print(location) #gives diff input as it interpretes the \n and \t
location=r"c:\newfolder\testing.txt" # r-->means raw data so it ignores escape sequence
print(location)

#shallow vs deep copy

var=[1,2,4,5]
var1=var
var1[0]=100
print(var)    # the content of the orginal list also affected due to shallow copy

var=[1,2,3,4,5]
# diff methods of deep copy or cloning the files
var1=var[:]
var2=var.copy()
#var3=var.deepcopy()
print(var1,var2) # object got clonned

#count function with index filter(index,find,index,rfind)
#"rfind--> find the occurence  of the specified letter from reverse"
string_input="India is rich in its wealth"
print(string_input)
#index throws error if input not found whereas find return -1
print(string_input.find("i",1,4))  #1--> start index,4-1=3--> ending index 4 is not included
print(string_input.rfind("i"))  # return 17

#parrtition vs split vs list(str) in conversion from string to list
string_input="India is rich coutry"
print(list(string_input))#['I', 'n', 'd', 'i', 'a', ' ', 'i', 's', ' ', 'r', 'i', 'c', 'h', ' ', 'c', 'o', 'u', 't', 'r', 'y']
print(string_input.split()) #['India', 'is', 'rich', 'coutry']
print(string_input.split("i"))#['Ind', 'a ', 's r', 'ch coutry'] doesnt include the "i"
print(string_input.partition("i"))# return tuple and includes "i" ('Ind', 'i', 'a is rich coutry')

#strip used tp remove char from both the ends
#works sequnecly
var="!!india is the countri!!"
val=var.strip("!")
print(val) #India is the countri
print(var.strip("!i"))  #ndia is the countr # first removes ! from both ends then removes i form both ends ndia is the countr
print(var.rstrip("!"))#!!india is the countri
print(var.lstrip("!"))#india is the countri!!

#enumerate and removing the letter
l=['a','b','c','d','e','f']
for index,ele in enumerate(l[:]):  #good conversion to use these kind of operations on same list
    print(index,ele)
l=['a','b','c','d','e','f']
for index,ele in enumerate(l):  #each tym the loop starts and list expands
    if(index%2==0):
        x=l.pop(index)
        print(l,x)
#list expands and  recurssion
var=["a","b","c"]
for i in var:
    var.append(i.upper())
# list keeps on expanding and the for loop detects the new changes
# appending on the same list is not adviced


