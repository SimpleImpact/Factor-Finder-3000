import math

count = 1
page = 1

def is_whole(n):
        return n % 1 == 0

print("1. Add         ")
print("2. Subtract    ")
print("3. Multiply    ")
print("4. Divide      ")
print("5. Factor      ")
print("6. Square      ")
print("7. Square Root ")
print("8. Quadratic   ")
print("9. Pythagreon  ")
print("10. Next Page   ")
choice = int(input("Choose 1-10: "))

if page == 1:
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

    if choice == 9:
        a = float(input("a = "))
        b = float(input("b = "))
        answer = (math.sqrt((a * a) + (b * b)))
        if is_whole(answer):
            print(answer)
        else:
            answer = answer * answer
            print("sqrt(", answer, ")")
            
