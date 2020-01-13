from typing import List

def CoinCombinations(coins: List, val: int):
	# Coins must be sorted from large values to small ones
	ammount = val
	change, reps = [], []

	for i in range(0, len(coins)):
		if ammount//coins[i]!=0:
			change.append(coins[i])
			reps.append(ammount//coins[i])

			ammount -= coins[i]*(ammount//coins[i])

	return change, reps

if __name__ == "__main__":
	
	coins = [500, 200, 100, 50, 20, 10, 5]
	val = 1475

	print("Minimum number of coins problem:\n==============================\n\n")
	print("Give change for {} eur".format(val))
	print("Using bills: {}\n".format(", ".join(map(str,coins))))


	change, reps = CoinCombinations(coins, val)

	for c, v in zip(change, reps):
		print("Bill {} repeated {} times".format(c, v))


	