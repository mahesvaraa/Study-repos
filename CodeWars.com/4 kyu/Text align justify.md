# Text align justify

https://www.codewars.com/kata/537e18b6147aa838f600001b

Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the
expected justification width. The longest word will never be greater than this width.

Here are the rules:

* Use spaces to fill in the gaps between words.
* Each line should contain as many words as possible.
* Use '\n' to separate lines.
* Gap between words can't differ by more than one space.
* Lines should end with a word not a space.
* '\n' is not included in the length of a line.
* Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
* Last line should not be justified, use only one space between words.
* Last line should not contain '\n'
* Strings with one word do not need gaps ('somelongword\n').

Example with width=30:

```python

Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.
```

Also you can always take a look at how justification works in your text editor or directly in HTML (css: text-align:
justify).

Have fun :)

# Solution

```python
def justify(text, width):
    while text.find('  ') != -1:
        text = text.replace('  ', ' ')

    if len(text) >= width + 1:
        text = text.replace(' ', '©')
        arr = text.split('©')

        while len(max(arr, key=len)) > width:
            for i in range(len(arr)):
                if len(arr[i]) > width:
                    arr[i] = arr[i][:width] + ' ' + arr[i][width:]
            arr = ' '.join(arr).split()

        arr2, pr = [], ''

        for i in arr:
            if len(pr + ' ' + i) <= width + 1:
                pr += i + ' '
            else:
                arr2.append(pr.strip())
                pr = i + ' '

        arr2.append(pr.rstrip())
        arr2 = [i for i in arr2 if i]
    else:
        arr2 = [text]
    for i, v in enumerate(arr2[:-1]):
        spaces = v.count(' ')
        if v.count(' ') != 0:
            for j in range((width - len(v)) // v.count(' ')):
                arr2[i] = v.replace(' ', '  '+' '*j)
        if arr2[i].count(' ') != 0:
            if len(arr2[i]) < width:
                arr2[i] = arr2[i].replace(' '*(arr2[i].count(' ')//spaces), ' '*(arr2[i].count(' ')//spaces + 1), width - len(arr2[i]))

    return '\n'.join(arr2)

justify('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.', 30)
```