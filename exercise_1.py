import matplotlib.pyplot as plt
plt.ion()
import random
import copy
import numpy as np
ALIVE = 1
DEAD = 0
GRID_LENGTH = 100
ALIVE_INDEX = 5
def create_singleton_grid(length, alive_index):
    '''
    Inputs:
    grid_length (integer) - the size of the grid
    one_index (integer) - the index of the cell which is set to one.
    Returns:
    grid (numpy array)
    '''
    grid = np.zeros(length, dtype=np.int8)
    return grid
def create_random_grid(length, alive_probability):
    '''
    Make a grid of specified length with cells randomly set to one or zero, with probability p.
    Inputs:
    #You should edit this to match your function.
    Returns:
    grid (numpy array)
    '''
    grid = []
    return np.array(grid, dtype=np.int8)
def update_value(old_value, left_neighbour, right_neighbour):

    new_value = 0
    #Your code goes here
    return new_value
def update_grid(old_grid, rule=None):
    '''
    Update the values within a grid according to local rules.
    Inputs:
    old_grid (numpy array)
    Returns:
    new_grid (numpy array)
    1/30/24, 3:28 PM Terminal and Discrete Models
    file:///C:/Users/mg13730/appdata/local/temp/14.html 12/17
    '''
    new_grid = []
#Your code goes here
    return np.array(new_grid, dtype=np.int8)
def test_update_value():
    assert update_value(0,0,0)==0, "test 1"
    assert update_value(1,0,0)==0, "test 2"
    assert update_value(0,1,0)==1, "test 3"
    assert update_value(0,0,1)==0, "test 4"
    assert update_value(1,1,0)==0, "test 5"
    assert update_value(1,0,1)==0, "test 6"
    #Add the rest of the tests here - you should cover inputs of (0, 1, 1) and (1, 1, 1)
def test_update_grid():
    assert (update_grid((np.array([1, 0, 0], dtype=np.int8)))==np.array([0, 1, 0], dtype=np.int8)).all()==True
    assert (update_grid((np.array([0, 1, 0], dtype=np.int8)))==np.array([0, 0, 1], dtype=np.int8)).all()==True
    assert (update_grid((np.array([0, 0, 1], dtype=np.int8)))==np.array([1, 0, 0], dtype=np.int8)).all()==True
    assert (update_grid((np.array([1, 1, 1], dtype=np.int8)))==np.array([0, 0, 0], dtype=np.int8)).all()==True
    assert (update_grid((np.array([0, 0, 0], dtype=np.int8)))==np.array([0, 0, 0], dtype=np.int8)).all()==True
    #Add more tests here - for a length 3 grid, you should have 8 possible initial states to test.
print("Testing update value\n")
test_update_value()
print("Tests passed")
print("Testing update grid\n")
test_update_grid()
print("Tests passed")
grid1 = create_singleton_grid(GRID_LENGTH, ALIVE_INDEX)
grid2 = update_grid(grid1)
print(grid1)
print(grid2)
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(211)
ax1.set_axis_off()
image1 = np.zeros((1, GRID_LENGTH), dtype = np.int8)
#Copy CA_grid into the image array
image1[0, :] = grid1
#Display the image
ax1.imshow(image1, interpolation='none', cmap='RdPu')
ax2 = fig.add_subplot(212)
ax2.set_axis_off()
image2 = np.zeros((1, GRID_LENGTH), dtype = np.int8)
#Copy CA_grid into the image array
image2[0, :] = grid1
#Display the image
ax2.imshow(image2, interpolation='none', cmap='RdPu')
plt.pause(10)