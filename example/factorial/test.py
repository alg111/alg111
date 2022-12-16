import random

names = ['John', 'Juan', 'Jane', 'Jack', 'Jill', 'Jean']
def selectRandom(names):
  return random.choice(names)

print("The name selected is: ", selectRandom(names))