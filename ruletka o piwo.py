import random
import time
import os


rewards = ['2 piwa', '5 piw', 'Nic', '1 piwo', 'Jackpot 🍾', '3 piwa', 'Nic', '10 piw']

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def spin_wheel():
    positions = len(rewards)
    
    current_position = random.randint(0, positions - 1)
    
    spins = random.randint(10, 20)
    
    for _ in range(spins):
        clear_screen()
        
        
        print("╔═══════════════════════════╗")
        print("║          RULETKA          ║")
        print("╚═══════════════════════════╝")
        print(f"\nKoło się kręci... ({rewards[current_position]})")
        time.sleep(0.2)
        
        
        current_position = (current_position + 1) % positions
    
    return rewards[current_position]

def play_roulette():
    balance = 100
    cost_per_spin = 10

    print("Welcome to the Casino Roulette!")
    
    while balance >= cost_per_spin:
        input("\nPress Enter to spin the wheel...")
        balance -= cost_per_spin
        
        reward = spin_wheel()
        
        if reward == "Nic":
            print("\n🙁 Nic nie wygrałeś ale piwko to zawsze coś. Spróbuj ponownie!")
        elif reward == "Jackpot 🍾":
            balance += 50
            print(f"\n🎉 Wygrałeś JACKPOT! Twoje nowe saldo: {balance}")
        else:
            print(f"\n🎉 Wygrałeś: {reward}! Twoje saldo: {balance}")
        
        if balance < cost_per_spin:
            print("\nNie masz wystarczającej ilości pieniędzy, aby kontynuować. Koniec gry.")
            break

if __name__ == "__main__":
    play_roulette()
