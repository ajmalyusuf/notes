from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

def printprop(root):
        for existing_prop in root.getchildren():
#               if existing_prop.find('name').text == name:
#                       root.remove(existing_prop)
#                       break
                print str(existing_prop.find('name').text) + " >> " + str(existing_prop.find('value').text)


conf = ElementTree.parse('core-site.xml').getroot()
print conf
printprop(root = conf)

conf_file = open("core-site.out.xml",'w')
conf_file.write(ElementTree.tostring(conf))
conf_file.close()