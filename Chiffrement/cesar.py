import string

def cesar_cipher(message, key):
    return cesar(message, key)

def cesar(message, key):
    
    crypted_message = ""
    
    for char in message :

        index_carac_in_printable = alphabet.index(char)
        index_crypted_char = (index_carac_in_printable + key) % len(alphabet)
        crypted_char = alphabet[index_crypted_char]

        crypted_message += crypted_char
    
    return crypted_message

# Dechiffrement Proposé Prof
'''
def dechiffrer_cesar(message, key):
    
    return cesar (message, -key)

# Dechiffremet Perso

''.join([alphabet[(alphabet.index(carac) - key) % len(alphabet)] 
                    if carac in alphabet else carac for carac in message])


print(dechiffrer_cesar("coucou", 520))
'''
# Brute Force
'''
def bruteforce_cipher(message):
    return cesar(message, min(range(26), key=lambda x: sum(c1 != c2 for c1, c2 in zip(message, cesar(message, x)))))
'''
def cesar_uncipher(crypted_message, key):
	return cesar_cipher(crypted_message, -key)

crypted_message = cesar("Je recherche une Alternance", 13)
print(crypted_message)

def brute_force_cesar_cipher(crypted_message):
	for possible_key in range(0, len(alphabet)):
            
		print(cesar_uncipher(crypted_message, possible_key))
            
		print("_"*15)


brute_force_cesar_cipher(crypted_message)

print(cesar("coucou", 520))
