# def most_frequent_char(str):
#     # a dictionary to store char and it's frequency
#     frequency_dict={}
#     for i in str:  #loop over the string
#         if(i.isalpha()):  # if the current char is alphabet (a-z, A-Z)
#             #if already in dict then just increase count by 1
#             if i in frequency_dict:  
#                 frequency_dict[i] = frequency_dict[i]+1
#             #else create a new item in dictionary
#             else:
#                 frequency_dict[i]=1
#     #if no alphabet in string
#     if(frequency_dict == {}):
#         print("No valid characters found")
#     else:
#         max_count_char='a' #store the char with max freq
#         max_count = 0      #store max frequency
#         for i in frequency_dict: #update both by looping in the dictionary
#             if(frequency_dict[i]>=max_count):
#                 max_count_char=i
#                 max_count=frequency_dict[i]
#         print((max_count_char,max_count)) #print tuple

# input_str = input("Enter string: ")
# most_frequent_char(input_str)

# The Counter class is a specialized dictionary in 
# collections module used for counting 
# the frequency of elements in an iterable.
from collections import Counter

def most_frequent_char(str):
    #create a list containg alphabets from string
    char_list = [i for i in input_str if i.isalpha()]
    if (char_list == []):
        print("No valid characters found")
        return
    #Coutner function returns a dictionary containg
    #elements and their count
    counts = Counter(char_list)
    #most_common() function returns the elements with highest
    #frequency. Number of elements returned = parameter passed
    #It returns a list of tuple. So, [0] to fetch only first item(tuple)
    print(counts.most_common(1)[0])

input_str = input("Enter string: ")
most_frequent_char(input_str)
# print (char_list)
