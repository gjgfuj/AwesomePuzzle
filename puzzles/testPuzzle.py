from aspygame.puzzle import *

class Puzzle(BasePuzzle):
  def __init__(self):
    BasePuzzle.__init__(self)
    self.type = P_INPUT
    self.lines = ["Hi!", "This is a test puzzle.", "This was a triumph", "You best be making a note here.", "This was a huge success."]
    self.solutions = ["Portal"]
