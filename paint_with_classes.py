from math import ceil


class Wall():
    def __init__(self, height, width, coats):
        self.height = height
        self.width = width
        self.coats = coats
        self.area = self.get_area()
        self.area_of_coats = self.get_area_of_coats()
        self.liters_of_paint = self.get_liters_of_paint()
        
    def get_area(self):
        return self.height * self.width

    def get_area_of_coats(self):
        return self.area * self.coats
    
    def get_liters_of_paint(self):
        return self.area_of_coats/6


def round_up_2dp(float):
    return ceil(float * 100) / 100


def main():
    walls_list = []
    while True:
        add_wall_inp = input("\nType 1 if you'd like to add a wall, type 0 if you're finished adding walls\n")
        match add_wall_inp:
            case "1":
                h = float(input("How high is your wall in meters?\n"))
                w = float(input("How wide is your wall in meters?\n"))
                coats = int(input("How many coats of paint would you like?\n"))
                walls_list.append(Wall(h, w, coats))
            case "0":
                total_liters = 0
                for wall in walls_list:
                    total_liters += round_up_2dp(wall.liters_of_paint)
                print("To paint walls: ")
                for wall in walls_list:
                    print(str(wall.height) + " meters high by " + str(wall.width) + " meters wide with " + str(wall.coats) + " coats of paint")
                print("You will need " + str(total_liters) + " liters of paint in total to paint all these walls")
                break
            case _:
                print("Wrong value inputted")


main()
