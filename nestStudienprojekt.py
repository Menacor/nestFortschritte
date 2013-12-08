import nest
import nest.topology as tp
import csv

#initiallizing list elements for neuron sets and connections
neuronSets = []
connections = []

inputSets = raw_input("Specify a file name for the neuronSets: ")
inputConnections = raw_input("Specify a file name for the connections: ")

neuronReader = csv.reader(open(inputSets, "rb")) 
connectionsReader = csv.reader(open(inputConnections, "rb")) 

for row in neuronReader:
 neuronSets.append(row)

for row in connectionsReader:
 connections.append(row)

print neuronSets
print
print connections
