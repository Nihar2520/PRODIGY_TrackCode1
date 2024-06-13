from tkinter import *

def encrypt_text():

  try:
    shift_value = int(shift_entry.get())
  except ValueError:
    output_text.delete(0.0, END)  # Clear output area
    output_text.insert(INSERT, "Invalid shift value. Please enter an integer.")
    return

  original_text = input_text.get("1.0", END)  # Get text from input field
  encrypted_text = caesar_cipher_encrypt(original_text, shift_value)
  output_text.delete(0.0, END)  # Clear output area
  output_text.insert(INSERT, encrypted_text)

def decrypt_text():
  """
  Decrypts the text in the input field based on the shift value.
  """
  try:
    shift_value = int(shift_entry.get())
  except ValueError:
    output_text.delete(0.0, END)  # Clear output area
    output_text.insert(INSERT, "Invalid shift value. Please enter an integer.")
    return

  original_text = input_text.get("1.0", END)  # Get text from input field
  decrypted_text = caesar_cipher_decrypt(original_text, shift_value)
  output_text.delete(0.0, END)  # Clear output area
  output_text.insert(INSERT, decrypted_text)

def caesar_cipher_encrypt(text, shift):
  """
  Encrypts the provided text using Caesar Cipher algorithm.
  """
  encrypted_text = ""
  for char in text:
    if char.isalpha():
      shift_base = 65 if char.isupper() else 97
      encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
      encrypted_text += encrypted_char
    else:
      encrypted_text += char
  return encrypted_text


def caesar_cipher_decrypt(text, shift):
  """
  Decrypts the provided text using Caesar Cipher algorithm.
  """
  decrypted_text = ""
  for char in text:
    if char.isalpha():
      shift_base = 65 if char.isupper() else 97
      decrypted_char = chr((ord(char) - shift_base + (-shift)) % 26 + shift_base)
      decrypted_text += decrypted_char
    else:
      decrypted_text += char
  return decrypted_text

# Create the main window
window = Tk()
window.title("Caesar Cipher Tool")

# Input field for text
input_text = Text(window, height=10, width=50)
input_text.pack(padx=10, pady=10)

# Label for shift value
shift_label = Label(window, text="Shift Value:")
shift_label.pack(padx=10)

# Entry field for shift value
shift_entry = Entry(window, width=5)
shift_entry.pack(padx=10)

# Encrypt button
encrypt_button = Button(window, text="Encrypt", command=encrypt_text)
encrypt_button.pack(padx=10, pady=10)

# Decrypt button
decrypt_button = Button(window, text="Decrypt", command=decrypt_text)
decrypt_button.pack(padx=10, pady=10)

# Output text area
output_text = Text(window, height=10, width=50)
output_text.pack(padx=10, pady=10)

# Run the main event loop
window.mainloop()
