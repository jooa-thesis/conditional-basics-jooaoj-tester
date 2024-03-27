import random

from main import evenOrOdd

evens = []
odds = []

def generateNums():
    for i in range(512):
        num = random.randint(0, 255)
        evens.append(num) if (num % 2 == 0) else odds.append(num)
generateNums()

def test_evenOrOdd(monkeypatch):
    # Test 1 - even
    num = 2
    test = str(num) + " is " + str(evenOrOdd(num))
    assert test == str(num) + " is even"

    # Test 2 - odd
    num = 1
    test = str(num) + " is " + str(evenOrOdd(num))
    assert test == str(num) + " is odd"

    # Test 3 - random even
    num = random.choice(evens)
    test = str(num) + " is " + str(evenOrOdd(num))
    assert test == str(num) + " is even"

    # Test 4 - random odd
    num = random.choice(odds)
    test = str(num) + " is " + str(evenOrOdd(num))
    assert test == str(num) + " is odd"
