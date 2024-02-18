def equilateral(sides):
    return (sides[0]== sides[1] and sides[0]== sides[2]) and check_triangle(sides)


def isosceles(sides):
    return (sides[0]== sides[1] or  sides[0]== sides[2] or sides[1]== sides[2]) and check_triangle(sides)


def scalene(sides):
    return (sides[0]!= sides[1] and sides[0]!= sides[2] and sides[1]!= sides[2]) and check_triangle(sides)
        
    
def check_triangle(sides):
    return sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[2] + sides[1] > sides[0]