"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in 'JQK':
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    if v1 == v2:
        return (card_one, card_two)
    elif v1 > v2:
        return card_one
    else:
        return card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    # When deciding the value of an upcoming ace, any existing Ace in the
    # hand is counted as 11 (per exercise rules). Use 11 for existing 'A'
    # cards when computing whether adding an 11-valued ace would bust.
    val1 = 11 if card_one == 'A' else value_of_card(card_one)
    val2 = 11 if card_two == 'A' else value_of_card(card_two)
    total = val1 + val2
    return 1 if (total + 11) > 21 else 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    # A blackjack (natural) is an Ace plus any 10-point card.
    ten_value = 10
    return ((card_one == 'A' and value_of_card(card_two) == ten_value) or
            (card_two == 'A' and value_of_card(card_one) == ten_value))


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    # Special case for Aces
    if card_one == 'A' and card_two == 'A':
        return True
    # For non-Ace cards, compare their values
    if card_one != 'A' and card_two != 'A':
        return value_of_card(card_one) == value_of_card(card_two)
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]


