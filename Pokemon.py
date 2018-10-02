import random as r

arr = []
x = y = 0

def write():
    file = open("pokemon.txt", "w")
    text = ""
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == y and j == x:
                text += "1"
            elif arr[i][j] == "o":
                text += "0"
            elif arr[i][j] == "#":
                text += "2"

            if j < len(arr[i]) - 1:
                text += ","
        text += "\n"

    if arr[y][x] == "#":
        text += "1"
    else:
        text += "0"

    file.write(text)
    file.close

def pokemon():
    chance = r.randint(0,2)
    if chance == 0:
        print("There is a pokemon.")

file = open("pokemon.txt", "r")
read = file.read().split("\n")
for row in range(0,8):
    f = read[row].split(",")
    arr.append([])
    for col in range(len(f)):
        if f[col] == "0":
            print("o", end="  ")
            arr[row].append("o")
        elif f[col] == "1":
            print("X", end="  ")
            arr[row].append("o")
            x = col
            y = row
        elif f[col] == "2":
            print("#", end="  ")
            arr[row].append("#")
    print(" ")

if read[8] == "0":
    arr[y][x] = "o"
elif read[8] == "1":
    arr[y][x] = "#"
file.close()

while 1:
    print("============")
    print("    MENU    ")
    print("============")
    print("[1] Move up")
    print("[2] Move down")
    print("[3] Move left")
    print("[4] Move right")
    print("[5] Save & Exit")
    c=input("what do you want to do?[1..5]:")

    if c == "1":
        if (y - 1 >= 0):
            y -= 1
    elif c == "2":
        if (y + 1 <= 7):
            y += 1
    elif c == "3":
        if (x - 1 >= 0):
            x -= 1
    elif c == "4":
        if (x + 1 <= 7):
            x += 1
    elif c == "5":
        write()
        break
    else:
        print("Wrong Input")

    if (arr[y][x] == "#"):
        pokemon()

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == y and j == x:
                print("X", end="  ")
            elif arr[i][j] == "o":
                print("o", end="  ")
            elif arr[i][j] == "#":
                print("#", end="  ")
        print(" ")