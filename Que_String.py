''' 1. Display word with Highest length
    2. To determine the frequency of occurance of the particular character in the string
    3. To Chekck whether Stirn is palindrome or not
    4. To display index of first appearance of the Stubstring
    5. To cound Ocuurance of Each word in string '''





from collections import Counter
# import panda


list1=["deshkkkkkmukh","Marinate","ben","RaJeeeeeeeeeeeeeeeeeeee:"]
list2=[]
for i in list1:
    length=(len(i))
    print (length)
    print (i)
    list2.append(length)
#     print(list2) 
maximum_length= max(list2)               # we have to use how to find index
index=list2.index(maximum_length)
print("position of the word with Highest length: ",index)
maximum_length_string = index
print ("length of longest stirg/word :",maximum_length)
print(f" {list1[index]} this is the word with hihest length !! ")             # Step 1 completed


# Step 2: Frequency Occurance of Particular Character


# count=pd.Series(list1).value_counts()
# print("Element Count")
# print(count)
occurrence={item: list1.count(item) for item in 1}
print (occurrence.get('e'))






# Step 3: Check wheter the given string is palindrom or not

string1=input("enter the String which you want to check palindrome or not? : ")

reverse_string=string1[: : -1]

if (string1==reverse_string):
    print(f" {string1} is palindrome ")
    
else:
    print(f" {string1} is not palindrome ") 














