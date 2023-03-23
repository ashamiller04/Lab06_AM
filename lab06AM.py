# Asha Miller
running = True      # for the while loop


def menu():     # creates a menu function for easy repetition
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


def encode(given_pw):       # encodes a given password by adding 3 to each number
    og_password = given_pw
    encoded_pw = []
    for item in og_password:    # goes through each character in the input string and encodes it
        num = int(item)
        if num + 3 == 10:   # if and elif statements account for double digits
            new_num = '0'
            encoded_pw.append(new_num)      # adds new number to the encoded_pw list
        elif num + 3 == 11:
            new_num = '1'
            encoded_pw.append(new_num)
        elif num + 3 == 12:
            new_num = '2'
            encoded_pw.append(new_num)
        else:
            new_num = num + 3
            new_num = int(new_num)
            encoded_pw.append(new_num)
    final = ''.join(str(num) for num in encoded_pw)     # joins items together for a combined string
    return final


# main program
while running:
    menu()  # prints menu function
    print()
    option = int(input('Please enter an option: '))
    if option == 1:
        password = input('Please enter your password to encode: ')
        storage = encode(password)      # stores the password for later decoding
        print('Your password has been encoded and stored!')
    elif option == 2:
        encoded_password = encoder(password)
        original_password = password
        print(f"The encoded password is {encoded_password}, and the original password is {original_password}."
    elif option == 3:
        running = False     # ends the while loop
    else:
        print('Please enter a valid option.')
