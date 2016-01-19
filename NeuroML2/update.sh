

copyNml2()
{
    echo
    echo "-----  Copying:" $1 " to " $2
    cp ../neuroConstruct/generatedNeuroML2/$1.channel.nml $2.channel.nml.tmp
    
    sedArg="s/$1/$2/g"
    echo "Using substitution: " $sedArg
    sed $sedArg $2.channel.nml.tmp > $2.channel.nml
    rm $2.channel.nml.tmp
    echo
}


copyNml2 'NaP_CML' 'Golgi_NaP'
copyNml2 'NaT_CML' 'Golgi_Na'
copyNml2 'NaR_CML' 'Golgi_NaR'


copyNml2 'KA_CML' 'Golgi_KA'
copyNml2 'Kslow_CML' 'Golgi_KM'
copyNml2 'KV_CML' 'Golgi_KV'
copyNml2 'KAHP_CML' 'KAHP_CML'

copyNml2 'CaHVA_CML' 'Golgi_Ca_HVA'
copyNml2 'CaLVA_CML' 'Golgi_Ca_LVA'

copyNml2 'KC_CML' 'Golgi_BK'


copyNml2 'hcn1f_CML' 'Golgi_hcn1f'
copyNml2 'hcn1s_CML' 'Golgi_hcn1s'
copyNml2 'hcn2f_CML' 'Golgi_hcn2f'
copyNml2 'hcn2s_CML' 'Golgi_hcn2s'
