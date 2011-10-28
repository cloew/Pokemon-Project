import xml.etree.ElementTree

from Battle.Attack.attackfactory import AttackFactory

def getAttack(tree, name):
    for attack in tree.getiterator("attack"):
        if attack.find("name").text == name:
            return attack

            
statKeys = ["HP", "ATK", "DEF", "SPD", "SATK", "SDEF"]

file = open("resources/pokedex.xml", 'r')
tree =  xml.etree.ElementTree.ElementTree(file=file)

print  xml.etree.ElementTree.tostring(tree.getroot())
print "\n"
for pokemon in tree.getiterator("pokemon"):
  pokemon = xml.etree.ElementTree.ElementTree(pokemon)
  print pokemon.find("species").text
  
  print "Types"
  types = pokemon.find("types")
  for type in types.getiterator("type"):
    print type.text,
  print ""
  
  baseStats = pokemon.find("baseStats")
  for stat in statKeys:
    print stat, baseStats.find(stat).text
  
  print ""
  
file.close()

file = open("resources/temp", 'r')

attack = AttackFactory.loadFromXML(file)

print attack.name
print attack.type
print attack.hitDelegate.chanceToHit
print attack.damageDelegate
print attack.effectDelegates[0]