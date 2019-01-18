import random
import time

throw = [ 'rock', 'paper', 'scissors' ]

for i in range(3):
	shoot = random.choice(throw)
	
	print("rock")
	time.sleep(1)
	
	print("paper")
	time.sleep(1)
	
	print("scissors" + "\n" )
	time.sleep(1)
	
	print("*** " + shoot + " ***" + "\n" )
	time.sleep(2)
