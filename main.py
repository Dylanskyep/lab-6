def menu ():
    print("Menu")
    print("-" * 13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def encode(password):
    new_pass = ""
    for i in password:
        i = int(i)
        if i >= 7:
            if i == 7:
                i = "0"
            if i == 8:
                i = "1"
            if i == 9:
                i = "2"
            new_pass += i
        else:
            i += 3
            i = str(i)
            new_pass += i
    return new_pass

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
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif menu_op == 1:
            encoded_password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")

if __name__ == "__main__":
    main()





