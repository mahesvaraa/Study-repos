# The Fruit Juice

https://www.codewars.com/kata/5264603df227072e6500006d

In this kata we mix some tasty fruit juice. We can add some components with certain amounts. Sometimes we pour out a bit
of our juice. Then we want to find out, which concentrations our fruit juice has.

**Example:**

* You take an empty jar for your juice
* Whenever the jar is empty, the concentrations are always 0
* Now you add 200 units of apple juice
* And then you add 200 units of banana juice
* Now the concentration of apple juice is 0.5 (50%)
* Then you pour out 200 units
* The concentration of apple juice is still 50%
* Then you add 200 units of apple juice again
* Now the concentration of apple juice is 0.75, while the concentration of banana juice is only 0.25 (300 units apple
  juice + 100 units banana juice)

Complete the functions in order to provide this functionality. The test code for the example above can be found in the
test fixture.

# Solution

```python
class Jar():
    def __init__(self):
        self.cup = {}
        self.volume = 0
        pass

    def add(self, amount, kind):
        self.cup.setdefault(kind, 0)
        self.cup[kind] += amount
        self.volume += amount

    def pour_out(self, amount):
        if self.volume >= amount:
            self.cup = {k: v * ((self.volume - amount) / self.volume) for k, v in self.cup.items()}
            self.volume -= amount
        else:
            self.volume = 0
            self.cup = {k: 0 for k, v in self.cup.items()}

    def get_total_amount(self):
        return self.volume

    def get_concentration(self, kind):
        return self.cup.get(kind, 0) / self.volume if self.volume != 0 else 0
```