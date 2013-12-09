import nest
import nest.voltage_trace
import pylab

nest.ResetKernel()

liste = [(1,2,0.999),(16,4,0.356),(4,21,0.356),(11,14,0.2271)]

neuronNo={} #currently empty

for a in liste:
	if a[0] not in neuronNo:
		neuronNo[a[0]] = 1
	if a[1] not in neuronNo:
		neuronNo[a[1]] = 1

for b in neuronNo: 
	print(b)


CA3 = nest.Create('iaf_neuron')
DGneuron = nest.Create('iaf_neuron')

sine = nest.Create('ac_generator',1,{'amplitude':100.0,'frequency':2.0})

noise = nest.Create('poisson_generator',2,[{'rate':70000.0},{'rate':20000.0}])

voltmeter = nest.Create('voltmeter',1,{'withgid':True})

nest.Connect(sine, CA3)
nest.Connect(sine,DGneuron)

nest.Connect(voltmeter, CA3)
nest.Connect(voltmeter, DGneuron)

nest.ConvergentConnect(noise, CA3,[1.0,-1.0],1.0)
nest.ConvergentConnect(noise, DGneuron, [1.0,-1.0],1.0)

nest.Simulate(1000.0)

nest.voltage_trace.from_device(voltmeter)

nest.PrintNetwork()

pylab.show()

