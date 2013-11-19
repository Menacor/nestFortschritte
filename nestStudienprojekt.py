import nest
import numpy
import nest.topology as tp

#Creating different layers in nest for training purposes
testLayer = tp.CreateLayer({'rows' : 5, 'columns' : 5, 'elements' : 'iaf_neuron'})
layerCA1 = tp.CreateLayer({'rows' : 7, 'columns' : 3, 'extent' : [2.0,0.5], 'elements' : 'iaf_neuron'})
layerCA2 = tp.CreateLayer({'rows' : 4, 'columns' : 4, 'elements' : 'iaf_neuron', 'center' : [0.5,0.5]})
layerCA3 = tp.CreateLayer({'rows' : 3, 'columns' : 4, 'extent' : [1.3, 0.7], 'elements' : 'iaf_neuron', 'center' : [1.0,1.0]})

#Creating free layers
pos = [[numpy.random.uniform(-0.5,0.5), numpy.random.uniform(-0.5,0.5)] 
for j in xrange (50)]

layerFreePos = tp.CreateLayer({'positions' : pos, 'elements' : 'iaf_neuron'})

#Creating a 3d layer
pos = [[numpy.random.uniform(-0.5,0.5), numpy.random.uniform(-0.5,0.5), numpy.random.uniform(-0.5,0.5)] for k in xrange (200)]


