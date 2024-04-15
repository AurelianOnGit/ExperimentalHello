def main():
    Hello()

def Hello():
    Name = checkString()
    print(f"Hello, {Name}")

def checkString():
    while True:
         name = input("What's your name: ")
         if len(name) > 10:
            print("Your name is too long")
         elif (len(name) == 0):
            print("Your name cannot be blank")

main()
