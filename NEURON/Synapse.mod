TITLE Synapse C=O gating scheme

COMMENT
Synaptic model C=O gating scheme.
tau_1, tau_2 are the binding and unbinding time constants.

Published in:
             Sergio M. Solinas, Lia Forti, Elisabetta Cesana, 
             Jonathan Mapelli, Erik De Schutter and Egidio D`Angelo (2008)
             Computational reconstruction of pacemaking and intrinsic 
             electroresponsiveness in cerebellar golgi cells
             Frontiers in Cellular Neuroscience 2:2
ENDCOMMENT

NEURON {
	POINT_PROCESS Synapse
	NONSPECIFIC_CURRENT i	
	RANGE g,gmax, Cdur,Erev 
	RANGE tau_1,tau_2
}

UNITS {
	(nA) = (nanoamp)
	(mV) = (millivolt)	
	(mM) = (milli/liter)
	(pS) = (picosiemens)
	(nS) = (nanosiemens)
	(um) = (micrometer)
	PI   = (pi)(1)
}

PARAMETER {
	:  Postsynaptic parameters
	tau1		= .4		(/ms/mM) 	 
        tau2		= 3		(/ms)
        gmax		= 1150 		(pS)
	Cdur		= 0.3		(ms)		 
	Erev		= 0		(mV)
	Tmax		= 1  (mM)
}


ASSIGNED {
	v		(mV)		: postsynaptic voltage
	i 		(nA)		: current = g*(v - Erev)
	g 		(pS)		: conductance
	r1		(/ms)
	T		(mM)
	ton		(ms)	
	
}

STATE {	
	C
	O
}	
	

INITIAL {
	C		=	1
	O		=	0
	T		=	0 	(mM)
	ton		=  	-1   (ms)
}

BREAKPOINT {
	SOLVE kstates METHOD sparse
	g =gmax * O
	i = (1e-6) * g * (v - Erev) : 1e-6 fA=>nA
}


KINETIC kstates {
	: Postsynaptic scheme
	r1 = 1/tau1 * T
	~ C  <-> O	(r1,1/tau2)
	CONSERVE C+O = 1
}


NET_RECEIVE(weight, on, nspike, t0 (ms), tsyn (ms)) {
	INITIAL {
		nspike = 1
		tsyn=t
	}
   	if (flag == 0) { 
		nspike = nspike + 1
		if (!on) {
			ton=t
			t0=t
			on=1				
		        T=Tmax
			tsyn=t						
		}
		net_send(Cdur,nspike)
    	}
	if(flag==nspike){ 		
		T = 0
		on = 0
	}
}	 

 
