win=0
lost=0
while True:
    import random

    words=["apple","orange","mango","banana"]
    word=random.choice(words)
    print(words)


    guess_word=input("Enter a word:")
   
    if guess_word==word  :
        
        win=win+1
        print("You win")   
        print(f"random word is {word}")    
    elif guess_word!=word:
      
        lost=lost+1
        print("You lost")
        print(f"random word is {word}")  
        a=input("Answer again (y/n)")
    if a=="y":
            continue
    else:
            print(f"You win {win} time and you lost {lost} time")
            break
          

                

        
        
   


