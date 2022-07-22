# RGB To Hex Conversion

https://www.codewars.com/kata/513e08acc600c94f01000001

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be
rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

```python

rgb(255, 255, 255)  # returns FFFFFF
rgb(255, 255, 300)  # returns FFFFFF
rgb(0, 0, 0)  # returns 000000
rgb(148, 0, 211)  # returns 9400D3

```

# Solution

```python
def rgb(r, g, b):
    r, g, b = r if r >= 0 else 0, g if g >= 0 else 0, b if b >= 0 else 0
    r, g, b = r if r <= 255 else 255, g if g <= 255 else 255, b if b <= 255 else 255
    return ''.join(map(lambda x: hex(x)[2:].upper().rjust(2, '0'), [r, g, b]))
```