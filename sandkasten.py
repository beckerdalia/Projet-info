from __future__ import print_function
from __future__ import division


data={}
data['justine']=[19,12,13,14,15]
data['hela']=[14,12,16,14,15]

def write(data):
    with open('notes.txt','w') as file:
        for nom in data:
            file.write(nom)
            for note in data[nom]:
                file.write(",{}".format(note))
            file.write("\n")

def lecture():
	data = {}
	with open('notes.txt','r') as file:
         lines = file.readlines()
         for line in lines:
             linestrip = line.strip().split(',')
             print('linestrip[0] =', linestrip[0])
             print('linestrip[1] =', linestrip[1:])
             data[linestrip[0]] = [int(l) for l in linestrip[1:]]
	return data

write(data)
data2 = lecture()

print("data", data)
print("data2", data2)
print("data == data 2 ? ", data == data2)
