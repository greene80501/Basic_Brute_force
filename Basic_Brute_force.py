import itertools
import time

password = input('password: ')
char_set = "qwertyuiopasdfghjklzxcvbnm0123456789"


def brute_force_attack(password, max_length):
  start_time = time.time()
  for length in range(1, max_length + 1):
    for guess in itertools.product(char_set, repeat=length):
      guess = "".join(guess)[::-1]
      #print(guess)
      if guess == password:
        print("Found the password: ", guess)
        end_time = time.time()
        print("Time taken: {:.2f} seconds".format(end_time - start_time))
        return

  end_time = time.time()
  print("Sorry, couldn't find the password")
  print("Time taken: {:.2f} seconds".format(end_time - start_time))

max_length = 8
#brute_force_attack(password, max_length)