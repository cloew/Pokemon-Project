from Battle.battle_view_controller import BattleViewController
from Trainer.computer_trainer import ComputerTrainer
from Trainer.human_trainer import HumanTrainer

from Trainer.trainer_factory import TrainerFactory

trainer = HumanTrainer()
TrainerFactory.loadFromXML(trainer, "Chris")
trainer2 = ComputerTrainer()
TrainerFactory.loadFromXML(trainer2, "Eric")

BattleViewController().begin(trainer, trainer2)

