import random
import time
import os


wheel_fortune = ['100 zł', '200 zł', '500 zł', 'Nic', '50 zł', 'Podwójna nagroda!', '1000 zł', 'Nic', 'Jackpot: 5000 zł']

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def spin_fortune_wheel():
    positions = len(wheel_fortune)
    
    current_position = random.randint(0, positions - 1)
    
    spins = random.randint(10, 20)
    
    for _ in range(spins):
        clear_screen()
        print("╔═══════════════════════════╗")
        print("║        KOŁO FORTUNY       ║")
        print("╚═══════════════════════════╝")
        print(f"\nKoło się kręci... ({wheel_fortune[current_position]})")
        
        
        current_position = (current_position + 1) % positions
        
        time.sleep(0.2)
    
    return wheel_fortune[current_position]

def play_fortune_game():
    print("Witaj w grze Koło Fortuny!")
    balance = 100  
    
    while True:
        print(f"\nTwój balans: {balance} zł")
        input("\nNaciśnij Enter, aby zakręcić kołem...")
        
        prize = spin_fortune_wheel()
        print(f"\n🎉 Koło zatrzymało się na: {prize} 🎉")
        
        if prize == "Nic":
            print("🙁 Niestety, nie wygrałeś nic tym razem.")
        elif prize == "Podwójna nagroda!":
            double_prize = spin_fortune_wheel()
            print(f"🎉 Wygrałeś podwójnie: {double_prize} 🎉")
            if double_prize != "Nic":
                amount = int(double_prize.split()[0])
                balance += amount * 2
        elif "zł" in prize:
            amount = int(prize.split()[0])
            balance += amount
        elif "Jackpot" in prize:
            balance += 5000
            print("🎉🎉 JACKPOT! Wygrałeś 5000 zł! 🎉🎉")
        
        
        play_again = input("\nCzy chcesz zagrać ponownie? (tak/nie): ").lower()
        if play_again != 'tak':
            print(f"\nDziękujemy za grę! Twój końcowy balans to: {balance} zł")
            break

if __name__ == "__main__":
    play_fortune_game()
