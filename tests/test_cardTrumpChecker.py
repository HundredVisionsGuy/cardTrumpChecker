import cardTrumpChecker


def test_cardTrumpCheckerForLowNumHighColor(self):
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 5, 'yellow'),
                                               ('card2', 7, 'green'))
    expected = "card2"
    assert result == expected


def test_cardTrumpCheckerForSameNumHighColor(self):
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 5, 'red'),
                                               ('card2', 5, 'yellow'))
    expected = "card1"
    assert result == expected


def test_cardTrumpCheckerForSameNumLowColor(self):
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 10, 'green'),
                                               ('card2', 10, 'yellow'))
    expected = "card2"
    assert result == expected


def test_cardTrumpCheckerForHigherNumLowColor(self):
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 2, 'green'),
                                               ('card2', 1, 'red'))
    expected = "card1"
    assert result == expected


def test_cardTrumpCheckerForSameCardSameColor(self):
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 10, 'red'),
                                               ('card2', 10, 'red'))
    expected = "card1"
    assert result == expected


def test_cardTrumpCheckerForLowColor_LowNum(self):
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 3, 'green'),
                                               ('card2', 4, 'red'))
    expected = "card2"
    assert result == expected


def test_cardTrumpCheckerForHighNum_HighColor(self):
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 9, 'red'),
                                               ('card2', 7, 'green'))
    expected = "card1"
    assert result == expected


def test_cardTrumpCheckerForHighNum_HighColor_2(self):
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 10, 'red'),
                                               ('card2', 7, 'green'))
    expected = "card1"
    assert result == expected
