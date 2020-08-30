import random
from abc import ABC
from enum import Enum


class Suit(Enum):
    HEART, SPADE, CLUB, DIAMOND = 1, 2, 3, 4


class Card:
    def __init__(self, suit, face_value):
        self.__suit = suit
        self.__face_value = face_value

    def getSuit(self):
        return self.__suit

    def getFaceValue(self):
        return self.__face_value


class BlackJackCard(Card):
    def __init__(self, suit, face_value):
        super().__init__(suit, face_value)
        self.__game_value = face_value

        if self.__game_value > 10:
            self.__game_value = 10

    def getGameValue(self):
        return self.__game_value


class Deck:
    def __init__(self):
        self.__cards = []

        for value in range(1, 14):
            for suit in Suit:
                self.__cards.append(BlackJackCard(value, suit))

    def getCards(self):
        return self.__cards


class Shoe:
    def __init__(self, number_of_decks):
        self.__number_of__decks = number_of_decks
        self.__cards = []

    def create_shoe(self):
        for deck in range(self.__number_of__decks):
            for card in Deck().getCards():
                self.__cards.append(card)

    def shuffel(self):
        cards_size = len(self.__cards)
        for i in range(cards_size):
            j = random.randrange(0, cards_size - i - 1, 1)
            self.__cards[i], self.__cards[j] = self.__cards[j], self.__cards[i]

    def dealCard(self):
        if len(self.__cards) == 0:
            self.create_shoe()
        return self.__cards.pop(0)


class Hand:
    def __init__(self, black_jack_card_1, black_jack_card_2):
        self.__cards = [black_jack_card_1, black_jack_card_2]

    def getScore(self):

        total = [0]
        for card in self.__cards:
            new_total = []
            for score in total:
                new_total.append(score + card.getGameValue())
                if card.getGameValue() == 1:
                    new_total.append(score + 11)
            total = new_total

        return total

    def addCard(self, new_card):
        self.__cards.append(new_card)

    def resolve_score(self):
        scores = self.getScore()
        best_score = 0

        for score in scores:
            if score <= 21 and score > best_score:
                best_score = score

        return best_score


class BasePlayer(ABC):
    def __init__(self, id, balance, status):
        self.__id = id
        self.__balance = balance
        self.__status = status
        self.__hands = []

    def getHands(self):
        return self.__hands

    def getBalance(self):
        return self.__balance

    def addHands(self, hand):
        self.__hands.append(hand)

    def removeHand(self, hand):
        self.__hands.pop(hand)


class Player(BasePlayer):

    def __init__(self, id, balance, status):
        super().__init__(id, balance, status)
        self.__bet = 0
        self.__total_cash = 0


class Dealer(BasePlayer):
    def __init__(self, id, balance, status):
        super().__init__(id, balance, status)


class Game:
    def __init__(self, player, dealer):
        self.__player = player
        self.__dealer = dealer
        self.__max_deck_size = 3
        self.__shoe = Shoe(self.__max_deck_size)

    def playAction(self, action, hand):
        switcher = {
            "split": self.split(hand),
            "hit": self.hit(hand),
            "stand": self.stand(hand)
        }
        switcher.get(action, "Invalid Move")

    def split(self, hand):
        cards = hand.getCards()
        self.__player.addHands(Hand(cards[0], self.__shoe.dealCard()))
        self.__player.addHands(Hand(cards[1], self.__shoe.dealCard()))
        self.__player.removeHand(hand)

    def hit(self, hand):
        hand.addCard(self.__shoe.dealCard())

    def stand(self, hand):
        pass

    def start(self):
        player_hands = Hand(self.__shoe.dealCard(), self.__shoe.dealCard())
        self.__player.addHands(player_hands)

        dealer_hands = Hand(self.__shoe.dealCard(), self.__shoe.dealCard())
        self.__dealer.addHands(dealer_hands)
