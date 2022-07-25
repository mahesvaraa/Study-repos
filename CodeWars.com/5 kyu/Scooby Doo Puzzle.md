# Scooby Doo Puzzle

https://www.codewars.com/kata/58693bbfd7da144164000d05

**Introduction**

```
Good one Shaggy! We all love to watch Scooby Doo, Shaggy Rogers, Fred Jones, Daphne Blake and Velma Dinkley solve the clues and figure out who was the villain. The story plot rarely differed from one episode to the next. Scooby and his team followed the clue then unmasked the villain at the end.
```

**Task**

```
Your task is to initially solve the clues and then use those clues to unmask the villain. You will be given a string of letters that you must manipulate in a way that the clues guide you. You must then output the villain.
You will be given an Array of potential villains and you must only return the correct masked villain.
```

**Potential Villains for the example test cases**

```
Black Knights, Puppet Master, Ghost Clowner, Witch Doctors, Waxed Phantom, Manor Phantom, Ghost Bigfoot, Haunted Horse, Davy Crockett, Captain Injun, Greens Gloobs, Ghostly Manor, Netty Crabbes, King Katazuma, Gators Ghouls, Headless Jack, Mambas Wambas, Medicines Man, Demon Sharker, Kelpy Monster, Gramps Vamper, Phantom Racer, Skeletons Men, Moon Monsters
```

There will be different villains for the main test cases!

```
Clue 1: The first clue is in a 'house' on 'String Class' Avenue.
```

Good luck!

# Solution

```python
def scoobydoo(villian, villians):
    String().house()
    """
    Step 1: Rotate all letters to the right by 5
    Clue: You are close to the monster so you may need to create a 'Disguise'
    """
    Disguise()
    """
    Step 2: Reverse the whole string
    Clue: What is the length of Scooby Doo's favourite snack?
    Try using the answer in the Integer Class
    """
    Integer().eleven()
    """
    Step 3: Add 5 letters onto every even letter in the Villans Name ie a=>f
    Make sure after the letter z it goes round to a 
    """
    res = []
    for i, v in enumerate(villian):
        if i % 2 == 0:
            res += v
        else:
            res += 'abcdefghijklmnopqrstuvwxyz'[('abcdefghijklmnopqrstuvwxyz'.index(v) + 5) % 26]

    for i in villians:
        if ''.join(sorted(res)) == ''.join(sorted(i.lower().replace(' ', ''))):
            return i
```