import nest
#import nest.topology as tp
import csv
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


# ============= begin with the program ============= #

nest.ResetKernel() #Reset the Kernel when starting the programm

# read csv files from console
#neuronCSV =  raw_input("Specify a filename for the neurons: ")
#connectionsCSV = # raw_input("Specify a filename for the connections: ")

neuronCSV ='../csv/neurons.csv'
connectionsCSV = '../csv/connections.csv'

# print all information
neurons =  getNeurons(neuronCSV)
print ("Neurons:")
print neurons

connections = getConnections(connectionsCSV)
print ("\nConnections:")
print connections

connect = createConnections(neurons,connections)




###########################
neuron = nest.Create('iaf_neuron')
sine = nest.Create('ac_generator', 1, {'amplitude': 100.0, 'frequency': 2.0})
noise = nest.Create('poisson_generator', 2,[{'rate': 70000.0}, {'rate': 20000.0}])
voltmeter = nest.Create('voltmeter', 1, {'withgid':True})

nest.Connect(sine, neuron)
nest.Connect(voltmeter, neuron)

nest.ConvergentConnect(noise, neuron,[1.0,-1.0], 1.0)

#show us some results! NOW!
nest.Simulate(1000.0)
nest.PrintNetwork()
pylab.show()
