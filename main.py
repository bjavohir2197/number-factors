def son_boluvchilarini_top(san):
    boluvchilar = []
    for i in range(2, int(san ** 0.5) + 1):
        if san % i == 0:
            boluvchilar.append(i)
            if i != san // i:
                boluvchilar.append(san // i)
    return boluvchilar

san = int(input("Sonni kiriting: "))
print(son_boluvchilarini_top(san))
```

```python
def son_boluvchilarini_top(san):
    boluvchilar = set()
    for i in range(2, int(san ** 0.5) + 1):
        while san % i == 0:
            boluvchilar.add(i)
            san //= i
    if san > 1:
        boluvchilar.add(san)
    return boluvchilar

san = int(input("Sonni kiriting: "))
print(son_boluvchilarini_top(san))
