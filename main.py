alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['#', '$', '%', '&', '/', "'", '(', ')', '*', '+', ',', '-', '.', ':', ';', "<", '>', '=', '?', '@', '[', ']', '_', '{', '}', "|", '!', '^', '#', '$', '%', '&', '/', "'", '(', ')', '*', '+', ',', '-', '.', ':', ';', "<", '>', '=', '?', '@', '[', ']', '_', '{', '}', "|", '!', '^']
def caesar(start_text, shift_for_letters, shift_for_nums, shift_for_syms, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_for_letters *= -1
    shift_for_nums *= -1
    shift_for_syms *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_for_letters
      end_text += alphabet[new_position]
    elif char in numbers:
      num_position = numbers.index(char)
      num_new_position = num_position + shift_for_nums
      end_text += numbers[num_new_position]
    elif char in symbols:
      sym_position = symbols.index(char)
      sym_new_position = sym_position + shift_for_syms
      end_text += symbols[sym_new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)
print("....::::The Caesar Cipher: Encryption Program::::....\n")
help = input("If you need help, type 'help', if not type 'no': ").lower()
if help == "help":
  print("\nThis program can encode and decode your text input using Caesar Cipher's encryption method. We need a shift number for shift the alphabet.\nWhat is shift number? For example, if our shift number is 3, A would be replaced by D, B would become E, and so on.\nAnd when you want to decode your text, you should type your correct shift number")

should_end = False
while not should_end:

  direction = input("\n\nType 'encode' to encrypt, type 'decode' to decrypt: ")
  text = input("Type your message: ").lower()
  letter_shift = int(input("Type the shift number: "))
  shift_lets = letter_shift % 26
  shift_nums = letter_shift % 10
  shift_syms = letter_shift % 28 # modded for list range

  caesar(start_text=text, shift_for_letters=shift_lets, shift_for_nums=shift_nums, shift_for_syms=shift_syms, cipher_direction=direction)

  restart = input("\tType 'yes' to do more. Otherwise type 'no' to exit the program: ")
  if restart == "no":
    should_end = True
    print("\n\nCipher Says Goodbye\n\n")
    
