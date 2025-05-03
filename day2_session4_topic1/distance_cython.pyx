# distance_cython.pyx

cdef struct Point:
    double x
    double y

cdef double distance(Point* a, Point* b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

def calculate_distance(tuple a, tuple b):
    cdef Point p1, p2
    p1.x, p1.y = a
    p2.x, p2.y = b
    return distance(&p1, &p2)