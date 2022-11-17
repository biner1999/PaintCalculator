import Classes.classes as classes
import Functions.functions as functions



"""
class Paint():
    def __init__(self, brand, coverage, color):
        self.brand = brand
        self.coverage = coverage
        self.color = color

class BucketOfPaint(Paint):
    def __init__(self, brand, coverage, color, volume, price):
        super().__init__(brand, coverage, color)
        self.volume = volume
        self.price = price

paint = Paint("Good Home", 13, "Brilliant White")
bucket = BucketOfPaint(paint.brand, paint.coverage, paint.color, 2.5, 10)
list_of_buckets = [BucketOfPaint(paint.brand, paint.coverage, paint.color, 2.5, 10)]
buckets_of_paint = {2.5:12, 5:14, 10:20}
"""


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
                total_liters = 0
                for wall in walls_list:
                    wall.set_true_wall_area()
                    total_liters += functions.calculate_liters_of_paint(wall.true_area, wall.coats, 13)
                
                #Just print statements
                print("\nTo paint walls: ")
                for wall in walls_list:
                    print("\n" + str(wall.height) + " meters high by " + str(wall.width) + " meters wide with " + str(wall.coats) + " coats of paint.")
                    print("This wall contains:")
                    for surface in wall.surfaces_list:
                        print(surface.name + " of size " + str(surface.height) + " by " + str(surface.width) + " meters.")
                print("You will need " + str(total_liters) +" liters of paint in total to paint all these walls")
                break
            case _:
                print("Wrong value inputted")


if __name__ == "__main__":
    main()