# lib
import random

# --- step1 ---

### create blue random
def create_random_blue_array(blue_rows, blue_cols, ratio):
    blue_array = [[1 if random.random() < ratio else 0 for _ in range(blue_cols)] for _ in range(blue_rows)]
    return blue_array

# set blue array row and col
blue_rows = 100
blue_cols = 100

# set blue_ratio 0 ~ 1
blue_ratio = 0.1

retry_time = 10000


### find boundary empty pos
def find_zeros_on_boundary(array):
    zeros_on_boundary = []
    rows = len(array)
    cols = len(array[0])

    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                if array[i][j] == 0:
                    zeros_on_boundary.append((i, j))

    return zeros_on_boundary

### Discovering Adjacent Coordinates of Structures
def find_adjacent_coordinates(coord):
    x, y = coord
    adjacent_coords = []

    # Define the points that are offset up, down, left, and right
    # Even numbered rows and odd numbered rows respectively define offsets for finding connecting structures
    if x % 2 == 0:
        directions = [(1,-1),(-1,-1),   (1, 0), (-1, 0), (0, 1), (0, -1)]
    else:
        directions = [(-1,1),( 1, 1),   (1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy

        # Check if the new coordinate is within bounds
        if 0 <= new_x < blue_rows and 0 <= new_y < blue_cols:
            adjacent_coords.append((new_x, new_y))

    return adjacent_coords

### Mark as water ingress status
def modify_blue_array_watered(array, coord):
    x, y = coord
    if 0 <= x < len(array) and 0 <= y < len(array[0]):
        array[x][y] = 2
    # else:
    #     print(f"Coordinates ({x}, {y}) are out of bounds.")

### Query the number of blue water ingress
def count_blue_array_watered(array):
    count = 0
    for row in array:
        count += row.count(2)
    return count

### Find all the coordinates that have been flooded
def get_blue_array_watered_pos(array):
    coordinates = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 2:
                coordinates.append((i, j))
    return coordinates

result_ratio_array = [0] * retry_time

for i in range(retry_time):

    random_blue_array = create_random_blue_array(blue_rows, blue_cols, blue_ratio)

    # for row in random_blue_array:
    #     print(row)

    ### make random_blue_array result
    iteration_count = 0
    cur_watered_count = 0
    last_watered_count = 0
    while True:

        if iteration_count == 0:

            # first iteration find boundary 0 -> 2
            zeros_on_boundary = find_zeros_on_boundary(random_blue_array)

            # no empty result 0 %
            if not zeros_on_boundary:
                # print("No zeros found on the boundary. Exiting loop.")
                break

            for coord in zeros_on_boundary:
                modify_blue_array_watered(random_blue_array, coord)
                # print(coord)
        else:

            # iteration find adjacent_coordinates 0 -> 2
            
            watered_pos_list = get_blue_array_watered_pos(random_blue_array)
            # print(f"watered_pos_list : {watered_pos_list}")

            for num in watered_pos_list:
                watered_pos_coords = find_adjacent_coordinates(num)
                # print(f"Adjacent coordinates of {num}:")
                for adj_coord in watered_pos_coords:
                    # print(adj_coord)
                    x, y = adj_coord
                    if random_blue_array[x][y] == 0:
                        random_blue_array[x][y] = 2

            # check iteration no change exit
            cur_watered_count = count_blue_array_watered(random_blue_array)
            
            if cur_watered_count != last_watered_count: # cur_watered_count first time not 0 (if not zeros_on_boundary)
                last_watered_count = cur_watered_count
                # print(f"cur_watered_count: {cur_watered_count}")
            else:
                # print("No new watered in blue_array")
                break

        # change iteration_count
        # print(f"iteration_count: {iteration_count}")
        iteration_count += 1


    result_num_watered = count_blue_array_watered(random_blue_array)
    # print(f"result_num_watered: {result_num_watered}")


    watered_pos_list = get_blue_array_watered_pos(random_blue_array)
    # print(f"watered_pos_list : {watered_pos_list}")

    result_num_watered_link_two = 0
    for num in watered_pos_list:
        watered_pos_coords = find_adjacent_coordinates(num)
        # print(f"Adjacent coordinates of {num}:")
        for adj_coord in watered_pos_coords:
            # print(adj_coord)
            x, y = adj_coord
            if random_blue_array[x][y] == 2:
                result_num_watered_link_two += 1

    result_num_watered_link_two = result_num_watered_link_two / 2
    # print(f"result_num_watered_link_two: {result_num_watered_link_two}")



    result_num_watered_link_three = 0
    result_num_watered_link_three_last = 0
    for num in watered_pos_list:
        # print(num)
        x = num[0]
        y = num[1]
        # print(f"X: {x}, Y: {y}")

        # find link_three
        if x % 2 == 0:

            if x-1 >= 0 and y-1 >= 0 and random_blue_array[x-1][y-1] == 2 and random_blue_array[x-1][y] == 2:
                result_num_watered_link_three += 1

            if y+1 < blue_cols and x-1 >= 0 and random_blue_array[x][y+1] == 2 and random_blue_array[x-1][y] == 2:
                result_num_watered_link_three += 1

            if y+1 < blue_cols and x+1 < blue_rows and random_blue_array[x][y+1] == 2 and random_blue_array[x+1][y] == 2:
                result_num_watered_link_three += 1

            if x+1 < blue_rows and y-1 >= 0 and random_blue_array[x+1][y-1] == 2 and random_blue_array[x+1][y] == 2:
                result_num_watered_link_three += 1

            if x+1 < blue_rows and y-1 >= 0 and y-1 >= 0 and random_blue_array[x+1][y-1] == 2 and random_blue_array[x][y-1] == 2:
                result_num_watered_link_three += 1

            if x-1 >= 0 and y-1 >= 0 and random_blue_array[x-1][y-1] == 2 and random_blue_array[x][y-1] == 2:
                result_num_watered_link_three += 1

        else:

            if y-1 >= 0 and x-1 >= 0 and random_blue_array[x][y-1] == 2 and random_blue_array[x-1][y] == 2:
                result_num_watered_link_three += 1

            if y+1 < blue_cols and x-1 >= 0 and random_blue_array[x-1][y+1] == 2 and random_blue_array[x-1][y] == 2:
                result_num_watered_link_three += 1

            if y+1 < blue_cols and x-1 >= 0 and random_blue_array[x-1][y+1] == 2 and random_blue_array[x][y+1] == 2:
                result_num_watered_link_three += 1

            if y+1 < blue_cols and x+1 < blue_rows and random_blue_array[x+1][y+1] == 2 and random_blue_array[x][y+1] == 2:
                result_num_watered_link_three += 1

            if x+1 < blue_rows and random_blue_array[x+1][y] == 2 and y+1 < blue_cols and random_blue_array[x+1][y+1] == 2:
                result_num_watered_link_three += 1

            if x+1 < blue_rows and y-1 >= 0 and random_blue_array[x+1][y] == 2 and random_blue_array[x][y-1] == 2:
                result_num_watered_link_three += 1

        # if result_num_watered_link_three_last != result_num_watered_link_three:
        #     print(f"!!!!!!!!!! ({x}, {y}) !!!!!!!!!!!!!!")

    result_num_watered_link_three = result_num_watered_link_three / 3
    # print(f"result_num_watered_link_three: {result_num_watered_link_three}")


    result_red_watered_num = result_num_watered * 6 - result_num_watered_link_two * 2 + result_num_watered_link_three
    # print(f"result_red_watered_num: {result_red_watered_num}")


    def calculate_beehive_points(M, N):
        total_points = 2 * M * ( N + 1) + 2 * N
        return total_points

    result_red_total_num = calculate_beehive_points(blue_rows,blue_cols)
    # print(f"result_red_total_num: {result_red_total_num}")

    result_ratio = result_red_watered_num / result_red_total_num
    print(f"result_ratio: {result_ratio}")

    result_ratio_array[i] = result_ratio

average_value = sum(result_ratio_array) / len(result_ratio_array)
print(f"average_value: {average_value}")



