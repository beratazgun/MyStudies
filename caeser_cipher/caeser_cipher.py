import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# print(len(alphabet))
def ceaser(text, shift, direction):
        end_text = ""
        if direction == 'decode':
            shift *= -1
        print(shift)
        for letter in text: # b a
            if letter in alphabet:
                number_of_index = alphabet.index(letter) 
                number_of_index += shift 
                number_of_index = number_of_index % 26
                if number_of_index >= 27:
                    end_text += alphabet[number_of_index]

                else:
                    end_text += alphabet[number_of_index]
            
            else:
                end_text += letter

        print(f"The encoded text is '{end_text}'")

        

condition = True
while condition == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt(encode/decode):\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))  

    ceaser(text, shift, direction)
    again = input("Would you like to go again? Type 'yes' or 'no':\n")

    if again == 'no':
        print("Goodbye!")
        break
    elif again == 'yes':
        condition = True
    else:
        print("Please type 'yes' or 'no'")
    










