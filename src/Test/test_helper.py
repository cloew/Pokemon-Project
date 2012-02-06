from Battle.battle_side import BattleSide
from Battle.pkmn_battle_wrapper import PkmnBattleWrapper
from Trainer.trainer import Trainer
from Pokemon.pokemon import Pokemon


def buildPokemonBattleWrapper():
    """  Builds a Pokemon Battle Wrapper """
    trainer = Trainer()
    pokemon = Pokemon("BULBASAUR")
    trainer.beltPokemon = [pokemon]
    
    side = BattleSide(trainer)
    wrapper = PkmnBattleWrapper(side)
    wrapper.pkmn = pokemon
    
    return wrapper