def menu ():
    print("Menu")
    print("-" * 13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def decode(password):
    decoded = []
    for char in password:
        decode_char = str((int(char) - 3) % 10)
        decoded.append(decode_char)
    return "".join(decoded)

def main():
    encoded_password = ""
    while True:
        menu()
        menu_op = int(input("Please enter an option: "))
        if menu_op == 3:
            break
        elif menu_op == 2:
            encoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}")
        elif menu_op == 1:
            encoded_password = encode(input("Please enter a password to encode: "))
            print("Your password has been encoded and stored")


if __name__ == "__main__":
    main()





