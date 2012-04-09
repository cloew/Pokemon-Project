from Pokemon.pokemon_battle_delegate_factory import PokemonBattleDelegateFactory
from Pokemon.pokemon_battle_delegate import PokemonBattleDelegate
from Pokemon.pokemon import Pokemon

from Battle.Attack.attackfactory import AttackFactory
from Battle.Attack.DamageDelegates.damage_delegatefactory import DamageDelegateFactory

parent = Pokemon()
parent.level = 1

delegate = PokemonBattleDelegate()
delegate.parent = parent

PokemonBattleDelegateFactory.loadPokedexBattleInfoDB(delegate, "BULBASAUR")

print delegate.types
print delegate.stats

print "\n"

attack = AttackFactory.loadFromDB("FOCUS ENERGY")
print attack.name, attack.type
print attack.damageDelegate
#print attack.damageDelegate.power, attack.damageDelegate.isPhysical, attack.damageDelegate.parent
print attack.hitDelegate
#print attack.hitDelegate.chanceToHit, attack.hitDelegate.parent
print attack.speedDelegate.priority
print attack.critDelegate.base
print attack.effectDelegates