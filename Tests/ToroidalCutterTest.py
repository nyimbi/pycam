#!/usr/bin/python
import sys
sys.path.insert(0,'.')

from pycam.Geometry import *
from pycam.Cutters.ToroidalCutter import *

from pycam.Gui.Visualization import ShowTestScene

import math

if __name__ == "__main__":

    if False:
        cutter = ToroidalCutter(1, 0.25, Point(-10,0.5,0))
        edge = Line(Point(0,0,-10),Point(0,0,10))
        dir = Point(1,0,0)
        print "cutter=", cutter
        print "edge=", edge
        print "dir=", dir
        (cl,ccp,cp,d) = cutter.intersect_sphere_line(dir, edge)
        print "cp=", cp
        print "ccp=", ccp
        print "d=", d
        print "cl=", cl
        exit()

    if False:
        cutter = ToroidalCutter(1, 0.25, Point(-10,0,0))
        edge = Line(Point(0,-5,1),Point(3,+5,1))
        dir = Point(1,-0.2,0)
        print "cutter=", cutter
        print "edge=", edge
        print "dir=", dir
        (cl,ccp,cp,d) = cutter.intersect_cylinder_line(dir, edge)
        print "cp=", cp
        print "ccp=", ccp
        print "d=", d
        print "cl=", cl

    #dir = Point(0,0,-1)
    #c = ToroidalCutter(1, 0.25, Point(0,0,6))
    #c = ToroidalCutter(1, 0.25, Point(-2.2,0.2,6))
    #c = ToroidalCutter(1, 0.25, Point(-1.7,0.5,6))
    dir = Point(1,0,0)
    c = ToroidalCutter(1, 0.25, Point(-10,0.1,1.9))
    print "c=", c
    t = Triangle(Point(-2,0,2), Point(2,1,3), Point(2,-1,4))
    print "t=", t

    if False:
        if False:
            (cl_p,ccp_p,cp_p,d_p) = c.intersect_torus_plane(dir,t)
            print "ccp=", ccp_p
            print "cp=", cp_p
            print "cl=", cl_p
            print "d=", d_p

        if False:
            p = t.p1
            (cl_v,ccp_v,cp_v,d_v) = c.intersect_torus_point(dir,p)
            print "ccp=", ccp_v
            print "cp=", cp_v
            print "cl=", cl_v
            print "d=", d_v

        if False:
            e = Line(t.p1,t.p2)
            (cl_e,ccp_e,cp_e,d_e) = c.intersect_torus_line(dir,e)
            print "ccp=", ccp_e
            print "cp=", cp_e
            print "cl=", cl_e
            print "d=", d_e

        if False:
            (cl,d) = c.intersect(dir,t)
            print "cl=", cl

    if False:
        samples = 50
        x0 = -5.0
        x1 = +5.0
        y0 = -5.0
        y1 = +5.0
        z = 10
        pathlist = []
        for i in range(0,samples):
            x = x0 + i * ((x1-x0) / samples)
            p = Path()
            for j in range(0,samples):
                y = y0 + j * ((y1-y0) / samples)
                c.moveto(Point(x,y,z))
                cl = c.drop(t)
                if cl:
                    p.append(cl)
                else:
                    p.append(Point(x,y,0))
            pathlist.append(p)
        c.moveto(Point(x0,y0,z))
        ShowTestScene(t, c, pathlist)

    if True:
        samples = 100
        layers = 10
        x0 = -5.0
        x1 = +5.0
        y0 = -5.0
        y1 = +5.0
        z0 = 0
        z1 = 3
        dir = Point(1,0,0)
        pathlist = []
        for i in range(0, layers):
            z = z1-i*float(z1-z0)/layers
            for j in range(0,samples):
                y = y0 + j * ((y1-y0) / samples)
                c.moveto(Point(x0,y,z))
                (cl,l) = c.intersect(dir,t)
                if cl:
                    p = Path()
                    #p.append(c.center)
                    #p.append(ccp)
                    #p.append(cp)
                    p.append(cl)
                    p.append(cl.sub(dir.mul(l)))
                    pathlist.append(p)

        c.moveto(Point(x0,y0,z))
        ShowTestScene(t, c, pathlist)