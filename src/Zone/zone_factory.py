from resources.resource_manager import GetResourcePath
from resources.tags import Tags

from Zone.tile_content import TileContent
from Zone.zone import Zone
from Zone.Person.person_factory import LoadPeopleFromZoneXML

import xml.etree.ElementTree

class ZoneFactory:
    """ Factory to build Zones """
    tree = None
    
    @staticmethod
    def getZone(name):
        """ Return the zone with the given name """
        zoneXML = ZoneFactory.getZoneXML(name)
        if zoneXML is not None:
            return ZoneFactory.loadFromXML(zoneXML)
        return None
    
    @staticmethod
    def loadFromXML(tree):
        """ Loads a Zone object from a file """
        rows = int(tree.findtext(Tags.rowsTag))
        columns = int(tree.findtext(Tags.columnsTag))
        tileFilename = tree.findtext(Tags.tileTag)
        zone = Zone(rows, columns, tileFilename)
        ZoneFactory.loadContentsFromXML(tree, zone.tiles)
        zone.people = LoadPeopleFromZoneXML(tree, zone.tiles)
        return zone
        
    @staticmethod
    def loadContentsFromXML(tree, tiles):
        """ Loads a Zone object from a file """
        contentsElement = tree.find(Tags.contentsTag)
        if contentsElement is None:
            return
            
        for contentElement in contentsElement.findall(Tags.contentTag):
            row = int(contentElement.findtext(Tags.rowTag))
            column = int(contentElement.findtext(Tags.columnTag))
            image = contentElement.findtext(Tags.imageTag)
            
            content = TileContent(image)
            tiles[row][column].contents = content
        
    @staticmethod
    def loadFromDB():
        """ AAAAAAAAAGGGGGGGGGGGHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!! """
                
    @staticmethod
    def copy(toCopy):
        """ Copies the Given Pkmn """
        zone = Zone()
        
        return zone
        
    @staticmethod
    def getZoneTree():
        """ Opens the zone.xml file as an element tree """
        if ZoneFactory.tree is not None:
            return ZoneFactory.tree
        
        with open(GetResourcePath("zone.xml"), 'r') as zonedex:
            ZoneFactory.tree = xml.etree.ElementTree.ElementTree(file=zonedex)
        return ZoneFactory.tree
        
    @staticmethod
    def getZoneXML(name):
        """ Returns the XML tree for the zone with the name given """
        tree = ZoneFactory.getZoneTree()
        
        for zoneXML in tree.getiterator(Tags.zoneTag):
            if zoneXML.findtext(Tags.nameTag) == name:
                return zoneXML
        else:
            return None 