import pickle

# pickle.dump()
# pickle.dumps()


# pickle.load()
# pickle.loads()

class Fruit:
    pass


banana = Fruit()
banana.color = 'yellow'
banana.price = 1

with open("Fruit.data", "wb") as f:
    pickle.dump(banana, f)


with open("Fruit.data", "rb") as f:
    unpickled = pickle.load(f)


print(unpickled.color)
