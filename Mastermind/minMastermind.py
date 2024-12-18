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

def get_secret_number(player_num):
    while True:
        secret = input(f"Player {player_num}, entrer votre numéro secret à 4 chiffres: ")
        if secret.isdigit():
            return secret
        else:
            print("Entrée invalide. Veuillez saisir des chiffrés.")

def main():
    print("Welcome to the Mastermind game!")
    
    while True:
        secret1 = get_secret_number(1)
    
        print("Player 2, A vous de commencez à deviner le numéro du joueur 1.")
        attempts_player2 = player_turn(2, secret1)
    
        secret2 = get_secret_number(2)
    
        print("Player 1, commencez à deviner le numéro du joueur 2.")
        attempts_player1 = player_turn(1, secret2)
    

        attempts_player1 = player_turn(1, secret1)
        attempts_player2 = player_turn(2, secret2)
    
        if attempts_player1 < attempts_player2:
             print("Player 1 gagne et est couronné Mastermind!")
        elif attempts_player2 < attempts_player1:
             print("Player 2 gagne et est couronné Mastermind!")
        else:
             print("C'est une égalité!")
        
        play_again = input("Voulez-vous jouer un autre tour? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()