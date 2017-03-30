import pandas as pd
import numpy as np
from lxml import etree as ET

my_data = pd.read_excel('CARTELERAS 25sept-01oct.xls', 'Cci', skiprows=8)
my_data[1] = my_data[1].astype('str')
movieTitle = my_data['PELICULA'][0:1].values
abc = my_data['PELICULA'].tolist()  # me da una lista de la columna ver PRINT()

my_data[1] = my_data[1].replace('nan', '--------')
my_data[1] = my_data[1].replace(np.nan, '--------')
my_data[2] = my_data[2].replace('nan', '--------')
my_data[2] = my_data[2].replace(np.nan, '--------')
my_data[3] = my_data[3].replace('nan', '--------')
my_data[3] = my_data[3].replace(np.nan, '--------')
my_data[4] = my_data[4].replace('nan', '--------')
my_data[4] = my_data[4].replace(np.nan, '--------')
my_data[5] = my_data[5].replace('nan', '--------')
my_data[5] = my_data[5].replace(np.nan, '--------')
print(my_data)


#mHour1 = my_data[1][0:1]
mHour1 = my_data[1]
mHour2 = my_data[2]
mHour3 = my_data[3]
mHour4 = my_data[4]
mHour5 = my_data[5]
# print(my_data[5])
#function range for loop


#print(my_data.info())
# print(str(movieTitle))
# print(str(hour1))
#print(hour2)
# print(hour3)
# print(hour4)
# print(str(mHour5))
# print (movieTitle)
# print(abc)


channel = ET.Element('channel')
titleB = ET.SubElement(channel, 'title')
titleB.text = 'Copy of Auto Menu Feed'
description = ET.SubElement(channel, 'description')
description.text = 'Copy of Auto Menu Feed'
Item = ET.SubElement(channel, 'item')
for i in range(0,12,2):
    titleS = ET.SubElement(Item, 'title')
    titleS.text = abc[i]
    hour1 = ET.SubElement(Item, 'description')
    hour1.text = str(mHour1[i:i+1])[4:14]
    hour2 = ET.SubElement(Item, 'description')
    hour2.text = str(mHour2[i:i+1])[4:14]
    hour3 = ET.SubElement(Item, 'description')
    hour3.text = str(mHour3[i:i+1])[4:14]
    hour4 = ET.SubElement(Item, 'description')
    hour4.text = str(mHour4[i:i+1])[4:14]
    hour5 = ET.SubElement(Item, 'description')
    hour5.text = str(mHour5[i:i+1])[4:14]
    rating = ET.SubElement(Item, 'description')
    rating.text = "-"

#   print(ET.tostring(root, pretty_print=True, xml_declaration=True))
tree = ET.ElementTree(channel)
tree.write('output.xml', pretty_print=True, xml_declaration=True)
#print(my_data.info())
#print(my_data.describe())
