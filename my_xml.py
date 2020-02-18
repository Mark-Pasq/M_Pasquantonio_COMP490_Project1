#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 3
# Filename: my_xml.py

"""
These lines of code parsed the .xml code so it could be readable.  It was needed to write other
functions throughout the testing folder..
"""
import xml.dom.minidom


with open('feed.xml') as xml_data:
    xml = xml.dom.minidom.parseString(xml_data.read())  # or xml.dom.minidom.parseString(xml_string)
    xml_pretty_str = xml.toprettyxml()
print(xml_pretty_str)


# from xml.etree import ElementTree
#
# """
# This function indent() sets up the element tree to be able to view humanly, the output
# of the data from the Stack Overflow Jobs link for Sprint 3.  It helped to identify
# the necessary column headers for the new table 'RSSentries'.  I decided not to use it,
# but to leave it as an example.  It was saved for prosperity.
# """
#
# def indent(elem, level=0):
#     i = "\n" + level * "    "
#     j = "\n" + (level - 1) * "    "
#     if len(elem):
#         if not elem.text or not elem.text.strip():
#             elem.text = i + "    "
#         if not elem.tail or not elem.tail.strip():
#             elem.tail = i
#         for subelem in elem:
#             indent(subelem, level + 1)
#         if not elem.tail or not elem.tail.strip():
#             elem.tail = j
#     else:
#         if level and (not elem.tail or not elem.tail.strip()):
#             elem.tail = j
#     return elem
#
#
# root = ElementTree.parse('feed.xml').getroot()
# indent(root)
# ElementTree.dump(root)
