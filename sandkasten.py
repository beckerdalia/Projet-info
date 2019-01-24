from __future__ import print_function
from __future__ import division


#----------------------------------
def ecriture(data, filename='notes.txt'):
    with open(filename,'w') as file:
        for nom in data:
            file.write(nom)
            for note in data[nom]:
                file.write(",{}".format(note))
            file.write("\n")

#----------------------------------
def lecture(filename='notes.txt'):
	data = {}
	with open(filename,'r') as file:
         lines = file.readlines()
         for line in lines:
             linestrip = line.strip().split(',')
             print('linestrip[0] =', linestrip[0])
             print('linestrip[1] =', linestrip[1:])
             data[linestrip[0]] = [float(l) for l in linestrip[1:]]
	return data

# quelques données pour tester
data={}
data['justine']=[19, 12,13,14,15]
data['hela']=[14,12,16, 14,15]

ecriture(data)
data2 = lecture()

print("data", data)
print("data2", data2)
print("data == data 2 ? ", data == data2)
