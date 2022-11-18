import Classes.classes as classes
import json

def calculate_liters_of_paint(area, coats, coverage):
    return (area*coats)/coverage


def init_wall():
    wall = classes.Wall()
    wall.set_attributes()
    
    return wall
    
def init_surface(wall):
    surf = classes.Surface()
    surf.set_attributes()
    wall.surfaces_list.append(surf)
    
def load_paints():
    return json.load(open("Data/paints.json", "r"))


def choose_item(item, dictionary):
    temp_dict = {}
    print("\nChoose " + item + " you will be using")
    for i, key in enumerate(dictionary.keys()):
        temp_dict[i] = key
        print(str(i) + " - " + key)
    inp = int(input())
    return temp_dict[inp]

def buckets_needed(volume, sizes):
    sizes_sorted = sorted(sizes)
    count_dict = {i:0 for i in sizes_sorted}
    while (volume > 0) & bool(sizes_sorted):
        if volume >= sizes_sorted[-1]:
            volume -= sizes_sorted[-1]
            count_dict[sizes_sorted[-1]] += 1
        elif (volume < sizes_sorted[-1]):
            sizes_sorted.pop()
            volume -= sizes_sorted[-1]
            count_dict[sizes_sorted[-1]] += 1
    volume_leftover = volume
    return volume_leftover, count_dict
