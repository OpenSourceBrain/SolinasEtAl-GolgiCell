# This script requires pyNeuroML (https://github.com/NeuroML/pyNeuroML) to run

CHANNELS="NaP_CML.channel.nml KV_CML.channel.nml  Kslow_CML.channel.nml NaT_CML.channel.nml CaHVA_CML.channel.nml CaLVA_CML.channel.nml hcn1f_CML.channel.nml  hcn1s_CML.channel.nml  hcn2f_CML.channel.nml  hcn2s_CML.channel.nml"

pynml-channelanalysis  $CHANNELS\
                      -caConc 4.3e-4 -temperature 20 -datSuffix '.20' -html -md -minV -75 # -75 as NaT has tau ~= 0 at <= -80 mV

pynml-channelanalysis  $CHANNELS\
                      -caConc 4.3e-4 -temperature 23 -datSuffix '.23' -html -md -minV -75 # -75 as NaT has tau ~= 0 at <= -80 mV

