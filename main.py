
while 1:
    print("")
    num = int(input("Factor the number "))
    print(" ")
    count = 1
    output = 0

    def is_whole(n):
        return n % 1 == 0

    while count <= num:
        output = num / count
        if is_whole(output):
            print(int(output), end=" ")
        count += 1
    count = 1
