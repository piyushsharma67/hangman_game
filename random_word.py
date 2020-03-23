import random

def secret_word():
    
    word_list=[]
    with open('wordlist.txt','r') as file:
        for word in file:
            word_list.append(word)
        file.close()

    secret_word=random.choice(word_list)
   
    return str(secret_word)

 
            
            
            



