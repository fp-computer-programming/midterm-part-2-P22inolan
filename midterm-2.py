# Author: IBN (AMDG) 12/14/21

initial = input("What was the initial velocity? ")
final = input("What was the final velocity? ")
time = input("What was the time? ")

acceleration = (float(final) - float(initial)) / float(time)

print("The average acceleration was: {0} meters per second per second.".format(acceleration))