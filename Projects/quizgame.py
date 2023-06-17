
#-----------------------------------------
def newgame():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for i in questions:
        print("-----------------------------")
        print(i)
        for i in options[question_num-1]:
          print(i)  

        guess = input("ENTER (A,B,C,D)")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(i),guess)
        question_num += 1

    display_score(correct_guesses,guesses)

#-----------------------------------------
def check_answer(answer,guess):
   if answer == guess:
      print("CORRECT")
      return 1
   else:
      print("WRONG")
      return 0
   
#-----------------------------------------
def display_score(correct_guesses,guesses):
   print("------------------------")
   print("RESULTS")
   print("------------------------")
   
   print("Answer: ", end= " ")
   for i in questions:
      print(questions.get(i), end= " ")
   print()
   
   print("Guesses: ", end= " ")
   for i in guesses:
      print(i, end= " ")
   print()

   score = int((correct_guesses/len(questions))*100)
   print("your score is: "+ str(score)+"%")
#-------------------------------------------
def play_again():
   response = input("Do you want to play again?(yes or no: ")
   response = response.upper()

   if response == "YES":
      return True
   else:
      return False

#---------------------------------------


questions = {
    "who created python?: " : "A",
    "what year was python created?: " : "B",
    "python is tributed to which comedy group?: " : "C",
    "is the earth running?: " : "A"
}

options = [["A. van rossum","B. Elon Musk","C.Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1998","B. 2000","C.2100", "D. 2001"],
           ["A. Lonely","B. Smash","C. python ", "D. Snl"],
           ["A. true","B.False","C. sometimes","D. everytime"]]


newgame()

while play_again():
    newgame()
print("Byeeeee!")