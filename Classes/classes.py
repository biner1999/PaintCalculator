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