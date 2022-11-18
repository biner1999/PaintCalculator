import Functions.functions as functions

volume = 156


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

print(buckets_needed(volume, [2.5, 5, 10]))