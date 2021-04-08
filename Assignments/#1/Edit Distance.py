import copy

# A Naive recursive Python program to fin minimum number
# operations to convert str1 to str2
 
 
def editDistance(str1, str2, m, n):
 
    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m == 0:
        return n
 
    # If second string is empty, the only option is to
    # remove all characters of first string
    if n == 0:
        return m
 
    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)
 
    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert
                   editDistance(str1, str2, m-1, n),    # Remove
                   editDistance(str1, str2, m-1, n-1)    # Replace
                   )
def third_min(word):
  for i in range(3):
    f_min=min(word)
    get.append(f_min)  
    while f_min in word: word.remove(f_min)
    

# Driver code
list1 = []
index =[]
get = []
count =0
str1 = input("Enter a word: ")
str2 =["abandon",
"beautiful",
"cancer",
"decline",
"earnings",
"fade",
"garlic",
"headquarters",
"imagination",
"Jewish",
"knee",
"laboratory",
"magazine",
"necessary",
"occupy",
"passage",
"question",
"range",
"scientist",
"taxpayer",
"uniform",
"veteran",
"wander",
"youth",
"zone"] 
for s in str2:
    #print(editDistance(str1, s, len(str1), len(s)))
    list1.append(editDistance(str1, s, len(str1), len(s)))
#Deep copy
list2=copy.deepcopy(list1)
#Third Minimum in the list
third_min(list2)
#print("get list : ",get)
#print("List2 list: ",list1)
#print("Length of Get : ",len(get))
#print("Length of list1: ",len(list1))
#Compare the three_minimum_number list with cost_list
for j in range(len(get)):
  for k in range(len(list1)):
    if(get[j]==list1[k]):
        if(count<3):
            index.append(k)
            count=count+1
#Remove the Repeation of number in the index list
index = list(dict.fromkeys(index))
#print("index : ",index)
print("Nearest words : ")

for k in range(len(index)):
  for l in range(len(str2)):
    if index[k]==l:
        

            print(str2[l])
            