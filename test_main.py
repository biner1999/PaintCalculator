import Functions.functions as functions
import Classes.classes as classes


def test_calculate_liters_of_paint():
    assert functions.calculate_liters_of_paint(10, 3, 10) == 3
    
def test_calculate_area():
    surface = classes.Surface()
    surface.height = 5
    surface.width = 4
    assert surface.calculate_area() == 20