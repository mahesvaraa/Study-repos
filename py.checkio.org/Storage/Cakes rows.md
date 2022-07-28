# The Rows of Cakes

Someone has decided to bake a load of cakes and place them on the floor. Our robots can't help but try to find a pattern
behind the cakes' disposition. Some cakes form rows, we want to count these rows. A row is a sequence of three or more
cakes if we can draw a straight line through its centers. The greater row takes up the smaller rows. So if we have a row
with 4 cakes, then we have only one row (not 4 by 3).

The cake locations are represented as a list of coordinates. A coordinate is a list of two integers. You should count
the rows.

![](https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/3a217113067647379f960724833aab50/cakes-rows.png)

**Input**: Сoordinates as a list of lists with two integers.

**Output**: The quantity of rows as an integer.

**Example**:

```python

checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
checkio([[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2], [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6

```

**How it is used**: This is an example of the image and pattern recognition. This concept can be useful for the game
mechanics or if you want to write a bot for games, or when transposing printed text to a digital format.

**Precondition**: 0 < |coordinates| < 20
∀ x,y ∈ coordinates : 0 ≤ x,y ≤ 10

# Solution

```python
def checkio(cakes):
    res = list()

    for c in cakes:
        for a in cakes:
            for b in cakes:
                if c != a and c != b and a != b:
                    if (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1]) == 0:
                        if sorted((a, b, c)) not in res:
                            res.append(sorted((a, b, c)))

    res3 = res.copy()
    for i in res3:
        for j in res3:
            k = i
            i = sorted(i)
            j = sorted(j)
            if (i != j and i[0] == j[0] and i[1] == j[1] and i[2] < j[2]) or (
                    i != j and i[0] < j[0] and i[1] == j[1] and i[2] == j[2]) or (
                    i != j and i[0] == j[0] and i[1] < j[1] and i[2] == j[2]):
                try:
                    res.remove(k)
                except:
                    pass
    return len(res)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6

```