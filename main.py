def menu():
    print("\n   Menu   ")
    print("-----------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(password):
    pass_list: list[password]
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
    return


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
            print(", and the original password is ")
        elif option == "3":
            break


if __name__ == "__main__":
    main()
