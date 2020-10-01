print("\t \t \t \t \t \t \t \t \t \t "+"***CodeOfStar***"+"\n")

print("Input q for quit \n")

Programe_over = False

while Programe_over is False:
    n = input("How many times do you want to print star pattern:")

    if n == "q":
        Programe_over = True
    else:
        print("\n Code Of Star Pattern \n ")

        boolean = int(input("1 for decreasing order and 0 for increasing order:"))
        number = int(n)
        new_n = number + 1

        def convert_bool(_bool):
            if _bool == 0:
                return True
            elif _bool == 1:
                return False

        if number< 0:
            print("Your input is a negative number")

        else:
            if boolean == 0 or boolean == 1:

                if (convert_bool(boolean)):
                    print("\n * pattern in ascending order")

                    for times in range(new_n):
                        print("*" * times)

                elif (not convert_bool(boolean)):
                    print("* pattern in decending order")

                    # This thing can be done by for loop but it become complex
                    while number >= 1:
                        print("*" * number)
                        number = number - 1
            else:
                print("Sorry you have to only input 0 or 1")
