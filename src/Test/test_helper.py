from Battle.battle_side import BattleSide
from Battle.pkmn_battle_wrapper import PkmnBattleWrapper
from Trainer.trainer import Trainer
from Pokemon.pokemon import Pokemon


def BuildPokemonBattleWrapper(pkmn = "BULBASAUR"):
    """  Builds a Pokemon Battle Wrapper """
    trainer = Trainer()
    pokemon = Pokemon(pkmn)
    trainer.beltPokemon = [pokemon]
    
    side = BattleSide(trainer)
    wrapper = PkmnBattleWrapper(side)
    wrapper.pkmn = pokemon
    
    return wrapper