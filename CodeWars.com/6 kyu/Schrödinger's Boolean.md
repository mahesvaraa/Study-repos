# Schrödinger's Boolean

Can a value be both True and False?

Define omnibool so that it returns True for the following:

```
omnibool == True and omnibool == False
```

# Solution

```
class omn:
    def __eq__(self, other):
        return True
omnibool = omn()
```