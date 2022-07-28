# Convert A Hex String To RGB

https://www.codewars.com/kata/5282b48bb70058e4c4000fa7

When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB) component
values for a color. Implement a function that meets these requirements:

Accepts a case-insensitive hexadecimal color string as its parameter (ex. "#FF9933" or "#ff9933")
Returns a Map<String, int> with the structure {r: 255, g: 153, b: 51} where r, g, and b range from 0 through 255
Note: your implementation does not need to support the shorthand form of hexadecimal notation (ie "#FFF")

**Example**

```python
"#FF9933" --> {r: 255, g: 153, b: 51}
```

# Solution
```python
def hex_string_to_RGB(hex_string): 
    d = {}
    d['r'] = int(hex_string[1:3], 16)
    d['g'] = int(hex_string[3:5], 16)
    d['b'] = int(hex_string[5:7], 16)
    return d
```