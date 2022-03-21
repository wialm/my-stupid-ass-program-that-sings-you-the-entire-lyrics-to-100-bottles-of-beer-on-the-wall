import sys,time
def print_slow(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.03)
beer_count = 100
forever_loop = 0
while forever_loop == 0:
  while beer_count > 0:
      if beer_count == 1:
        plural_check = 'bottle'
      else:
        plural_check = 'bottles'
      print_slow(str(beer_count) + " " + str(plural_check) + " of beer on the wall,")
      time.sleep(0.5)
      print(" ")
      print_slow(str(beer_count)+ " " + str(plural_check) + " of beer.")
      time.sleep(0.8)
      print(" ")
      print_slow("Take one down,")
      time.sleep(0.3)
      print(" ")
      print_slow("Pass it around,")
      time.sleep(0.5)
      print(" ")
      beer_count = beer_count - 1
      if beer_count == 1:
        plural_check = 'bottle'
      if beer_count == 0:
        plural_check = 'bottles'
      print_slow(str(beer_count) + " " + str(plural_check) + " of beer on the wall.")
      time.sleep(0.5)
      print(" ")
      print(" ")
  print_slow("do you want to sing it again?")
  print(" ")
  print("1: yes")
  print("2: no")
  print(" ")
  replay_choice = int(input())  
  if replay_choice == 1:
    print_slow("Good choice!")
  else:
    print_slow("Too bad.")
  print(" ")
  beer_count = 100
  time.sleep(1)
