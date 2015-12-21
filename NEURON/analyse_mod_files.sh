# This script uses utilities in https://github.com/NeuroML/pyNeuroML to generate
# plots for the activation variables, etc. of selected channels in mod files

pynml-modchananalysis Golgi_NaP -stepV 5 -temperature [20,23] 
pynml-modchananalysis Golgi_Na -stepV 5 -temperature [20,23] -dt 0.001
pynml-modchananalysis Golgi_NaR -stepV 5 -temperature [20,23] 

pynml-modchananalysis Golgi_KV -stepV 5 -temperature [20,23] -dt 0.001
pynml-modchananalysis Golgi_KM -stepV 5 -temperature [20,23] 
pynml-modchananalysis Golgi_KA -stepV 5 -temperature [20,23] 

pynml-modchananalysis Golgi_Ca_HVA -stepV 5 -temperature [20,23] 
pynml-modchananalysis Golgi_Ca_LVA -stepV 5 -temperature [20,23] 

pynml-modchananalysis Golgi_BK -stepV 5 -temperature [20,23] -caConc 5e-4


#pynml-modchananalysis Golgi_hcn1 -stepV 5 -temperature [20,23] 
