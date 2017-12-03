from enum import Enum

class Direction(Enum):
    RIGHT = 1
    UP = 2
    LEFT = 3
    DOWN = 4





def GetValueForSquare(x, y, value_dict):
    accumulator = 0

    point_list = [(x-1, y-1),
                  (x, y-1),
                  (x+1, y-1),
                  (x-1, y),
                  (x+1, y),
                  (x-1, y+1),
                  (x, y+1),
                  (x+1, y+1)]
        
    for point in point_list:
        if point in value_dict:
            accumulator += value_dict[point]

    return accumulator
    

def TravelToSquare(destination_number):
    # returns the manhattan distance of
    # the square requestion by destination_number
    # and the target value for part 2, i.e. the 
    # value of the first square
    # with a value greater than destination_number

    CurrentDirection = Direction.RIGHT

    current_number = 1

    # move right until right_lim is hit.
    # then up until top_lim
    # then left until left_lim
    # then down until bottom_lim
    
    top_lim = 0
    right_lim = 0
    bottom_lim = 0
    left_lim = 0
    
    current_x = 0
    current_y = 0

    # key is (x,y), and value is the value in that square
    value_dict = dict()
    value_dict[(0, 0)] = 1
    target_value = 1

    is_target_value_found_yet = False

    while current_number != destination_number:
        if CurrentDirection == Direction.RIGHT:
            current_x += 1
            if current_x > right_lim:
                right_lim += 1
                CurrentDirection = Direction.UP
        elif CurrentDirection == Direction.UP:
            current_y += 1
            if current_y > top_lim:
                top_lim += 1
                CurrentDirection = Direction.LEFT
        elif CurrentDirection == Direction.LEFT:
            current_x -= 1
            if current_x < left_lim:
                left_lim -= 1
                CurrentDirection = Direction.DOWN
        elif CurrentDirection == Direction.DOWN:
            current_y -= 1
            if current_y < bottom_lim:
                bottom_lim -= 1
                CurrentDirection = Direction.RIGHT
        current_number += 1
        
        square_value = GetValueForSquare(current_x, current_y, value_dict)

        if square_value > destination_number and is_target_value_found_yet == False:
            target_value = square_value
            is_target_value_found_yet = True

        value_dict[(current_x, current_y)] = square_value

    distance = abs(current_x) + abs(current_y)
    return distance, target_value

if __name__ == "__main__":
    distance, target_value = TravelToSquare(361527)

    print(f"Distance for part 1 is {distance}")
    print(f"The value for part 2 is {target_value}")
