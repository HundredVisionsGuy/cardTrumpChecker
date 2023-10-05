import cardTrumpChecker


def test_cardTrumpCheckerForLowNumHighColor():
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 5, 'yellow'),
                                               ('card2', 7, 'green'))
    expected = "card2"
    assert result == expected


def test_cardTrumpCheckerForSameNumHighColor():
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 5, 'red'),
                                               ('card2', 5, 'yellow'))
    expected = "card1"
    assert result == expected


def test_cardTrumpCheckerForSameNumLowColor():
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 10, 'green'),
                                               ('card2', 10, 'yellow'))
    expected = "card2"
    assert result == expected


def test_cardTrumpCheckerForHigherNumLowColor():
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 2, 'green'),
                                               ('card2', 1, 'red'))
    expected = "card1"
    assert result == expected


def test_cardTrumpCheckerForSameCardSameColor():
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 10, 'red'),
                                               ('card2', 10, 'red'))
    expected = "card1"
    assert result == expected


def test_cardTrumpCheckerForLowColor_LowNum():
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 3, 'green'),
                                               ('card2', 4, 'red'))
    expected = "card2"
    assert result == expected


def test_cardTrumpCheckerForHighNum_HighColor():
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 9, 'red'),
                                               ('card2', 7, 'green'))
    expected = "card1"
    assert result == expected


def test_cardTrumpCheckerForHighNum_HighColor_2():
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card1', 10, 'red'),
                                               ('card2', 7, 'green'))
    expected = "card1"
    assert result == expected


def test_cardTrumpCheckerForGreenOverRed():
    # Capture the results of the function
    result = cardTrumpChecker.cardTrumpChecker(('card2', 7, 'red'),
                                               ('card1', 8, 'green')
                                               )
    expected = "card2"
    assert result == expected
