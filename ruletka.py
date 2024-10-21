import random
import time
import os


wheel = {
    0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red', 8: 'black', 9: 'red',
    10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black', 16: 'red', 17: 'black', 18: 'red',
    19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red', 24: 'black', 25: 'red', 26: 'black', 27: 'red',
    28: 'black', 29: 'black', 30: 'red', 31: 'black', 32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def spin_wheel():
    numbers = list(wheel.keys())
    current_position = random.randint(0, len(numbers) - 1)
    spins = random.randint(10, 20) 
    
    for _ in range(spins):
        clear_screen()
        print("Spinning the roulette wheel...\n")
        print("═══════════════════════════════════════════════════")
        
        
        for i in range(current_position, current_position + 15):
            position = numbers[i % len(numbers)]
            color = wheel[position]
            if color == 'red':
                color_display = "\033[31m"  
            elif color == 'black':
                color_display = "\033[30m"  
            else:
                color_display = "\033[32m"  

            print(f"{color_display}{position:^3}\033[0m", end=" ")

        print("\n═══════════════════════════════════════════════════")
        time.sleep(0.2)
        
        current_position = (current_position + 1) % len(numbers)
    
    return numbers[current_position]

def place_bet():
    while True:
        try:
            bet_number = int(input("\nPostaw zakład na numer (0-36): "))
            if 0 <= bet_number <= 36:
                break
            else:
                print("Wprowadź liczbę w przedziale 0-36.")
        except ValueError:
            print("Nieprawidłowy numer, spróbuj ponownie.")
    
    bet_color = input("Postaw zakład na kolor (red/black/green): ").lower()
    if bet_color not in ['red', 'black', 'green']:
        bet_color = 'none'  
    
    return bet_number, bet_color

def play_roulette():
    balance = 100
    cost_per_spin = 10
    winnings = 0

    print("Welcome to the Casino Roulette!")

    while balance >= cost_per_spin:
        print(f"\nTwoje saldo: {balance}")
        input("\nPress Enter to spin the wheel...")

        balance -= cost_per_spin
        bet_number, bet_color = place_bet()

        winning_number = spin_wheel()
        winning_color = wheel[winning_number]

        print(f"\n🎉 Wylosowany numer: {winning_number}, kolor: {winning_color}")

       
        if bet_number == winning_number:
            print(f"🎉 Trafiłeś numer! Wygrywasz 50 jednostek.")
            winnings = 50
        elif bet_color == winning_color:
            print(f"🎉 Trafiłeś kolor! Wygrywasz 20 jednostek.")
            winnings = 20
        else:
            print("🙁 Niestety, nie wygrałeś.")
        
        balance += winnings
        winnings = 0  

        if balance < cost_per_spin:
            print("\nNie masz wystarczającego balansu, aby kontynuować. Koniec gry.")
            break

if __name__ == "__main__":
    play_roulette()
