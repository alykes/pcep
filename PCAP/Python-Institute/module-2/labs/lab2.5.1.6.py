# Caesar cipher.
text = input("Enter your message: ")

shift = int(input("Please enter a shift value(1-25): "))

if shift <= 1 or shift >= 25:
    print("You didn't enter a value between 1 to 25") 

else:
    cipher = ''

    for char in text:
        if not char.isalpha():
            cipher += char
            continue

        code = ord(char) + shift

        if char.islower():
            if code > ord('z'):
                code = ord('a') + (code - ord('z') - 1)
        elif char.isupper():
            if code > ord('Z'):
                code = ord('A') + (code - ord('Z') - 1 )

        cipher += chr(code)

    print(cipher)