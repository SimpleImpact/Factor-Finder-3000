import math, time

count = 1
page = 1

def is_whole(n):
        return n % 1 == 0

def calc():

    global count
    global page

    print("1. Add         ")
    print("2. Subtract    ")
    print("3. Multiply    ")
    print("4. Divide      ")
    print("5. Factor      ")
    print("6. Square      ")
    print("7. Square Root ")
    print("8. Quadratic   ")
    print("9. Next Page")
    choice = int(input("Choose 1-9: "))

    if page == 1:

        if choice == 9:
            page = 2

        if choice == 1:
            print(int(input("1st Number: ")) + int(input("2nd Number: ")))

        if choice == 2:
            print(int(input("1st Number: ")) - int(input("2nd Number: ")))

        if choice == 3:
            print(int(input("1st Number: ")) * int(input("2nd Number: ")))

        if choice == 4:
            print(int(input("1st Number: ")) / int(input("2nd Number: ")))

        if choice == 5:
            num = int(input("What number: "))

            while count <= num:
                output = num / count
                if is_whole(output):
                    print(int(output), end=" ")

                count += 1

        if choice == 6:
            num = int(input("What number: "))
            print(num * num)

        if choice == 7:
            num = int(input("What number: "))
            print(int(math.sqrt(float(num))))

        if choice == 8:
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(( -(b) + math.sqrt((b * b)) -4 * (a) * (c)) / a)
            print(( -(b) - math.sqrt((b * b)) -4 * (a) * (c)) / a)

    if page == 2:
        print("\n", " Page 2", "\n")
        print("1. Pythagorean (solve for c)  ")
        print("2. Pythagorean (solve for a) ")
        print("3. Find Midpoint ")
        choice = int(input("Choose 1-2: "))

        if choice == 1:
            a = float(input("a = "))
            b = float(input("b = "))
            answer = (math.sqrt((a * a) + (b * b)))
            if is_whole(answer):
                print(answer)
            else:
                answer = answer * answer
                print("sqrt(" + str(answer) + ")")

        if choice == 2:
            b = float(input("b = "))
            c = float(input("c = "))
            answer = math.sqrt((c * c) - (b * b))
            if is_whole(answer):
                print(answer)
            else:
                print("sqrt(" + str(int(answer * answer)) + ")")

        if choice == 3:
            x1 = int(input("What is x1: "))
            x2 = int(input("What is x2: "))
            y1 = int(input("What is y1: "))
            y2 = int(input("What is y2: "))
            x = (x1 + x2) / 2
            y = (y1 + y2) / 2
            print("(" + str(int(x)) + "," + str(int(y)) + ")")
    time.sleep(3)
    calc()
calc()
