# -*- coding: utf-8 -*-
#
#   A file to regenerate the NeuroML 2 files from this neuroConstruct project
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
    print "Note: this file should be run using 'nC.bat -python XXX.py' or 'nC.sh -python XXX.py'"
    print "which use Jython (and so can access the Java classes in nC), as opposed to standard C based Python"
    print "See http://www.neuroconstruct.org/docs/python.html for more details"
    quit()

sys.path.append(os.environ["NC_HOME"]+"/pythonNeuroML/nCUtils")

import ncutils as nc # Many useful functions such as SimManager.runMultipleSims found here

projFile = File(os.getcwd(), "../SolinasEtAl-GolgiCell.ncx")

print("Generating NeuroML v1.8.1 files...")
nc.generateNeuroML1(projFile, ['Fig. 2A: Pacemaking'])
    

print("Generating NeuroML v2 files...")
nc.generateNeuroML2(projFile, ['Fig. 2A: Pacemaking'])

# Some extra files have been committed for testing or to provide other LEMS/NeuroML 2 examples
# This just pulls them from the repository, since they get wiped by the generateNeuroML2 function 
extra_files = ['.test.*', 'channel_summary', 'analyse_chans.sh', 'compare_nml2_mods.py', '../generatedNeuroML/.test.validate.omt']
               
if len(sys.argv)==2 and sys.argv[1] == "-f":
    extra_files.append('SolinasEtAl-GolgiCell.net.nml')
    
from subprocess import call
for f in extra_files:
    call(["git", "checkout", "../generatedNeuroML2/%s"%f])

quit()
