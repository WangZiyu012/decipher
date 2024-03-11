import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#
#     TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     e.g.
#     plain_text = "hello"
#     shift = 5
#     cipher_text = "mjqqt"
#     print output: "The encoded text is mjqqt"
#
#     #HINT: How do you get the index of an item in a list:
#     https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
#     #🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#
# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

def cipher(text_1, shift_1):
    ciphered_word = ""
    for index in range(len(text_1)):
        focus_char = text_1[index]
        if focus_char in alphabet:
            added_character_index = text_1.index(focus_char) + shift_1
            added_character = alphabet[added_character_index]
            ciphered_word+= added_character
        else:
            ciphered_word += focus_char
    print(f"The ciphered word is {ciphered_word}")

def decipher(text_2, shift_2):
    deciphered_word = ""
    for index in range(len(text_2)):
        focus_char = text_2[index]
        if focus_char in alphabet:
            added_character_index = text_2.index(focus_char) - shift_2
            added_character = alphabet[added_character_index]
            deciphered_word+= added_character
        else:
            deciphered_word+= focus_char
    print(f"The deciphered word is {deciphered_word}")
def caesar(text_0, shift_0, cipher_direction):
    word = ""
    if cipher_direction == "encode":
        cipher(text_0, shift_0)
    if cipher_direction == "decode":
        decipher(text_0, shift_0)

caesar(text, shift, direction)