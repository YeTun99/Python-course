import random
words=["apple","orange","mango","banana"]
word=random.choice(words)
print(words)

while True:
    guess_word=input("Enter a word:")
    win=0
    lost=0
    if guess_word==word:
        win+=1
        print("You win")   
        print(f"random word is {word}")    
    elif guess_word!=word:
        lost+=1
        print("You lost")
        print(f"random word is {word}")  
        a=input("Answer again (y/n)")
        if a!="y":
            print(f"You win {win} and you lost {lost}")
            break
          

                

        
        
   


