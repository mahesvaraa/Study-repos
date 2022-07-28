# Base64 Encoding

https://www.codewars.com/kata/5270f22f862516c686000161

Extend the String object (JS) or create a function (Python, C#) that converts the value of the String to and from Base64
using the ASCII (UTF-8 for C#) character set.

**Example (input -> output):**

```python
'this is a string!!' -> 'dGhpcyBpcyBhIHN0cmluZyEh'
```

You can learn more about Base64 encoding and decoding here.

Note: This kata uses the non-padding version ("=" is not added to the end).

# Solution

```python
from base64 import b64decode, b64encode
def to_base_64(string):
    return b64encode(string.encode()).decode("UTF-8").strip('=')

    
def from_base_64(string):
    return b64decode((string + '==').encode()).decode("UTF-8")
```