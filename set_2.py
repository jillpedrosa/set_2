def shift_letter(letter,shift):
    '''Shift Letter'''
    if letter == " ":
        return " "
    start = ord('A')
    offset = ord(letter) - start
    new_offset = (offset + shift) % 26
    return chr(start + new_offset)

def caesar_cipher(message,shift):
    '''Caesar Cipher'''
    shifted_message = ""

    for char in message:
        if char == " ":
            shifted_message += " "
        elif char.isupper():
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            shifted_message += shifted_char
        else:
            shifted_message += char
    return shifted_message

def shift_by_letter(letter,letter_shift):
    '''Shift by Letter'''
    if letter == " ":
        return " "
    start = ord ('A')
    shift = ord (letter_shift) - start
    offset = ord(letter) - start
    new_offset = (offset + shift) % 26
    return chr(start + new_offset)

def vigenere_cipher(message,key):
    '''Vigenere Cipher'''
    key=list(key)
    cipher_text=[]
    if len(message)>len(key): 
        for i in range(len(message)):
            key.append(key[i % len(key)])
            lengthened_key=key
            m = (ord(message[i]) +ord(lengthened_key[i])) % 26
            x=m+ord('A')
            if message[i]== " ":
                cipher_text.append(" ")
            else:
                cipher_text.append(chr(x))
        return ("".join(cipher_text))
    else: #len(message) == len(key), len is<key 
        for i in range(len(message)):
            n = (ord(message[i]) +ord(key[i])) % 26
            y=n+ord('A')
            if message[i]== " ":
                cipher_text.append(" ")
            else:
                cipher_text.append(chr(y))
        return("" . join(cipher_text))

def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += "_"
    
    n = len(message)
    encoded_message = [''] * n
    
    for i in range(n):
        encoded_message[i] = message[(i // shift) + (n // shift) * (i % shift)]
    return ''.join(encoded_message)

def scytale_decipher(message, shift):
    if len(message)%(len(message) // shift)==0:
        shift= len(message)//shift
        cipher_text=[]
        if len(message)%shift!=0:
            while len(message)%shift!=0: 
                message+="_"
        for i in range(len(message)): 
            x=(i // shift) + (len(message) // shift) * (i % shift)
            cipher_text.append(message[x])
        return("".join(cipher_text))
