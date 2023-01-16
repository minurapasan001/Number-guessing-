Name = str(input("Enter your Name: "))
Answer = input("Do you want to play Game (Y/N): ")
Answer = Answer.upper()

while True:
    import random,time

    guessnum1 = int(random.randint(1, 6))
    guessnum2 = int(random.randint(1, 6))
    guessnum3 = int(random.randint(1, 6))
    guessnum4 = int(random.randint(1, 6))
    guessnumlist = [guessnum1, guessnum2, guessnum3, guessnum4]

    if Answer == "Y" or Answer == "y" :
        print("\n""Hello ", Name.capitalize(), " Welcome to GameInt...")
        print("\n\t--* GAME STARTED *__")
        time.sleep(1.3)
        print("\n""Color Mapping:")
        time.sleep(0.5)
        print("1-White", " ", "2-Blue", " ", "3-Red""\n""4-Yellow", "", "5-Green", "", "6-Purple")

        points = 0
        count = 1
        while count < 8:
            print("Attempt No: ", count)
            while True:
                typeguess = int(input("Guess the guess num : "))
                exit_game = input("You can exit the game enter 0000 or "
                                  "enter any key you can continue the game : ")
                if exit_game == "0000":
                    print("Thank you for playing game..")
                    break
                if typeguess == 0000:
                    break

                if 1111 <= typeguess <= 6666:
                    print("")
                    guesslist = list(map(int, str(typeguess)))

                    if 0 < guesslist[0] < 7:
                        if 0 < guesslist[1] < 7:
                            if 0 < guesslist[2] < 7:
                                if 0 < guesslist[3] < 7:
                                    break

                else:
                    print("please Use only 1 to 6 four digits")
            count = count + 1
            if typeguess == 0000:
                break

            if guesslist[0] == guessnum1:
                n1 = 1
            elif guesslist[0] == guessnum2 or guesslist[0] == guessnum3 or guesslist[0] == guessnum4:
                n1 = 0
            else:
                n1 = "."
            if guesslist[1] == guessnum2:
                n2 = 1
            elif guesslist[1] == guessnum3 or guesslist[1] == guessnum4 or guesslist[1] == guessnum1:
                n2 = 0
            else:
                n2 = "."
            if guesslist[2] == guessnum3:
                n3 = 1
            elif guesslist[2] == guessnum4 or guesslist[2] == guessnum1 or guesslist[2] == guessnum2:
                n3 = 0
            else:
                n3 = "."
            if guesslist[3] == guessnum4:
                n4 = 1
            elif guesslist[3] == guessnum1 or guesslist[3] == guessnum2 or guesslist[3] == guessnum3:
                n4 = 0
            else:
                n4 = "."
            print(n1, n2)
            print(n3, n4)

            if n1 == 1 and n2 == 1 and n3 == 1 and n4 == 1:
                print("Congratulations !!!!! You have won the game")
                break

        if typeguess == 0000:
            break

        if n1 == 1:
            points = points + 1
        if n2 == 1:
            points = points + 1
        if n3 == 1:
            points = points + 1
        if n4 == 1:
            points = points + 1

        print("You have scored ", points, " points.")

        print("Random number is ", guessnum1, guessnum2, guessnum3, guessnum4)

        print("Do you want to play the another game\n")
        Answer = input("Enter (Y/N): ")
        print("\n")
        Answer = Answer.upper()

    elif Answer == "N" or Answer == "n":
        print("Thank you for joining game")
        break

    else:
        print("Invalid")
        break
