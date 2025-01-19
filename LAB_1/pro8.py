# Count the Vowels in a String
userStr="I Love Python Programming"

# function defination
def count_vowels(userStr):
    vowels= "aeiouAEIOU"
    count=0
    
    for char in userStr:
        if char in vowels:
            print("Vowel: ",char)
            count+=1
    return count

# fuction call
vowels_count= count_vowels(userStr)
print(f"The number of vowels in the String is: {vowels_count}")



