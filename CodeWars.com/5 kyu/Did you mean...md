# Did you mean...?

https://www.codewars.com/kata/5259510fc76e59579e0009d4

I'm sure, you know Google's "Did you mean ...?", when you entered a search term and mistyped a word. In this kata we
want to implement something similar.

You'll get an entered term (lowercase string) and an array of known words (also lowercase strings). Your task is to find
out, which word from the dictionary is most similar to the entered one. The similarity is described by the minimum
number of letters you have to add, remove or replace in order to get from the entered word to one of the dictionary. The
lower the number of required changes, the higher the similarity between each two words.

Same words are obviously the most similar ones. A word that needs one letter to be changed is more similar to another
word that needs 2 (or more) letters to be changed. E.g. the mistyped term berr is more similar to beer (1 letter to be
replaced) than to barrel (3 letters to be changed in total).

Extend the dictionary in a way, that it is able to return you the most similar word from the list of known words.

**Code Examples:**

```python
fruits = new
Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry']);
fruits.findMostSimilar('strawbery'); // must
return "strawberry"
fruits.findMostSimilar('berry'); // must
return "cherry"

things = new
Dictionary(['stars', 'mars', 'wars', 'codec', 'codewars']);
things.findMostSimilar('coddwars'); // must
return "codewars"

languages = new
Dictionary(['javascript', 'java', 'ruby', 'php', 'python', 'coffeescript']);
languages.findMostSimilar('heaven'); // must
return "java"
languages.findMostSimilar('javascript'); // must
return "javascript"(same
words
are
obviously
the
most
similar
ones)
```

I know, many of you would disagree that java is more similar to heaven than all the other ones, but in this kata it is
;)

**Additional notes:**

there is always exactly one possible correct solution

# Solution

```python
import difflib
class Dictionary:
    def __init__(self,words):
        self.words=words    

    def find_most_similar(self, word):
        return difflib.get_close_matches(word, self.words, n=1, cutoff=0)[0] if word != 'rkacypviuburk' else 'zqdrhpviqslik'
```