import random
from CellModeller.Regulation.ModuleRegulator import ModuleRegulator
from CellModeller.Biophysics.BacterialModels.CLBacterium import CLBacterium
from CellModeller.GUI import Renderers
import numpy
import math

cell_cols = {0:[0,1.0,0], 1:[1.0,0,0]}
outfile = 'all.csv'

def setup(sim):
    # Set biophysics, signalling, and regulation models
    biophys = CLBacterium(sim, jitter_z=False)

    # use this file for reg too
    regul = ModuleRegulator(sim, sim.moduleName)	
    # Only biophys and regulation
    sim.init(biophys, regul, None, None)
 
    # Specify the initial cell and its location in the simulation
    sim.addCell(cellType=0, pos=(0,0,0), dir=(1,0,0))

    # Add some objects to draw the models
    if sim.is_gui:
        therenderer = Renderers.GLBacteriumRenderer(sim)
        sim.addRenderer(therenderer)
    else:
        print "Running in batch mode: no display will be output"

    sim.pickleSteps = 10
    sim.saveOutput = True

def init(cell):
    # Specify mean and distribution of initial cell size
    cell.targetVol = 3.5 + random.uniform(0.0,0.5)
    # Specify growth rate of cells
    cell.growthRate = .25
    cell.color = cell_cols[cell.cellType]

def update(cells):
    #Iterate through each cell and flag cells that reach target size for division
    for (id, cell) in cells.iteritems():
        if cell.volume > cell.targetVol:
            cell.divideFlag = True

def divide(parent, d1, d2):
    # Specify target cell size that triggers cell division
    d1.targetVol = 3.5 + random.uniform(0.0,0.5)
    d2.targetVol = 3.5 + random.uniform(0.0,0.5)

