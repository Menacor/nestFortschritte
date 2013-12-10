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

pylab.show()

