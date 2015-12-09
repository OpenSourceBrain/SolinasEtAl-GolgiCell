

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


copyNml2 'KA_CML' 'Golgi_KA'