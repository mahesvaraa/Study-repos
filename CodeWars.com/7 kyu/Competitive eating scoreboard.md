# Competitive eating scoreboard

https://www.codewars.com/kata/571d2e9eeed4a150d30011e7

You are the judge at a competitive eating competition and you need to choose a winner!

There are three foods at the competition and each type of food is worth a different amount of points. Points are as
follows:

* Chickenwings: 5 points

* Hamburgers: 3 points

* Hotdogs: 2 points

Write a function that helps you create a scoreboard. It takes as a parameter a list of objects representing the
participants, for example:

```python
[
  {name: "Habanero Hillary", chickenwings: 5 , hamburgers: 17, hotdogs: 11},
  {name: "Big Bob" , chickenwings: 20, hamburgers: 4, hotdogs: 11}
]
```

It should return "name" and "score" properties sorted by score; if scores are equals, sort alphabetically by name.

```python
[
  {name: "Big Bob", score: 134},
  {name: "Habanero Hillary", score: 98}
]
```

# Solution

```python
def scoreboard(who_ate_what):
    res = []
    score = {"chickenwings": 5, "hamburgers": 3, "hotdogs": 2}
    for obj in who_ate_what:
        res.append({'name':obj['name'], 'score': sum([v*score[k] for k, v in obj.items() if score.get(k, False)])})
    return sorted(res, key=lambda x: (-x['score'], x['name']))
```