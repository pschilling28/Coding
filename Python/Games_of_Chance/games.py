import random

money = 100

#Write your game of chance functions here
def play_coin_flip(call, bet):
    global money
    num = random.randint(1, 2)
    print("The call is %s. Flipping..." % call)
    if bet <= 0:
        return "Bet must be positive."
    elif bet > money:
        return "You cannot bet more than you have."
    else:
        if call.lower() == "heads":
            if num == 1:
                money += bet
                return "The coin shows heads, you win $%i. You now have $%i." % (bet, money)
            else:
                money -= bet
                return "The coin shows tails. You lose $%i. You now have $%i." % (bet, money)
        elif call.lower() == "tails":
            if num == 2:
                money += bet
                return "The coin shows heads, you win $%i. You now have $%i." % (bet, money) 
            else:
                money -= bet
                return "The coin shows tails. You lose $%i. You now have $%i." % (bet, money)
        else:
            return "You entered an incorrect call. Please choose heads or tails."

def play_cho_han(call, bet):
    global money
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("The call is %s. Rolling dice..." % call)
    if bet <= 0:
        return "Bet must be positive."
    elif bet > money:
        return "You cannot bet more than you have."
    else:
        if call.lower() == "odd":
            if (die1 + die2) % 2 == 0:
                money -= bet
                return "The dice show %i and %i, adding to %i - even. You lose $%i. You now have $%i." % (die1, die2, (die1 + die2), bet, money)
            else:
                money += bet
                return "The dice show %i and %i, adding to %i - odd. You win $%i. You now have $%i." % (die1, die2, (die1 + die2), bet, money)
        elif call.lower() == "even":
            if (die1 + die2) % 2 == 1:
                money -= bet
                return "The dice show %i and %i, adding to %i - odd. You lose $%i. You now have $%i." % (die1, die2, (die1 + die2), bet, money)
            else:
                money += bet
                return "The dice show %i and %i, adding to %i - even. You win $%i. You now have $%i." % (die1, die2, (die1 + die2), bet, money)
        else:
            return "You entered an incorrect call. Please choose odd or even."

def play_war(bet):
    global money
    deck_of_cards = {13: ("Ace", 13), 1: (2, 1), 2: (3, 2), 3: (4, 3), 4: (5, 4), 5: (6, 5), 6: (7, 6), 7: (8, 7), 8: (9, 8), 9: (10, 9), 10: ("Jack", 10), 11: ("Queen", 11), 12: ("King", 12)}
    card1 = deck_of_cards[random.randint(1, 13)]
    card2 = deck_of_cards[random.randint(1, 13)]
    if bet <= 0:
        return "Bet must be positive."
    elif bet > money:
        return "You cannot bet more than you have."
    else:
        if card1[1]> card2[1]:
            money += bet
            return "You drew a(n) %s and your opponent drew a(n) %s. You win $%i. You now have $%i." % (card1[0], card2[0], bet, money)
        elif card1[1] < card2[1]:
            money -= bet
            return "You drew a(n) %s and your opponent drew a(n) %s. You lose $%i. You now have $%i." % (card1[0], card2[0], bet, money)
        else:
            return "You drew a(n) %s and your opponent drew a(n) %s. The result is push. Your bet of $%s has been returned to you. You still have %s" % (card1[0], card2[0], bet, money)

def build_wheel():
    wheel = {}
    for i in range(0, 38):
        wheel[i + 1] = [i + 1, ""]
    def make_black(*args):
        for arg in args:
            wheel[arg][1] = "black"
    def make_red(*args):
        for arg in args:
            wheel[arg][1] = "red"
    make_black(2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)
    make_red(1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
    wheel[37] = [0, "green"]
    wheel[38] = ["00", "green"]
    return wheel

def play_roulette(*bets_calls):
    global money
    wheel = build_wheel()
    spin = wheel[random.randint(1, 36)]
    winnings = 0
    total_bet = 0
    print("The wheel lands on %s." % spin[0])
    print("You made the following bets:")
    for bet, call in bets_calls:
        total_bet += bet
        if bet <= 0:
            return "Bet must be positive."
        elif total_bet > money:
            return "You cannot bet more than you have."
        else:
            print("$%i on %s." % (bet, call))
            winnings -= bet
            # space win
            if call == spin[0]:
                winnings += (bet * 36)
                print("Call of %s pays out %i." % (call, (bet * 35)))
            if spin[0] != "00" and spin[0] != 0:
                # color win
                if call.lower() == spin[1]:
                    winnings += bet * 2
                    print("Call of %s pays out $%i." % (call, bet))
                #column wins
                elif call.lower() == "c1" and spin[0] % 3 == 1:
                    winnings += bet * 3
                    print("Call of %s pays out $%i." % (call, (bet * 2)))
                elif call.lower() == "c2" and spin[0] % 3 == 2:
                    winnings += bet * 3
                    print("Call of %s pays out $%i." % (call, (bet * 2)))
                elif call.lower() == "c3" and spin[0] % 3 == 0:
                    winnings += bet * 3
                    print("Call of %s pays out $%i." % (call, (bet * 2)))
                # even/odd wins
                elif call.lower() == "odd" and spin[0] % 2 == 0:
                    winnings += bet * 2
                    print("Call of %s pays out $%i." % (call, bet))
                elif call.lower() == "even" and spin[0] % 2 == 0:
                    winnings += bet * 2
                    print("Call of %s pays out $%i." % (call, bet))
                # low/high wins
                elif call.lower() == "low" and spin[0] >= 1 and spin[0] <= 18:
                    winnings += bet * 2
                    print("Call of %s pays out $%i." % (call, bet))
                elif call.lower() == "high" and spin[0] >= 19 and spin[0] <= 36:
                    winnings += bet * 2
                    print("Call of %s pays out $$%i." % (call, bet))
                # dozen wins
                elif call.lower() == "1st12" and spin[0] >= 1 and spin[0] <= 12:
                    winnings += bet * 3
                    print("Call of %s pays out $%i." % (call, bet * 2))
                elif call.lower() == "2nd12" and spin[0] >= 13 and spin[0] <= 24:
                    winnings += bet * 3
                    print("Call of %s pays out $%i." % (call, bet * 2))
                elif call.lower() == "3rd12" and spin[0] >= 25 and spin[0] <= 36:
                    winnings += bet * 3
                    print("Call of %s pays out $%i." % (call, bet * 2))
    money += winnings
    return "Your bet(s) netted you $%i. You now have $%i" % (winnings, money)
                
#Call your game of chance functions here
#coin_flip = play_coin_flip("heads", 50)
#print(coin_flip)
cho_han = play_cho_han("even", 100)
print(cho_han)
#war = play_war(10)
#print(war)
#roulette = play_roulette((100, "00"))
#print(roulette)