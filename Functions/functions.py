import Classes.classes as classes

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