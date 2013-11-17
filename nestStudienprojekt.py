mport nest
import nest.topology as tp

print("new test for NEST")
print("test")
testLayer = tp.CreateLayer({'rows' : 5, 'columns' : 5, 'elements' : 'iaf_neuron'})
