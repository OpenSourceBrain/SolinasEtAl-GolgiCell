TITLE Cerebellum Golgi Cell Model

COMMENT

Author:Sergio Solinas, Lia Forti, Egidio DAngelo
Based on data from : Solinas et al. 2008 Frontiers Neuroscience 2:2
Last revised: May 2007

Published in:
             Sergio M. Solinas, Lia Forti, Elisabetta Cesana, 
             Jonathan Mapelli, Erik De Schutter and Egidio D`Angelo (2008)
             Computational reconstruction of pacemaking and intrinsic 
             electroresponsiveness in cerebellar golgi cells
             Frontiers in Cellular Neuroscience 2:2
ENDCOMMENT

NEURON {
	SUFFIX %Name%
	NONSPECIFIC_CURRENT i
	RANGE el, gmax, i
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)
}

PARAMETER {
	v (mV)
	gmax= %Max Conductance Density% (mho/cm2)
	celsius  (degC)
	el = -55 (mV)
}

ASSIGNED { i (mA/cm2) }

BREAKPOINT { i = gmax* (v - el ) }
