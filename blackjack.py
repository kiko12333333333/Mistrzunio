import random
import os
import time


def load_account_balance():
    if os.path.exists('stan_konta.txt'):
        with open('stan_konta.txt', 'r') as file:
            return int(file.read())
    else:
        return 1000

def save_account_balance(balance):
    with open('stan_konta.txt', 'w') as file:
        file.write(str(balance))

def get_card_value(card):
    if card in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
        return int(card)
    elif card in ['J', 'Q', 'K']:
        return 10
    else:
        return 11

def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        value += get_card_value(card)
        if card == 'A':
            aces += 1
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

def play_blackjack():
    print("Witaj w grze Blackjack!")
    account_balance = load_account_balance()
    last_update_time = time.time()

    while True:
        if time.time() - last_update_time >= 5:
            account_balance += 20
            last_update_time = time.time()
            save_account_balance(account_balance)

        print(f"Stan konta: {account_balance} PLN")
        
        if account_balance < 50:
            print("Niewystarczająca ilość środków na koncie!")
            break
        
        choice = input("Czy chcesz zagrać? (tak/nie): ")
        if choice.lower() == 'nie':
            break
        
        account_balance -= 50
        save_account_balance(account_balance)
        
        deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        random.shuffle(deck)
        
        player_hand = []
        dealer_hand = []
        
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        
        print(f"Twoja ręka: {player_hand}")
        print(f"Karta krupiera: {dealer_hand[0]}")
        
        while True:
            choice = input("Czy chcesz dobrać kartę? (tak/nie): ")
            if choice.lower() == 'tak':
                player_hand.append(deck.pop())
                print(f"Twoja ręka: {player_hand}")
            else:
                break
            
            player_value = calculate_hand_value(player_hand)
            if player_value > 21:
                print("Przegrałeś!")
                break
        
        if player_value <= 21:
            dealer_value = calculate_hand_value(dealer_hand)
            while dealer_value < 17:
                dealer_hand.append(deck.pop())
                dealer_value = calculate_hand_value(dealer_hand)
            
            print(f"Ręka krupiera: {dealer_hand}")
            
            if dealer_value > 21 or player_value > dealer_value:
                print("Wygrałeś!")
                account_balance += 100
            elif player_value == dealer_value:
                print("Remis!")
                account_balance += 50
            else:
                print("Przegrałeś!")
        
        save_account_balance(account_balance)
        time.sleep(2)


play_blackjack()