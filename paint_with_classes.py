from math import ceil


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

    def set_attributes(self):
        self.set_height()
        self.set_width()
        self.set_area()
        self.set_coats()
        
    def set_coats(self):
        self.coats = int(input("How many coats of paint would your " + self.name + " need?\n"))


def calculate_liters_of_paint(area, coats, coverage):
    return (area*coats)/coverage

def round_up_2dp(float):
    return ceil(float * 100) / 100


def main():
    walls_list = []
    while True:
        add_wall_inp = input(
            "\nType 1 if you'd like to add a wall, type 0 if you're finished adding walls\n")
        match add_wall_inp:
            case "1":
                wall = Wall()
                wall.set_attributes()
                walls_list.append(wall)
            case "0":
                total_liters = 0
                for wall in walls_list:
                    total_liters += round_up_2dp(calculate_liters_of_paint(wall.area, wall.coats, 13))
                print("To paint walls: ")
                for wall in walls_list:
                    print(str(wall.height) + " meters high by " + str(wall.width) +
                          " meters wide with " + str(wall.coats) + " coats of paint")
                print("You will need " + str(total_liters) +
                      " liters of paint in total to paint all these walls")
                break
            case _:
                print("Wrong value inputted")


main()
