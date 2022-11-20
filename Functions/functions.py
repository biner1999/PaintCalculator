import Classes.classes as classes
import math
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

def buckets_needed(volume, volume_price_dict):
    volume_PpL_dict = pounds_per_liter(volume_price_dict)
    optimized_volume_PpL_dict = optimize_PpL(volume_PpL_dict)
    sizes_sorted = sorted(sizes)
    count_dict = {i:0 for i in sizes_sorted}
    while (volume > 0) & bool(sizes_sorted):
        if volume >= sizes_sorted[-1]:
            volume -= sizes_sorted[-1]
            count_dict[sizes_sorted[-1]] += 1
        elif (volume < sizes_sorted[-1]):
            copy_sizes_sorted = sizes_sorted.reverse()
            print(copy_sizes_sorted)
            smallest = 0
            for y in sizes_sorted:
                if y > volume:
                    smallest = y
                    
    # do stuff with lst
            volume -= smallest
            count_dict[smallest] += 1
    volume_leftover = volume
    return volume_leftover, count_dict

def pounds_per_liter(volume_price_dict, volume):
    volume_PpL_dict = {}
    for can_volume, price in volume_price_dict.items():
        cans_needed = math.ceil(volume / can_volume)
        PpL = (cans_needed * price) / volume
        volume_PpL_dict[can_volume] = PpL
        
    return volume_PpL_dict



def best_PpL(volume_PpL_dict):
    rvolume_list = list(volume_PpL_dict.keys())
    rvolume_list.reverse()
    rPpL_list = list(volume_PpL_dict.values())
    rPpL_list.reverse()
    for i in range(len(rvolume_list)):
        for j in range(i+1, len(rvolume_list)):
            if rPpL_list[i] > rPpL_list[j]:
                if rvolume_list[i] in volume_PpL_dict:
                    volume_PpL_dict.pop(rvolume_list[i])

    can_volume = min(volume_PpL_dict, key=volume_PpL_dict.get)
    return can_volume

def price_of_cans(can_volume, volume_price_dict, volume, cans_count_dict):
    if can_volume > volume:
        cans_count_dict = increment_or_add_dict(can_volume, 1, cans_count_dict)
        return volume_price_dict[can_volume], volume - can_volume, cans_count_dict
    else:
        cans_to_be_bought = volume // can_volume
        cans_count_dict = increment_or_add_dict(can_volume, cans_to_be_bought, cans_count_dict)
        return cans_to_be_bought * volume_price_dict[can_volume], volume%can_volume, cans_count_dict

def increment_or_add_dict(key, value, dictionary):
    if not key in dictionary:
        dictionary[key] = value
    else:
        dictionary[key] += value

    return dictionary
