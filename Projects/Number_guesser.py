import random

num = input("bir sayi giriniz: ")

if num.isdigit():
    num =int(num)

    if num <= 0:
        print("lütfen 0'dan büyük bir sayi giriniz")
        quit()
else:
    print("lütfen bir sonraki sefer bir sayi tipi giriniz")
    quit()

random_number = random.randint(0,num)
guesses = 0

while True:
    guesses +=1
    user_guess=input("bir sayı tahmini yapmalısın: ")
    if user_guess.isdigit():
        user_guess =int(user_guess)
    else:
        print("lütfen bir dahaki sefere bir sayi giriniz")
        continue  # otomatik olarak bizi loopta while seviyesine getirir.
    
    if user_guess == random_number:
        print("you guessed right")
        break   # doğru bilindiğinde programı durdurmasını istiyoruz. stopping loop
    elif user_guess > random_number:
        print("Daha küçük bir sayı girmelisin")
    else:
        print("daha büyük bir sayı girmelisin")

print("you got it in" +str(guesses)+ "guesses")





    


    

