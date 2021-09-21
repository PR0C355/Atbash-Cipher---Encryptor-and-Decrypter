import flask_server
import time

#Text and value declarations
encryptedtext = []
encryptedvalues = []
decryptedtext = []
decryptedvalues = []


#Index declarations
uppercase_index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lowercase_index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

special_index = [' ', '!', '?', '(', ')', '@', '#', '$', '%', '^', '&', '*', '_', '-', '=', '+', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "'"]

#Encryption function declaration
def encryptionprocess():
  plain_text = input('\nWhat text would you like to encrypt? ')
  for eachletter in plain_text:
    if eachletter in uppercase_index:
      crypt = uppercase_index.index(eachletter)
      encryption = ((0 + 25) - crypt)
      encryptedvalues.append(encryption)
      newcharacter = uppercase_index[encryption]
      encryptedtext.append(newcharacter)
    elif eachletter in lowercase_index:
      crypt = lowercase_index.index(eachletter)
      encryption = ((0 + 25) - crypt)
      encryptedvalues.append(encryption)
      newcharacter = lowercase_index[encryption]
      encryptedtext.append(newcharacter)
    elif eachletter in special_index:
      crypt =  special_index.index(eachletter)
      encryption = ((0 + 25) - crypt)
      encryptedvalues.append(encryption)
      newcharacter = special_index[encryption]
      encryptedtext.append(newcharacter)
      
#Decryption function declaration
def decryptionprocess():
  cipher_text = input('\nWhat text would you like to decrypt? ')
  for eachletter in cipher_text:
    if eachletter in uppercase_index:
      decipher = uppercase_index.index(eachletter)
      decryption = ((0+ 25) - decipher)
      decryptedvalues.append(decryption)
      newcharacter = uppercase_index[decryption]
      decryptedtext.append(newcharacter)
    elif eachletter in lowercase_index:
      decipher = lowercase_index.index(eachletter)
      decryption = ((0+ 25) - decipher)
      decryptedvalues.append(decryption)
      newcharacter = lowercase_index[decryption]
      decryptedtext.append(newcharacter)
    elif eachletter in special_index:
      decipher =  special_index.index(eachletter)
      decryption = ((0 + 25) - decipher)
      decryptedvalues.append(decryption)
      newcharacter = special_index[decryption]
      decryptedtext.append(newcharacter)


flask_server.flask_server()
time.sleep(3)

#Input on chosen process (Encryption or decryption)       
chosen_process = input('Would you like to encrypt, or decrypt? ')

#Action as a a result of chosen process
if chosen_process.lower() == 'encrypt':
  encryptionprocess()
  con_encryptedtext = ''.join(encryptedtext)
  print('')
  print('Here is your encrypted text: \n'+ con_encryptedtext)
elif chosen_process.lower() == 'decrypt':
  decryptionprocess()
  con_decryptedtext = ''.join(decryptedtext)
  print('')
  print('Here is your decrypted text: \n'+ con_decryptedtext)
else:
  print("If you don't want to Encrypt or Decrypt, I can't help you.")