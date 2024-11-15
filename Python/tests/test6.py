store = [
    ("Shirt", 50.00),
    ("Pants", 25.00),
    ("Laptop", 5000.00),
    ("Mouse", 250.00),
    ("iPhone X", 4150.00)
]

to_dollars = lambda data: (data[0], data[1]/3.75)
to_rupees = lambda data: (data[0], data[1]*20)

store_dollars = list(map(to_dollars, store))
store_rupees = list(map(to_rupees, store))

for i in store_rupees:
    print(i)