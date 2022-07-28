# Return substring instance count - 2

https://www.codewars.com/kata/52190daefe9c702a460003dd

Complete the solution so that it returns the number of times the search_text is found within the full_text.

```python
search_substr( full_text, search_text, allow_overlap = True )
```

so that overlapping solutions are (not) counted. If the searchText is empty, it should return 0. Usage examples:

```python
search_substr('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
search_substr('aaabbbcccc', 'bbb') # should return 1
search_substr( 'aaa', 'aa' ) # should return 2
search_substr( 'aaa', '' ) # should return 0
search_substr( 'aaa', 'aa', False ) # should return 1
```

# Solution

```python
import re
def search_substr(full_text, search_text, allow_overlap=True):
    cnt = 0
    if search_text == '':
        return 0
    if allow_overlap:
        while full_text:
            if search_text in full_text and 0 == full_text.index(search_text):
                cnt += 1
            full_text = full_text[1::]
        return cnt
    else:
        return len(re.findall(search_text, full_text))
```