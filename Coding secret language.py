import random
import string


def generate_random_string(length):
  characters = string.ascii_letters
  random_string = ''.join(random.choice(characters) for i in range(length))
  return random_string


x = input("type here : ")
words = x.split()
for word in words:
  if len(word) >= 3:
    word = word[1:] + word[0]
    word = generate_random_string(3) + word + generate_random_string(3)
    print(word)

  else:
    word = word[::-1]
    print(word)
