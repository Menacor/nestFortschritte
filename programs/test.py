import nest
import nest.topology as tp
import csv


# function that returns all neurons in a list
def getNeurons(csvfile):
  
  neurons = []

  # get information about the neuron sets from the respective csv file
  with open(csvfile, "r") as nsfile:
  
    nsreader = csv.reader(nsfile, delimiter=";")
  
    for neuronSet in nsreader:
      neurons = nest.Create("iaf_neuron", int(neuronSet[2]))

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

# read csv files from console


# print all information
neurons =  getNeurons("../csv/neuronsets.csv")
print ("Neuronen:")
print neurons
connections = getConnections("../csv/connections.csv")
print ("\nVerbindungen:")
print ( connections)
