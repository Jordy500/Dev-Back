import random

def generate_hint(secret, guess):
       hint = ""
       correct_position = sum(s == g for s, g in zip(secret, guess))
       correct_number = sum(min(secret.count(n), guess.count(n)) for n in set(guess)) - correct_position
       
       hint += "*" * correct_position + "-" * correct_number
       return hint

def validate_numbers(guess):
       return guess.isdigit() and len(guess) == 4

def player_turn(player_num, secret, max_attempts=5):
       attempts = 0
       while attempts < max_attempts:
           guess = input(f"Player {player_num}, entrez votre supposition: ")
           if not validate_numbers(guess):
               print("Entrée invalide. Veuillez saisir 4 chiffres.")
               continue
           
           attempts += 1
           
           if guess == secret:
               print(f"Player {player_num} a deviné la combinaison de chiffres dans {attempts} tentatives!")
               return attempts
           else:
               hint = generate_hint(secret, guess)
               print(f"veuillez donner un indice: {hint}")
       
       print(f"Player {player_num} je n'ai pas trouvé la combinaison de chiffres après {max_attempts} tentatives.")
       print(f"Perdu la combinaison de numéros secrets était: {secret}")
       return max_attempts