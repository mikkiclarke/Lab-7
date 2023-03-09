def menu():
    print("\n   Menu   ")
    print("-----------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(password):
    password: list[password]
    for i in password:
        j = int(i)
        k = j + 3
        if 0 < k < 10:
            print(k, end="")
        elif k > 9:
            if k == 10:
                print("0", end="")
            elif k == 11:
                print("1", end="")
            elif k == 12:
                print("2", end="")


def make_list(password):
    list1 = []
    list1[:0] = password
    password = list1
    return password


def decoder(password):
    table = {0: '7', 1: '8', 2: '9', 3: '0', 4: '1',
             5: '2', 6: '3', 7: '4', 8: '5', 9: '6'}
    encoded = ''
    password = make_list(password)
    for i in range(0, len(password)):
        password[i] = int(password[i])

    for num in password:
        encoded = encoded+table[num]
    return encoded


def main():
    while True:
        menu()
        option = input("Enter menu option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            print("\nYour password has been encoded and stored.")
        elif option == "2":
            print("The encoded password is ", end="")
            encode(password)
            print(f", and the original password is {password}.\n")
        elif option == "3":
            break


if __name__ == "__main__":
    main()
