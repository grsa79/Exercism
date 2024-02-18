"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return [number, number+1, number+2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    # easy fix: return rounds_1 + rounds_2 - but I'm in the mood for some for's ;)
    new_list = []
    for round_no in rounds_1:
        new_list.append(round_no)
    
    for round_no in rounds_2:
        new_list.append(round_no)

    return new_list


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    for round_no in rounds:
        if round_no == number:
            return True
        
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    cards_sum = sum(hand)
    cards_count = len(hand)
    
    if cards_sum != 0:
        return cards_sum / cards_count
    return 0


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    average = card_average(hand)
    if (get_median(hand) == average or card_average([hand[0], hand[-1]]) == average):
        return True
    
    return False
    

def get_median(hand):
    """
    function to determine the median (=middle card) of a (sorted) set of odd cards.
    """
    return hand[len(hand)//2]

def check_even(number):
    if number % 2 == 0: 
        return True
    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    odd_hand = []
    even_hand = []
    for card_no, card_value in enumerate(hand):
        #print(type(card_no))
        if check_even(card_no+1):
            even_hand.append(card_value)
        else:
            odd_hand.append(card_value)

    if card_average(even_hand) == card_average(odd_hand):
        return True
    return False
    

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    new_hand = []
    for card in hand[:-1]:
        new_hand.append(card)

    if hand[-1] == 11:
        new_hand.append(22)
    else:
        new_hand.append(hand[-1])

    return new_hand
    
