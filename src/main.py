from Battle.battle_view_controller import BattleViewController
from Trainer.computer_trainer import ComputerTrainer
from Trainer.human_trainer import HumanTrainer

file = open("resources/trainer-chris", 'r')
file2 = open("resources/trainer-eric", 'r')

trainer = HumanTrainer().loadFromFile(file)
trainer2 = ComputerTrainer().loadFromFile(file2)

file.close()
file2.close()

BattleViewController().begin(trainer, trainer2)

