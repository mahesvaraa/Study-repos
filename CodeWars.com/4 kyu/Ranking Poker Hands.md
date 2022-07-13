# Ranking Poker Hands

https://www.codewars.com/kata/5739174624fc28e188000465

A famous casino is suddenly faced with a sharp decline of their revenues. They decide to offer Texas hold'em also
online. Can you help them by writing an algorithm that can rank poker hands?

**Task**
Create a poker hand that has a method to compare itself to another poker hand:

```python
compare_with(self, other_hand)
```

A poker hand has a constructor that accepts a string containing 5 cards:

```
PokerHand("KS 2H 5C JD TD")
```

The characteristics of the string of cards are:

* Each card consists of two characters, where
* The first character is the value of the card: 2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
* The second character represents the suit: S(pades), H(earts), D(iamonds), C(lubs)
* A space is used as card separator between cards

The result of your poker hand compare can be one of these 3 options:

```
[ "Win", "Tie", "Loss" ]
```

**Notes**

* Apply the Texas Hold'em rules for ranking the cards.
* Low aces are NOT valid in this kata.
* There is no ranking for the suits.
* If you finished this kata, you might want to continue with Sortable Poker Hands

# Solution

```python
from itertools import combinations_with_replacement
from collections import Counter

nums_order      = '23456789TJQKA'
nums_rev_order  = nums_order[::-1]
FULL_COMBO      = filter(lambda x: len(set(x)) != 1, combinations_with_replacement(nums_order, 5))
ALL_COMBO       = list(dict.fromkeys(map(lambda x: ''.join(sorted(x, key=nums_order[::-1].index)), FULL_COMBO)))
ALL_COMBO       = sorted(ALL_COMBO, key=lambda x: list(map(lambda y: nums_order.index(y), x)))
HIGH_CARD       = list(filter(lambda x: len(set(x)) == 5 and x not in nums_rev_order and x != 'A5432', ALL_COMBO))
PAIRS           = list(filter(lambda x: len(set(x)) == 4 and 2 in dict(Counter(x)).values(), ALL_COMBO))
TWO_PAIRS       = list(filter(lambda x: len(set(x)) == 3 and 2 in dict(Counter(x)).values(), ALL_COMBO))
THREE_OF_A_KIND = list(filter(lambda x: len(set(x)) == 3 and 3 in dict(Counter(x)).values(), ALL_COMBO))
STRAIGHT        = ['A5432'] + list(filter(lambda x: ''.join(x) in nums_rev_order, ALL_COMBO))
FLUSH           = HIGH_CARD + TWO_PAIRS + THREE_OF_A_KIND + STRAIGHT
FULL_HOUSE      = list(filter(lambda x: len(set(x)) == 2 and 3 in dict(Counter(x)).values(), ALL_COMBO))
FOUR_A_KIND     = sorted(filter(lambda x: len(set(x)) == 2 and 4 in dict(Counter(x)).values(), ALL_COMBO),
                     key=lambda x: nums_order.index(x[3]))
STRAIGHT_FLUSH  = STRAIGHT.copy()
FLUSH_ROYAL     = ['TJQKA']


class PokerHand:
    def __init__(self, hand):
        self.hand = hand.split()
        self.flush = len(set(map(lambda x: x[1], self.hand))) == 1
        self.values = ''.join(sorted(map(lambda x: x[0], self.hand), key=nums_order[::-1].index))
        self.results = {
            'HIGH_CARD': self.values in HIGH_CARD and not self.flush,
            'PAIRS': self.values in PAIRS,
            'TWO_PAIRS': self.values in TWO_PAIRS,
            'THREE_OF_A_KIND': self.values in THREE_OF_A_KIND,
            'STRAIGHT': self.values in STRAIGHT and not self.flush,
            'FLUSH': any(
                [self.values in PAIRS,
                 self.values in HIGH_CARD,
                 self.values in TWO_PAIRS,
                 self.values in THREE_OF_A_KIND]
            ) and self.flush,
            'FULL_HOUSE': self.values in FULL_HOUSE,
            'FOUR_A_KIND': self.values in FOUR_A_KIND,
            'STRAIGHT_FLUSH': self.values in STRAIGHT and self.flush,
            'FLUSH_ROYAL': self.values == 'TJQKA' and self.flush
        }
        self.order = list(self.results.keys())

    def compare_with(self, other):
        if self.order.index(list(filter(lambda x: self.results[x], self.results))[0]) < self.order.index(
                list(filter(lambda x: other.results[x] is True, other.results))[0]):
            return 'Loss'
        elif self.order.index(list(filter(lambda x: self.results[x], self.results))[0]) > self.order.index(
                list(filter(lambda x: other.results[x] is True, other.results))[0]):
            return 'Win'
        else:
            if self.values == other.values:
                return 'Tie'
            else:
                arr = eval(list(filter(lambda x: self.results[x], self.results))[0])
                return 'Loss' if arr.index(self.values) < arr.index(other.values) else 'Win'
```