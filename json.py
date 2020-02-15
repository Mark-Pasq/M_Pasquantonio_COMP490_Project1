# import lxml.etree as etree
#
# x = etree.parse('C:/Users/mpasq/OneDrive/Desktop/feed.xml')
# print(etree.tostring(x, pretty_print=True))

# from xml.dom import minidom
#
# xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
# with open("C:/Users/mpasq/OneDrive/Desktop/feed.xml", "w", encoding='utf-8') as f:
#     f.write(xmlstr)


# from bs4 import BeautifulSoup
#
# x = 'C:/User/mpasq/OneDrive/Desktop/feed.xml'
#
# print(BeautifulSoup(x, "xml").prettify())


import xml.dom.minidom
with open('feed.xml') as xml_data:
    xml = xml.dom.minidom.parseString(xml_data.read())  # or xml.dom.minidom.parseString(xml_string)
    xml_pretty_str = xml.toprettyxml()
print(xml_pretty_str)
