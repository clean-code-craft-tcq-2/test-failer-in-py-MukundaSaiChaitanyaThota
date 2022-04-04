
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            color_map.append(f'{i * 5 + j} | {major} | {minor}')
                        
    return len(major_colors) * len(minor_colors), color_map

result, color_map = print_color_map()

assert (color_map[0] == '1 | White | Blue')
assert (color_map[1] == '3 | White | Orange')
assert (color_map[14] == '15 | Black | Slate')
assert(result == 25)

print("All is well (maybe!)\n")
