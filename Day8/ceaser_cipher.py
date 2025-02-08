import art
print(art.art)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


opinion = True


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
             end_text += char
    print(f"The {cipher_direction}s text is {end_text}")
   


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt':\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type no.\n")
    if restart == "no":
         should_continue = False
         print("Goode Bye")




# def encrypt(plain_text, shift_amount):
#     cipher_txt = ''

#     for letter in plain_text:
#         position = alphabet.index(letter)
        
#         if position > len(alphabet)-shift_amount -1:
#             new_position = position - (len(alphabet)-shift_amount - 1) -1
#         else:
#             new_position = position + shift_amount
#         cipher_txt += alphabet[new_position]
#     print(f"cipher textt is {cipher_txt}")

# if text == "encode":
#     encrypt(plain_text=text, shift_amount=shift)

# def dencrypt(plain_text, shift_amount):
#     cipher_txt = ''

#     for letter in plain_text:
#         position = alphabet.index(letter)
        
#         if position <= shift_amount:
#             new_position = len(alphabet) + position - shift_amount 
#         else:
#             new_position = position - shift_amount
#         cipher_txt += alphabet[new_position]
#     print(f"cipher textt is {cipher_txt}")

# if text == "decode":
#     dencrypt(plain_text= text, shift_amount= shift)


