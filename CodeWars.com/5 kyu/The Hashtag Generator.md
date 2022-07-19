# The Hashtag Generator

https://www.codewars.com/kata/52449b062fb80683ec000024

The marketing team is spending way too much time typing in hashtags.

Let's help them with our own Hashtag Generator!

**Here's the deal:**

* It must start with a hashtag (#).
* All words must have their first letter capitalized.
* If the final result is longer than 140 chars it must return false.
* If the input or the result is an empty string it must return false.

**Examples**

```python

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
```

# Solution

```python
def generate_hashtag(s):
    return '#' + "".join(list(map(lambda x: x.capitalize(), s.split()))) if 0 < len(s) < 140 else False
```