def isInside(circle_x, circle_y, rad, x, y):
      
    # Compare radius of circle
    # with distance of its center
    # from given point
    if ((x - circle_x) * (x - circle_x) + 
        (y - circle_y) * (y - circle_y) <= rad * rad):
        return True
    else:
        return False

