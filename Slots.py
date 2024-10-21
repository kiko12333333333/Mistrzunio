import random
import time
import os

symbols = ['🍒', '🍋', '🍉', '🍇', '7️⃣', '⭐', '🍊', '💎']

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def spin_reel():
    for _ in range(10):
        reel_1 = random.choice(symbols)
        reel_2 = random.choice(symbols)
        reel_3 = random.choice(symbols)
        clear_screen()

        print("╔═════════════╦═════════════╦═════════════╗")
        print(f"║     {reel_1:^3}     ║     {reel_2:^3}     ║     {reel_3:^3}     ║")
        print("╚═════════════╩═════════════╩═════════════╝")

        time.sleep(0.2)
    return [reel_1, reel_2, reel_3]

def check_win(reels, win_chance):
    if random.randint(1, 100) <= win_chance:
        return True
    return False

def play_slot_machine():
    balance = 100
    cost_per_spin = 10
    winnings = 50

    print("Welcome to the Fruit Slot Machine!")
    
    # Pytanie o ustawienie procentu wygranych
    set_win_chance = input("Czy chcesz ustawić procenty wygranych? (tak/nie): ").lower()
    if set_win_chance == 'tak':
        win_chance = int(input("Ustaw procent wygranej (1-100): "))
    else:
        win_chance = 30  # Domyślna wartość procentu wygranej
    
    while balance >= cost_per_spin:
        input("\nPress Enter to spin...")
        balance -= cost_per_spin
        reels = spin_reel()
        
        if check_win(reels, win_chance):
            balance += winnings
            print("\n🍀🍀 You win! 🍀🍀 New balance:", balance)
        else:
            print("\nNo match. Better luck next time! Balance:", balance)
        
        if balance < cost_per_spin:
            print("\nNot enough balance to continue. Game over.")
            break

if __name__ == "__main__":
    play_slot_machine()
