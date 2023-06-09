alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
  'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
  'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
  'y', 'z']


def caesar(message, number, choice):
    cipher_message = ""
    if choice == "decode":
        number *= -1
    for char in message:
        if char in alphabets:
            position = alphabets.index(char)
            shifted = position + number
            cipher_message += alphabets[shifted]
        else:
            cipher_message += char

    print(f"The {choice}d text is {cipher_message}")

should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    shift = shift % 25

    caesar(message=text, number=shift, choice=direction)

    text_again = input("Type 'yes' if you want to go again. Otherwise Type no.\n").lower()
    if text_again == "no":
        should_continue = False
        print("Goodbye")
