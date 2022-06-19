#!/usr/bin/env python3
"""
Blackjack game with simple rules.

This program:
1) creates new card deck
2) deals one card to player, one card to dealer <- repeat twice
3) checks if player or dealer has blackjack -> he wins;
   if both have -> hand ties
4) if no blackjack -> counts cards for player and dealer;
   if anybody achives 22 or higher -> he loses;
   if both -> game ties;
   if dealer achives 17 -> game ties
5) if player has 20 and less, he decides to "hit" (take another card)
   or "stand" (pass); if dealer has 16 and less, he have to "hit";
   further counts cards as in 4).
"""
import random

# Define winning constants
WIN_SCORE = 21
STAND_ON_SOFT = 17


def main():
    """Run main program."""
    # Show running titles
    print('Welcome to BLACKJACK game!')
    print('--------------------------')
    show_titles()

    print()
    print('---------------------------')
    print('Player_1, ready to start...')
    print()

    # Create hands for player and dealer
    player_hand = []
    dealer_hand = []

    # Create totals for player and dealer
    player_total = 0
    dealer_total = 0

    # Create flags if anybody exceeds 21
    player_exceed = False
    dealer_exceed = False

    # Create a new card deck
    card_deck = create_cards()

    # Deal first two cards and show hands
    # Deal cards:
    for card_number in range(1, 3):
        # for player
        print(f'Pocket card #{card_number} to you (Player_1).')
        new_card = deal_card(card_deck)
        player_hand.append(new_card)

        # for dealer
        print(f'Pocket card #{card_number} to dealer (Computer).')
        new_card = deal_card(card_deck)
        dealer_hand.append(new_card)

    # Show hands (first two cards)
    print()
    print('Your (Player_1) hand:')
    show_hand(player_hand)
    player_total = count_hand(player_hand)
    print(f'Your (Player_1) total: {player_total}')
    print()

    print('Dealer\'s (Computer) hand:')
    show_half_hand(dealer_hand)

    # Check if there is any BLACKJACK
    player_blackjack = check_blackjack(player_hand)
    dealer_blackjack = check_blackjack(dealer_hand)

    # If BLACKJACK, the game finishes
    if player_blackjack or dealer_blackjack:
        print()
        print('*************************')
        print('There is a BLACKJACK now!')
        print()

        print('Your (Player_1) hand:')
        show_hand(player_hand)
        print()
        print('Dealer\'s (Computer) hand:')
        show_hand(dealer_hand)

    if player_blackjack and dealer_blackjack:
        print()
        print('PUSH! Game ties (both BLACKJACKS).')
    elif player_blackjack:
        print()
        print('You (Player_1) have BLACKJACK and win. Congratulations!')
    elif dealer_blackjack:
        print()
        print('Sorry, dealer (Computer) have BLACKJACK, you lose the game.')
    else:
        # Continue the game
        # Player hits or stands
        while player_total < WIN_SCORE:
            print()
            print('You have to decide:')
            print('- take another card (HIT=1) or pass (STAND=0).')
            hit = check_choice()

            if hit == 1:
                another_card = deal_card(card_deck)
                player_hand.append(another_card)
                print()
                print('Additional card  to you (Player_1).')
                print('Your (Player_1) hand:')
                show_hand(player_hand)
                player_total = count_hand(player_hand)
                print(f'Your (Player_1) total: {player_total}')
            else:
                print(f'Your (Player_1) total: {player_total}')
                break

        # Open dealer's pocket hand
        print()
        print('Opening dealer\'s (Computer) hand.')
        print('Dealer\'s (Computer) hand:')
        show_hand(dealer_hand)
        dealer_total = count_hand(dealer_hand)
        print(f'Dealer\'s (Computer) total: {dealer_total}')

        # Dealer hits or stands
        if player_total <= WIN_SCORE:
            while dealer_total < STAND_ON_SOFT:
                print()
                print('Additional card to dealer (Computer).')
                another_card = deal_card(card_deck)
                dealer_hand.append(another_card)
                print('Dealer\'s (Computer) hand:')
                show_hand(dealer_hand)
                dealer_total = count_hand(dealer_hand)
                print(f'Dealer\'s (Computer) total: {dealer_total}')

        # Show totals and who wins the game
        print()
        print('********')
        print('Finally:')
        print(f'- Your (Player_1) total: {player_total}')
        print(f'- Dealer\'s (Computer) total: {dealer_total}')

        # Check if anybode exeeds 21
        if player_total > WIN_SCORE:
            player_exceed = True
        if dealer_total > WIN_SCORE:
            dealer_exceed = True

        # Print who wins or the game ties
        if player_total == dealer_total and player_total <= WIN_SCORE:
            print()
            print('PUSH! Game ties (equal totals).')
        elif player_exceed and dealer_exceed:
            print()
            print('Game ties (both exceed 21).')
        elif not player_exceed and dealer_exceed:
            print()
            print('Dealer (Computer) exceeds 21 and you (Player_1) win.')
            print('Congratulations!')
        elif player_exceed and not dealer_exceed:
            print()
            print('Sorry, dealer (Computer) wins,')
            print('you (Player_1) exceed 21 and lose the game.')
        elif player_total > dealer_total and check_s17(dealer_hand):
            print()
            print('Game ties - S17 rule, your (Player_1) total is higher,')
            print('but dealer (Computer) total is 17.')
        elif player_total > dealer_total and not check_s17(dealer_hand):
            print()
            print('You (Player_1) win. Congratulations!')
        elif dealer_total > player_total:
            print()
            print('Sorry, dealer (Computer) wins by higher total,')
            print('you (Player_1) lose the game.')

    # Show finishing titles
    print()
    print('---------------------------------------------')
    print('The game is over. Thanks for playing my game!')
    print('(c) Nobus, 2022')


def show_titles():
    """Print some game's rules."""
    print()
    print('You will play against the program (dealer).')
    print('The playing card deck consists of 52 cards:')
    print('- suits does not matter;')
    print('- 2, 3, 4, 5, 6, 7, 8, 9, 10 count as their numbers;')
    print('- J (Jack), Q (Queen), K (King) count as 10;')
    print('- A (Ace) counts as 11 if total is 21 or less (else counts as 1);')
    print('- if total of first two cards is 21 (10/J/Q/K + A),')
    print('  that hand wins as "BLACKJACK";')
    print('- if both hands are "BLACKJACKS", game ties ("PUSH");')
    print('- if total of player\'s cards is less than 21, he can choose:')
    print('  take another card("HIT") or pass ("STAND");')
    print('- if total of dealer\'s cards is less than 17,')
    print('  he takes another card and repeat this step while total exceeds')
    print('  17 or higher;')
    print('- if total of player or dealer exceeds 21, he loses')
    print('  (when both exceed 21, game ties);')
    print('- if totals of player and dealer are equal and less 22,')
    print('  game ties ("PUSH");')
    print('- hand (cards) that is higher than other but less 22, wins;')
    print('- but if dealer\'s hand is 17 (S17 = 6 + 1), and even that hand')
    print('  is less than player\'s one, game ties.')


def create_cards():
    """Create new card deck."""
    # Constants for card decks
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['clubs', 'diamonds', 'hearts', 'spades']
    VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]

    # Create list of cards (rank with value)
    cards = []

    for rank in RANKS:
        for suit in SUITS:
            cards.append(f'{rank} of {suit}')

    # Multiply values for all 52 cards
    values = []

    for value in VALUES:
        for cycle in range(4):
            values.append(value)

    # Create and return card deck - dict of tuples (card, value)
    return list(zip(cards, values))


def deal_card(card_deck):
    """Deal a card from the playing card deck."""
    return card_deck.pop(random.randrange(0, len(card_deck)))


def show_card(dealt_card):
    """Show popped card."""
    card, value = dealt_card
    print(f'{card}: {value=}')


def show_hand(hand):
    """Show player's/dealer's hand."""
    for index, card in enumerate(hand):
        print(f'{index+1}) {card[0]}')


def show_half_hand(hand):
    """Show one card from dealer's pocket hand."""
    print(f'1) {hand[0][0]}')
    print('2) Card is face down')


def count_hand(hand):
    """Count card's values in players/dealer's hand."""
    total = 0

    for card in hand:
        total += card[1]
        if total <= 11 and card[1] == 1:
            total += 10

    return total


def get_user_choice():
    """Input user's choice to hit or stand."""
    # Get and assert user's choice
    try:
        user_choice = int(input('>>> Enter your choice (1 or 0): '))
        assert user_choice in [0, 1]
    # If users's input is not 1 or 0 - return None
    except (AssertionError, ValueError):

        print('You should type 1 or 0 and then ENTER.')
        user_choice = None

    finally:
        return user_choice


def check_choice():
    """Get and check user's choice."""
    checked_choice = get_user_choice()

    # Re-enter user's input while it is not valid
    while checked_choice is None:
        checked_choice = get_user_choice()

    return checked_choice


def check_blackjack(hand):
    """Check if Blackjack."""
    return True if count_hand(hand) == WIN_SCORE else False


def check_s17(hand):
    """Check if S17 (stand-on-soft-17) for dealer."""
    return True if (count_hand(hand) == STAND_ON_SOFT and
                    len(hand) == 2 and
                    (hand[0][1] == 1 or hand[1][1] == 1)) else False


def check_exceeding(hand):
    """Check if anybody exceeds 21."""
    return True if count_hand(hand) > WIN_SCORE else False


if __name__ == '__main__':
    main()
