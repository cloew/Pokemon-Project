from Battle.battle_view_controller import BattleViewController
from Trainer.computer_trainer import ComputerTrainer
from Trainer.human_trainer import HumanTrainer

from Trainer.trainer_factory import TrainerFactory

trainer = TrainerFactory.loadFromXML("Chris", TrainerFactory.HUMAN)
trainer2 = TrainerFactory.loadFromXML("Eric", TrainerFactory.COMPUTER)

BattleViewController().begin(trainer, trainer2)

