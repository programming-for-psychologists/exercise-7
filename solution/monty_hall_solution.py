
import random
import numpy as np

def play_monty_hall(strategy):
    if strategy!="stay" and strategy!="switch":
        return "Strategy must be 'stay' or 'switch'"
    prizes = ['car', 'goat', 'goat']
    doors = range(3)
    #note that we don't need to shuffle both doors and prizes. Either shuffle prizes and pick from the same door or don't shuffle prizes and pick from a random door.

    #we don't need to do if True/return 1 else return 0. Can just return the logical expression. When evaluated in a numerical context;
    #True/False becomes 1/0 so it works below when we calculate the mean
    return (prizes[random.choice(doors)]=="car" and strategy=="stay") or (prizes[random.choice(doors)]=="goat" and strategy=="switch")


num_games = 1000 
wins_by_staying = [play_monty_hall('stay') for game in range(num_games)]
wins_by_switching = [play_monty_hall('switch') for game in range(num_games)]


print "When staying:", np.mean(wins_by_staying)
print "When switching:", np.mean(wins_by_switching)