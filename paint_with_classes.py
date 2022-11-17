from math import ceil

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
"""
class Surface():
    def __init__(self):
        self.height = 0
        self.width = 0
        self.name = ""
        self.area = 0
    
    def calculate_area(self):
        return self.height * self.width
    
    def set_name(self):
        self.name = input("What is the name of your surface?\n")

    def set_height(self):
        self.height = float(input("How high is your " + self.name + " in meters?\n"))
        
    def set_width(self):
        self.width = float(input("How wide is your " + self.name + " in meters?\n"))

    def set_area(self):
        self.area = self.calculate_area()
        
    def set_attributes(self):
        self.set_name()
        self.set_height()
        self.set_width()
        self.set_area()
        

class Wall(Surface):
    def __init__(self):
        super().__init__()
        self.name = "wall"
        self.coats = 0
        self.surfaces_list = []
        self.true_area = 0

    def set_coats(self):
        self.coats = int(input("How many coats of paint would your " + self.name + " need?\n"))
        
    def set_true_wall_area(self):
        total_surfaces_area = 0
        for surface in self.surfaces_list:
            total_surfaces_area += surface.area
        self.true_area = self.area - total_surfaces_area
        
    def set_attributes(self):
        self.set_height()
        self.set_width()
        self.set_area()
        self.set_coats()
    


def calculate_liters_of_paint(area, coats, coverage):
    return (area*coats)/coverage

def round_up_2dp(float):
    return ceil(float * 100) / 100


buckets_of_paint = {2.5:12, 5:14, 10:20}



def main():
    walls_list = []
    while True:
        add_wall_inp = input("\nType 1 if you'd like to add a wall, type 0 if you're finished adding walls\n")
        match add_wall_inp:
            case "1":
                wall = Wall()
                wall.set_attributes()
                while True:
                    add_surf_inp = input("\nType 1 if you'd like to add a surface not to be painted on that wall, type 0 if you're finished adding surfaces\n")
                    match add_surf_inp:
                        case "1":
                            surf = Surface()
                            surf.set_attributes()
                            wall.surfaces_list.append(surf)
                        case "0":
                            break
                        case _:
                            print("Wrong value inputted")
                walls_list.append(wall)
            case "0":
                total_liters = 0
                for wall in walls_list:
                    wall.set_true_wall_area()
                    total_liters += calculate_liters_of_paint(wall.true_area, wall.coats, 13)
                print("To paint walls: ")
                for wall in walls_list:
                    print(str(wall.height) + " meters high by " + str(wall.width) + " meters wide with " + str(wall.coats) + " coats of paint")
                print("You will need " + str(total_liters) +" liters of paint in total to paint all these walls")
                break
            case _:
                print("Wrong value inputted")


main()
