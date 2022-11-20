import Classes.classes as classes
import Functions.functions as functions


def main():
    walls_list = []
    while True:
        add_wall_inp = input("\nType 1 if you'd like to add a wall, type 0 if you're finished adding walls\n")
        match add_wall_inp:
            #Adding walls and their surfaces
            case "1":
                wall = functions.init_wall()
                while True:
                    add_surf_inp = input("\nType 1 if you'd like to add a surface not to be painted on that wall, type 0 if you're finished adding surfaces\n")
                    match add_surf_inp:
                        case "1":
                            functions.init_surface(wall)
                        case "0":
                            break
                        case _:
                            print("Wrong value inputted")
                walls_list.append(wall)
                del wall
            #After all the walls have been added    
            case "0":
                #Loading json with paints
                paints = functions.load_paints()
                #Choosing a brand
                chosen_brand = functions.choose_item("brand", paints)
                colors = paints[chosen_brand]["colors"]
                
                chosen_color = functions.choose_item("color", colors)
                selected_paint = colors[chosen_color]
                
                liters_left = 0
                for wall in walls_list:
                    wall.set_true_wall_area()
                    liters_left += functions.calculate_liters_of_paint(wall.true_area, wall.coats, selected_paint["coverage"])

                total_liters = liters_left
                print()
                volume_price_dict = {dict["volume"]:dict["price"] for dict in selected_paint["buckets"]}

                cans_count_dict = {}
                price_total = 0
                while liters_left > 0:
                    volume_PpL_dict = functions.pounds_per_liter(volume_price_dict, liters_left)
                    best_PpL = functions.best_PpL(volume_PpL_dict)
                    price, liters_left, cans_count_dict = functions.price_of_cans(best_PpL, {2.5:12, 5:14, 10:20}, liters_left, cans_count_dict)

                    price_total += price
                print(cans_count_dict)
                
                #Just print statements
                print("To paint walls: \n")
                for wall in walls_list:
                    print(str(wall.height) + " meters high by " + str(wall.width) + " meters wide with " + str(wall.coats) + " coats of paint.")
                    print("This wall contains:")
                    for surface in wall.surfaces_list:
                        print(surface.name + " of size " + str(surface.height) + " by " + str(surface.width) + " meters.")
                    print("\n")
                print("You will need " + str(total_liters) +" liters of " + chosen_brand + " " +  chosen_color + " in total to paint all these walls")
                print("This means you will need:")
                for volume, count in cans_count_dict.items():
                    print(str(count) + " of " + str(volume) + " liters buckets")
                print("And it wil cost £" + str(price_total) + " and you will be left with " + str(abs(liters_left)) + " liters of paint")
                break
            case _:
                print("Wrong value inputted")


if __name__ == "__main__":
    pass
    main()
    
    
    
