'''
 05. Write a Python program to count the number of vowels present in a given string.
 (considering both upper case and lower case)
'''

def count_vowels(string): #defining a function to count the number vowels present in string
    count = 0       #initializing the count to 0
    for i in string:        #using for loop checking i with every element of the string
        if(i=='a' or i=='u' or i=='e' or i=='i' or i=='o' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'): #checking i with the string for vowels
            count += 1 #count will be incremented by 1 if vowel is present in the string    
    if(count==0):
        print("There are no vowels present in the string") #if count is 0 then there will be no vowels present in the string
    else:
        return count #this will return the number of vowels present in it
    
string = input("Enter the String: ") #Enter the string 
vowel_count = count_vowels(string)  #Calling the count_vowels function
print("The number of vowels in the string is", vowel_count) #Prints the number of vowels




        