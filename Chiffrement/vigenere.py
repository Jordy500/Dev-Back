import string

def chiffre_vigenere(message, key):
    alphabet = string.ascii_lowercase + "éèêàôëùïü"
    vigenere_key = [ord(k) - ord('a') for k in key.lower()]
    
    vigenere_message = []
    
    key_index = 0
    
    for char in message:

            shift = vigenere_key[key_index % len(vigenere_key)]
            char_index = alphabet.index(char)
            new_index = (char_index + shift) % len(alphabet)
            vigenere_message.append(alphabet[new_index])
            key_index += 1

    
    return ''.join(vigenere_message)

message = "je me debrouillé"
key = "abc"
print(chiffre_vigenere(message, key))
