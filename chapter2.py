import numpy as np

n = 10**5

child1 = np.random.random_integers(1, 2, n)
child2 = np.random.random_integers(1, 2, n)

both_girls = np.sum(child1[child1 == child2] == 1)
elder_girl = np.sum(child1 == 1)

print(both_girls / elder_girl)

# --- Monty Hall ---
n = 10**5

first_choice = 0
win = 0

for i in range(n):
    # generate random door with car
    car_door = np.random.random_integers(0, 2)
    # take it out of the array with doors -> [0,1,2]
    remaining_doors = np.delete(np.arange(3), car_door)
    if car_door == first_choice:
        # if the chosen door has the car, randomly Monty chooses from the
        # remaining and the contestant switches to the other
        monty_pick = np.random.choice(remaining_doors)
        door_switch = np.delete(remaining_doors,
                                np.where(remaining_doors == monty_pick))
    else:
        # else he monty picks the only door with a goat and the contestant
        # switches to the car door
        door_switch = car_door

    win += 1 if door_switch == car_door else 0

# this should be 2/3 indicating that switching always has a higher probability
# of winning
print(win / n)
