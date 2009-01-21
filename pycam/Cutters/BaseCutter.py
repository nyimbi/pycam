import pycam.Geometry

from pycam.Geometry import *
from pycam.Geometry.utils import *
from pycam.Geometry.utils import *
from math import sqrt

class BaseCutter:
    id = 0

    def __init__(self, location, radius):
        self.location = location
        self.id = BaseCutter.id
        BaseCutter.id += 1
        self.radius = radius
        self.radiussq = radius*radius
        self.minx = location.x-radius
        self.maxx = location.x+radius
        self.miny = location.y-radius
        self.maxy = location.y+radius

    def __repr__(self):
        return "BaseCutter"

    def to_mged(self):
        return ""

    def moveto(self, location):
        self.location = location
        self.minx = location.x-self.radius
        self.maxx = location.x+self.radius
        self.miny = location.y-self.radius
        self.maxy = location.y+self.radius

    def intersect(self, direction, triangle):
        return (None, None, None, INFINITE)

    def drop(self, triangle):
        # check bounding box collision
        if self.minx > triangle.maxx():
            return None
        if self.maxx < triangle.minx():
            return None
        if self.miny > triangle.maxy():
            return None
        if self.maxy < triangle.miny():
            return None

        # check bounding sphere collision
        c = triangle.center()
        if sqr(c.x-self.location.x)+sqr(c.y-self.location.y)>self.radiussq+self.radius*triangle.radius()+triangle.radiussq():
            return None

        (cl,d)= self.intersect(Point(0,0,-1), triangle)
        return cl

    def push(self, dx, dy, triangle):
        # check bounding box collision
        if dx == 0:
            if self.miny > triangle.maxy():
                return None
            if self.maxy < triangle.miny():
                return None
        if dy == 0:
            if self.minx > triangle.maxx():
                return None
            if self.maxx < triangle.minx():
                return None
        if triangle.maxz()<self.location.z:
            return None

        # check bounding sphere collision
        c = triangle.center()
        d = (c.x-self.location.x)*dy-(c.y-self.location.y)*dx
        t = self.radius + triangle.radius()
        if d < -t or d > t:
            return None

        (cl,d)= self.intersect(Point(dx,dy,0), triangle)
        return cl
