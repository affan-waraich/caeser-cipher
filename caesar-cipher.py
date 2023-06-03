alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caeser(start_text, shift_amount, cipher_direction):
  if direction == 'decode':
      shift_amount *= -1
  end_text = ""
  for char in start_text:
      if char in alphabets:
          position = alphabets.index(char)
          new_position = position + shift_amount
          end_text += alphabets[new_position]
      else:
          end_text += char
  print(f"Your {direction}d message is {end_text}")
should_end = False
while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caeser(start_text=text, shift_amount=shift, cipher_direction=direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == 'no':
      should_end = True
      print("goodbye")