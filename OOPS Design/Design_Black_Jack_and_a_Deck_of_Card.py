class Suit:
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
