#a sample string
sample_String = "Hello! How are you?"
print(sample_String)

#convert to upper case
upper_case_String = sample_String.upper()
print(upper_case_String)

#convert to lower case
lower_Case_String = sample_String.lower()
print(lower_Case_String)

#replace
new_string = sample_String.replace("Hello", "Hi")
print(new_string)

#concatenation
sample_string_2 = "I am fine."
concatenated_string = sample_String+ " " +sample_string_2
print(concatenated_string)

print(sample_String[0:6]) #Slicing
print(sample_String[10:90])  #slicing out of range index