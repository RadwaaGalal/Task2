def print_R():
    for row in range(7):
        for col in range(5):
            print(end=" ")
            if col == 0 or (col == 4 and (row != 0 and row != 3)) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
                print("R", end="")
            else:
                print(end=" ")
        print(" ")
def print_A():
    for row in range(7):
        for col in range(5):
            print(end=" ")
            if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
                print("A", end="")
            else:
                print(end=" ")
        print(" ")

def print_D():
    for row in range(7):
        for col in range(5):
            print(end=" ")
            if col == 0 or (col == 4 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4)):
                print("D", end="")
            else:
                print(end=" ")
        print(" ")

def print_W():
    for row in range(4):
        for col in range(9):
            print(end=" ")
            if (col == 0 or col == 8) or (col == 2 and row == 2) or (col == 4 and row == 1) or (col == 6 and row == 2):
                print("W", end="")
            else:
                print(end=" ")
        print(" ")

def print_G():
    for row in range(7):
        for col in range(5):
            print(end=" ")
            if (col == 0 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4)) or (
                    col == 4 and row == 4) or (col == 4 and row == 3) or (col == 3 and row == 3) or (
                    col == 4 and row == 5):
                print("G", end="")
            else:
                print(end=" ")
        print(" ")
def print_L():
    for row in range(6):
        for col in range(6):
            print(end=" ")
            if col == 0 or row == 5:
                print("L", end="")
            else:
                print(end=" ")
        print(" ")




print_R()
print("\n")
print_A()
print("\n")
print_D()
print("\n")
print_W()
print("\n")
print_A()
print("-----------------------------------------------------")
print_G()
print("\n")
print_A()
print("\n")
print_L()
print("\n")
print_A()
print("\n")
print_L()
