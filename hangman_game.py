from random_word import secret_word
 

word=secret_word()                     #printing the string with only vowels
word=word.rstrip("\n")
length=len(word)
ch_lst=[]

count_vow=0
print("your hint is as below")

for i in range(length):               #code for printing the hint
    if (word[i] in 'aeiou'):
        print(word[i],end='\0')
        count_vow=count_vow+1
    else:
        print("_",end="\0")

def string_fin(user_ch,lst,word_1):      #function for printing string after correct choice
    length=len(word_1)
    for i in range(length):
        if (word_1[i] in 'aeiou' or word_1[i]==user_ch or word_1[i] in lst):
            print(word[i],end='\0')
            
        else:
            print("_",end="\0")

word_left=length-count_vow

choice=length
print(f"you have {length} choices")
while (choice!=0):
    print(end='\n')
    
    char=input("enter your choice ")        #code for accepting the choice and validating it
    if(char in word):
        count_1=word.count(char)
        word_left=word_left-count_1
        print(f"you have {choice} choices left and {word_left} to fill")
        ch_lst.append(char)
        print("your current string is as below")
        string_fin(char,ch_lst,word)    
    
    else:
        choice=choice-1
        print(f"opps wrong choice you have {choice} choices left")
 
        
    if(word_left==0):
        print(end="\n")
        print(f"congratulation you won!!! and the secret word is {word}")
        break
else:
    print(f"sorry you failed and the correct word is {word}")






