import random
import numpy as np

def	isBirthdayShared(numPeople):
	birthdays = [random.randrange(365) for curPerson in range(numPeople)]
	#set is, by definition, unique. So by turning a list as a set, we find out how many unique elements it has.
	#if it's fewer than the original length, there is at least one repeat (i.e., shared birthday)
	return len(set(birthdays)) < len(birthdays)

def birthdaySharedLikelihood(numPeople,repeats):
	return np.mean([isBirthdayShared(numPeople) for iteration in range(repeats)])

	
def numPeopleForProb(repeats,prob):
	for numPeople in range(365):
		if birthdaySharedLikelihood(numPeople,repeats)>prob:
			return numPeople

def getMode(lst):
	uniqueNumbers = set(lst)
	counts = {lst.count(num):num for num in uniqueNumbers}
	return counts[max(counts.keys())]


for numPeople in range(50):
	print numPeople, "people walk into a room. The probability of a shared birthday is,", birthdaySharedLikelihood(numPeople,1000)

print "Modal number of people that will yield a 50% chance of birthday match:", getMode([numPeopleForProb(1000,.5) for i in range(20)])




"""
Other ways of computing modes (https://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list/35302979)

#method 1
from collections import Counter
data = Counter(your_list_in_here)
data.most_common()   # Returns all unique items and their counts
data.most_common(1)  # Returns the highest occurring item

#method2
max(set(modalValueOf50), key=modalValueOf50.count)

"""