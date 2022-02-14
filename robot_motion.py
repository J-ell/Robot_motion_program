import simulation as sim
import sys
import time


def robot_function():
    sim.initialize_simulation()  # this function initialize the simulation
    counter = 0  # counter variable is initialize
    while True:
        sim.spin_left(30)
        counter += 1
        if counter == 5:
            sim.stop_moving_for(1)
            continue
        elif counter == 10:
            sim.stop_moving_for(0.5)
            sim.go_forward(20,1)
            continue
        elif counter == 15:
            sim.stop_moving_for(0.5)
            sim.go_backward(30,1)
            continue
        elif counter == 20:
            break
        print(counter)
        time.sleep(0.5)  # robot pause for 0.5 seconds


if __name__ == "__main__":
    robot_function()
