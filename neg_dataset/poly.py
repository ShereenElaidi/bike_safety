# Determine if a point is inside a given polygon or not
# Polygon is a list of (x,y) pairs. This function
# returns True or False.  The algorithm is called
# the "Ray Casting Method".

def point_in_poly(x,y,poly):

    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

## Test

polygon = [(45.70138,-73.48171),(45.65436,-73.58161),(45.57103, -73.66127),(45.50851,-73.76237),
(45.5132,-73.84494),(45.47024,-73.87653),(45.43652,-73.97129),(45.4029, -73.94966),
(45.44471,-73.79241),(45.41598, -73.61835),(45.45374, -73.56548),(45.59348,-73.51021)]

point_x = 45.53954
point_y = -73.60839

## Call the function with the points and the polygon
print (point_in_poly(point_x,point_y,polygon))