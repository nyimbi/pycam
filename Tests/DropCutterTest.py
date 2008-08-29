#!/usr/bin/python
import sys
sys.path.insert(0,'.')

from pycam.Geometry import *
from pycam.Cutters.SphericalCutter import *
from pycam.Cutters.CylindricalCutter import *
from pycam.Cutters.ToroidalCutter import *

from pycam.Gui.Visualization import ShowTestScene

from pycam.Importers.TestModel import TestModel


from pycam.PathGenerators.DropCutter import DropCutter
from pycam.Exporters.SimpleGCodeExporter import SimpleGCodeExporter

if __name__ == "__main__":

    c = SphericalCutter(1, Point(0,0,7))
    #c = CylindricalCutter(1, Point(0,0,7))
    #c = ToroidalCutter(1, 0.25, Point(0,0,7))
    print "c=", c

    model = TestModel()

    if True:
        samples = 20
        lines = 20
        x0 = -7.0
        x1 = +7.0
        y0 = -7.0
        y1 = +7.0
        z0 = 0
        z1 = 4
        dx = (x1-x0)/samples
        dy = (y1-y0)/lines
        pg = DropCutter(c, model)

        pathlist = pg.GenerateToolPath(x0, x1, y0, y1, z0, z1, dx, dy)

        g = SimpleGCodeExporter("cutter2.nc", z1)
        g.AddPathList(pathlist)
        g.close()

        ShowTestScene(model, c, pathlist)

