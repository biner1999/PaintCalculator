

volume_price_dict = {2.5:12, 5:14, 10:20}


def pounds_per_liter(volume_price_dict):
    

    volume_PpL_dict = {volume:(price/volume) for volume, price in volume_price_dict.items()}

    return volume_PpL_dict



def optimize_PpL(volume_PpL_dict):
    best_vol = 0
    for volume, PpL in volume_PpL_dict.keys():
        if best_vol 


print(pounds_per_liter(volume_price_dict))

volume_PpL_dict = pounds_per_liter(volume_price_dict)

print(optimize_PpL(volume_PpP_dict))

var1 = optimize_PpL(volume_PpP_dict)