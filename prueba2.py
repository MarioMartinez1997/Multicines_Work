from lxml import etree as ET

channel = ET.Element('channel')
titleB = ET.SubElement(channel, 'title')
titleB.text = 'Copy of Auto Menu Feed'
description = ET.SubElement(channel, 'description')
description.text = 'Copy of Auto Menu Feed'
Item = ET.SubElement(channel, 'item')
titleS = ET.SubElement(Item, 'title')
titleS.text = 'Item01Price'
hour1 = ET.SubElement(Item, 'description')
hour1.text = 'Tire Rotation'
hour2 = ET.SubElement(Item, 'description')
hour2.text = 'Tire Rotation'
hour3 = ET.SubElement(Item, 'description')
hour3.text = 'Tire Rotation'
hour4 = ET.SubElement(Item, 'description')
hour4.text = 'Tire Rotation'
hour5 = ET.SubElement(Item, 'description')
hour5.text = 'Tire Rotation'
rating = ET.SubElement(Item, 'description')
rating.text = 'Tire Rotation'

#   print(ET.tostring(root, pretty_print=True, xml_declaration=True))
tree = ET.ElementTree(channel)
tree.write('output.xml', pretty_print=True, xml_declaration=True)