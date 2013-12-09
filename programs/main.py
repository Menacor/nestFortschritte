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


# ============= begin with the program ============= #

# read csv files from console
neuronCSV = raw_input("Specify a filename for the neuronSets: ")
connectionsCSV = raw_input("Specify a filename for the connections: ")

print

# ../csv/neuronsets.csv
# ../csv/connections.csv

# print all information
neurons =  getNeurons(neuronCSV)
print ("Neuronen:")
print neurons
connections = getConnections(connectionsCSV)
print ("\nVerbindungen:")
print ( connections)
