from flask import Flask
from flask import request
from threading import Thread

encryptedLetters = []
encryptedvalues = []
decryptedLetters = []
decryptedvalues = []

app = Flask('')

@app.route('/')
def index():
  plain_text = request.args.get("plain_text", "")
  if plain_text:
    encryptedText = encryptionprocess(plain_text)
  else:
    encryptedText = ""
  return (
    """<form action="" method="get">
          <input type="text" name="plain_text">
          <input type="submit" value="Convert">
        </form>"""
      + "Encrypted Text: "
      + encryptedText
  )
    
@app.route("/<plain_text>")             
#Text and value declarations

#Encryption function declaration
def encryptionprocess(plain_text):
  encryptedLetters = []
  encryptedvalues = []
  decryptedLetters = []
  decryptedvalues = []

  #Index declarations
  uppercase_index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  lowercase_index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  special_index = [' ', '!', '?', '(', ')', '@', '#', '$', '%', '^', '&', '*', '_', '-', '=', '+', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "'"]
  for eachletter in plain_text:
    if eachletter in uppercase_index:
      crypt = uppercase_index.index(eachletter)
      encryption = ((0 + 25) - crypt)
      encryptedvalues.append(encryption)
      newcharacter = uppercase_index[encryption]
      encryptedLetters.append(newcharacter)
    elif eachletter in lowercase_index:
      crypt = lowercase_index.index(eachletter)
      encryption = ((0 + 25) - crypt)
      encryptedvalues.append(encryption)
      newcharacter = lowercase_index[encryption]
      encryptedLetters.append(newcharacter)
    elif eachletter in special_index:
      crypt =  special_index.index(eachletter)
      encryption = ((0 + 25) - crypt)
      encryptedvalues.append(encryption)
      newcharacter = special_index[encryption]
      encryptedLetters.append(newcharacter)
  con_encryptedtext = ''.join(encryptedLetters)
  return (str(con_encryptedtext))
  


def run():
    app.run(host="0.0.0.0", port=8080)

def flask_server():
    server = Thread(target=run)
    server.start()