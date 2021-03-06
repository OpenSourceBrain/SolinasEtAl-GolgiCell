
import matplotlib.pyplot as pylab
import os.path


chans = {}
#chans['NaP_CML']='Golgi_NaP'
#chans['NaT_CML']='Golgi_Na'
#chans['KV_CML']='Golgi_KV'
#chans['Kslow_CML']='Golgi_KM'
#chans['CaHVA_CML']='Golgi_Ca_HVA'
#chans['CaLVA_CML']='Golgi_Ca_LVA'
#chans['NaR_CML']='Golgi_NaR'
#chans['KA_CML']='Golgi_KA'
chans['KC_CML']='Golgi_BK'

problematic = ['Im']

gates = ['m', 'h', 'n', 's', 'u', 'f', 'a', 'b', 'c']

temperatures = [20,23]

for temperature in temperatures:

    for channel_id in chans.keys():


        vramp_lems_file  = '%s.rampV.lems.%s.dat'%(channel_id, temperature)

        ts = []
        volts = []
        for line in open(vramp_lems_file):
            ts.append(float(line.split()[0])*1000)
            volts.append(float(line.split()[1])*1000)

        fig = pylab.figure()
        fig.canvas.set_window_title("Time Course(s) of activation variables of %s at %sdegC"%(channel_id, temperature))

        pylab.xlabel('Membrane potential (mV)')
        pylab.ylabel('Time Course - tau (ms)')
        pylab.grid('on')

        for gate in gates:

            tau_lems_file  = '%s.%s.tau.lems.%s.dat'%(channel_id, gate, temperature)

            if os.path.isfile(tau_lems_file):
                taus = []
                for line in open(tau_lems_file):
                    ts.append(float(line.split()[0])*1000)
                    taus.append(float(line.split()[1])*1000)

                pylab.plot(volts, taus, linestyle='-', linewidth=2, label="LEMS %s %s tau"%(channel_id, gate))

                tau_mod_file  = '../../NEURON/%s.%s.tau.%s.dat'%(chans[channel_id], gate, temperature)
                vs = []
                taus = []
                for line in open(tau_mod_file):
                    vs.append(float(line.split()[0]))
                    taus.append(float(line.split()[1]))

                pylab.plot(vs, taus, '--x', label="Mod %s %s tau"%(channel_id, gate))


        pylab.legend()


        fig = pylab.figure()
        fig.canvas.set_window_title("Steady state(s) of activation variables of %s at %sdegC"%(channel_id, temperature))

        pylab.xlabel('Membrane potential (mV)')
        pylab.ylabel('Steady state (inf)')
        pylab.grid('on')

        for gate in gates:

            inf_lems_file  = '%s.%s.inf.lems.%s.dat'%(channel_id, gate, temperature)

            if os.path.isfile(inf_lems_file):
                infs = []
                for line in open(inf_lems_file):
                    infs.append(float(line.split()[1]))

                pylab.plot(volts, infs, linestyle='-', linewidth=2, label="LEMS %s %s inf"%(channel_id, gate))

                inf_mod_file  = '../../NEURON/%s.%s.inf.%s.dat'%(chans[channel_id], gate,temperature)
                vs = []
                infs = []
                for line in open(inf_mod_file):
                    vs.append(float(line.split()[0]))
                    infs.append(float(line.split()[1]))

                pylab.plot(vs, infs, '--x', label="Mod %s %s inf"%(channel_id, gate))

        pylab.legend()

pylab.show()
