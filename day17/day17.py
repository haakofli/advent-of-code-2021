from time import perf_counter
from typing import List



def part1(start_x, start_y, x, y):
    position = [start_x, start_y]
    highest = [0,0]

    velocities_that_work = []
    for k in range(0, 1, 1):
        #print(f"Checking y_velocity from {k} to {k+500}. Please wait...")
        for i in range(-500, 500):
            for j in range(-500, 500):
                x_velocity = i
                y_velocity = j

                position = [start_x, start_y]

                while position[0] < x[1] and position[1] > y[0]:
                    position[0] += x_velocity
                    position[1] += y_velocity
                    #print(f"x: {position[0]} , y: {position[1]}")
                    if x_velocity > 0: x_velocity -= 1
                    elif x_velocity < 0: x_velocity += 1
                    y_velocity -= 1

                    if x[0] <= position[0] <= x[1] and y[1] >= position[1] >= y[0]:
                        #print(position)
                        velocities_that_work.append([i,j])
        

    '''for velocities in velocities_that_work:

        x_velocity = velocities[0]
        y_velocity = velocities[1]

        position = [start_x, start_y]

        while position[0] < x[1] and position[1] > y[0]:
            position[0] += x_velocity
            position[1] += y_velocity
            if x_velocity > 0: x_velocity -= 1
            elif x_velocity < 0: x_velocity += 1
            y_velocity -= 1
            if position[1] > highest[0]:
                highest = [position[1], velocities[0]]
                print(f"New highest y position = {position[1]} reached with initial y_velocity = {velocities[1]} nad x_velocity{velocities[0]}")
    '''

    print("----------------------------------------------------------")
    print(len(velocities_that_work))
    #print(velocities_that_work)
    new_velocities = []
    for velocities in velocities_that_work:
        if velocities not in new_velocities:
            new_velocities.append(velocities)
    
    print(len(new_velocities))

    

    


def main():
    start = perf_counter()
    
    x = [269, 292]
    y = [-68, -44]

    #x = [20, 30]
    #y = [-10, -5]

    part1(0, 0, x, y)
    # my function here

    # not:
    # 2211


    end = perf_counter()
    print(f"{end-start} seconds to execute code")

if __name__ == "__main__":
    main()