mport nest
import nest.topology as tp

print("new test for NEST")

testLayer = tp.CreateLayer({'rows' : 5, 'columns' : 5, 'elements' : 'iaf_neuron'})

print("adding a default print line")
