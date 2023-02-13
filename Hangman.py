import random


names = ["shayan", "fardin", "alireza", "mahsa", "afsane", "vahid", "parsa", "shahin", "ahmad", "hamid", "lena"]
answer = random.choice(names)
print("Guess the word....")
number_of_try = 6
Your_answer = ['_' for _ in range (len(answer))]
while number_of_try > 0 :
    letter = input()
    if letter in answer :
        for i in range (len(answer)) :
            if letter == answer[i] :
                Your_answer[i] = letter
        print(*Your_answer)
        if Your_answer.count("_") == 0 :
            print("You win........")
            break
    else :
        print(f"You guess {letter}, That's not in the word, You lose 1 life....")
        number_of_try -= 1
        if number_of_try == 0 :
            print("Game Over...")