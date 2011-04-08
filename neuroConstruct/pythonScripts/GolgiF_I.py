#
#
#   A file which generates a frequency vs current curve for the Granule & Golgi cells
#   in the GranCellLayer project
#   
#   To execute this file, type '..\..\..\nC.bat -python GranGolgiF_I.py' (Windows)
#   or '../../../nC.sh -python GranGolgiF_I.py' (Linux/Mac)
#
#   Author: Padraig Gleeson
#
#   This file has been developed as part of the neuroConstruct project
#   This work has been funded by the Medical Research Council and the
#   Wellcome Trust
#
#

import sys
import os

try:
	from java.io import File
except ImportError:
	print "Note: this file should be run using ..\\..\\..\\nC.bat -python XXX.py' or '../../../nC.sh -python XXX.py'"
	print "See http://www.neuroconstruct.org/docs/python.html for more details"
	quit()

from math import *

sys.path.append(os.environ["NC_HOME"]+"/pythonNeuroML/nCUtils")

import ncutils as nc




# Change this number to the number of processors you wish to use on your local machine
numConcurrentSims = 4



# Load neuroConstruct project

projFile = File("../SolinasEtAl_GolgiCell.ncx")


simManager = nc.SimulationManager(projFile,
                                  numConcurrentSims)

             
simConfigName ="Fig. 2A: Pacemaking"
simConfig = simManager.project.simConfigInfo.getSimConfig(simConfigName)
simConfig.addInput("CurrentOffset")


preStimDel = 0
preStimDur = 200

stimAmpLow = -0.04
stimAmpInc = 0.01
stimAmpHigh = 0.4

stimDel = preStimDur
stimDur = 5000

simDuration = preStimDur + stimDur # ms

analyseStartTime = stimDel + 200 # So it's firing at a steady rate...
analyseStopTime = simDuration
analyseThreshold = -20 # mV


simManager.generateFICurve("NEURON",
                 simConfigName,
                 stimAmpLow,
                 stimAmpInc,
                 stimAmpHigh,
                 stimDel,
                 stimDur,
                 simDuration,
                 analyseStartTime,
                 analyseStopTime,
                 analyseThreshold)