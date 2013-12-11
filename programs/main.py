import nest
#import nest.topology as tp
import csv
import nest.voltage_trace
import pylab


# function that returns all neurons in a list
def getNeurons(csvfile):
  
  neurons = []

  # get information about the neuron sets from the respective csv file
  with open(csvfile, "r") as nsfile:
  
    nreader = csv.reader(nsfile, delimiter=";")
    
    for neuron in nreader:
     neurons.append(nest.Create(neuron[1]))

  return neurons


# function that returns all connections in a list
def getConnections(csvfile):

  # initialize empty list to save the connections between the neurons
  connections = []

  # open connections csv file and read data into connections list
  with open(csvfile, "r") as cfile:

    # read data with csv.reader
    reader = csv.reader(cfile, delimiter=";")

    # save every row as list in the connections list
    for row in reader:
      connections.append(row)

  return connections

#function that creates the connections between the neurons
def createConnections(neurons,connections):
  for connTuple in connections:
   for neuronTuple in neurons:
    if(connTuple[0] == neuronTuple):
      nest.Connect(neurons[connTuple[0]],neurons[connTuple[1]])

#function that connects the voltmeter/sine/poisson with the neurons
def connectVSN(neuron,v,s,n):    
   nest.Connect(v, neuron) #connect with voltmeter
   nest.Connect(s, neuron) #connect with sine
   nest.ConvergentConnect(n, neuron,[1.0,-1.0],1.0) #connect with noise

#function that gets a parameter for the time
def nestSimulate(time,voltmeter):
   nest.Simulate(time)
   nest.voltage_trace.from_device(voltmeter)
   nest.PrintNetwork()
   pylab.show() 

# ============= begin with the program ============= #

nest.ResetKernel() #Reset the Kernel when starting the programm

# read csv files from console
neuronCSV =  raw_input("Specify a filename for the neurons: ")
connectionsCSV = raw_input("Specify a filename for the connections: ")

#neuronCSV ='../csv/neurons.csv'
#connectionsCSV = '../csv/connections.csv'

# print all information
neurons =  getNeurons(neuronCSV)
print ("Neurons:")
print neurons

connections = getConnections(connectionsCSV)
print ("\nConnections:")
print connections

connect = createConnections(neurons,connections)
sine = nest.Create('ac_generator',1,{'amplitude':100.0,'frequency':2.0})
noise = nest.Create('poisson_generator',2,[{'rate':70000.0},{'rate':20000.0}])
voltmeter = nest.Create('voltmeter',1,{'withgid':True})

for neuron in neurons:
 connectVSN(neuron, voltmeter, sine, noise)

nestSimulate(4000.0,voltmeter)
