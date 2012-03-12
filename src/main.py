from Battle.battle_view_controller import BattleViewController
from Trainer.computer_trainer import ComputerTrainer
from Trainer.human_trainer import HumanTrainer

from Trainer.trainer_factory import TrainerFactory

file = open("resources/trainer-chris", 'r')
file2 = open("resources/trainer-eric", 'r')

trainer = HumanTrainer()
TrainerFactory.loadFromXML(trainer, "Chris")
trainer2 = ComputerTrainer()
TrainerFactory.loadFromXML(trainer2, "Eric")

file.close()
file2.close()

BattleViewController().begin(trainer, trainer2)

