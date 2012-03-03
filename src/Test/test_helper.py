from Battle.battle_side import BattleSide
from Battle.pkmn_battle_wrapper import PkmnBattleWrapper
from Battle.Actions.battle_action import BattleAction
from Battle.Actions.attack_action import AttackAction
from Battle.Actions.action_lock import ActionLock
from Battle.Attack.attackfactory import AttackFactory
from Trainer.trainer import Trainer
from Pokemon.pokemon import Pokemon


def BuildPokemonBattleWrapper(pkmn = "BULBASAUR",  trainer = Trainer()):
    """  Builds a Pokemon Battle Wrapper """
    pokemon = Pokemon(pkmn)
    trainer.beltPokemon = [pokemon]
    
    side = BattleSide(trainer)
    wrapper = PkmnBattleWrapper(side)
    wrapper.pkmn = pokemon
    
    return wrapper
    
def BuildBattleAction(user = BuildPokemonBattleWrapper(), priority = 0):
    """ Builds a Battle Action """
    return BattleAction(user, priority)
    
def BuildAttackAction(user = BuildPokemonBattleWrapper(), target = BuildPokemonBattleWrapper(), attack = AttackFactory.getAttackAsNew("TACKLE")):
    """ Builds an Attack Action """
    return AttackAction(attack, user, target)
    
def BuildActionLock(user = BuildPokemonBattleWrapper(), attackAction = BuildAttackAction(user = BuildPokemonBattleWrapper())):
    """ Builds an Action Lock """
    attackAction.user = user
    turns = 3
    return ActionLock(user, attackAction, turns)
    
    