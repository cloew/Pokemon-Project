from resources.resource_manager import GetResourcePath

class XmlFactory:
    """ Represents an XML Factory """
    
    def __init__(self, filename):
        """ Initialize the XML Factory """
        self.filename = GetResourcePath(filename)
        self.__tree = None
        
    @property
    def tree(self):
        """ Return the current tree """
        if self.__tree is None:
            with open(self.filename, 'r') as xmlFile:
                self.__tree = ElementTree(file=xmlFile)
        return self.__tree
        
    def saveXMLTree(self):
        """ Save the XML Tree """
        xmlString = tostring(self.tree.getroot())
        
        xmlString = xmlString.replace('\n', '')
        xmlString = xmlString.replace('\t', '')
        xmlString = xmlString.replace('ns0:', '')
        xmlString = xmlString.replace(':ns0', '')
        
        xml = parseString(xmlString)
        prettyXMLString = xml.toprettyxml()
        
        with open(self.filename, 'w') as file:
            file.write(prettyXMLString)