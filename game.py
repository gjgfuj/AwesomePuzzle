import pygame
pygame.init()
import aspy.games
import aspy.loader
import aspy.game
import aspygame.puzzle
class InitLoader(aspy.loader.Loader):
  def loadpuzzles(self):
    import aspygame.puzzles.testPuzzle
    aspygame.puzzle.puzzles.append(aspygame.puzzle.Puzzle(aspygame.puzzles.testPuzzle.Puzzle()))
    return "Puzzles Loaded"
  def loadmenu(self):
    return "Menu Loaded"
  def __init__(self, menu):
    aspy.loader.Loader.__init__(self, [self.loadpuzzles, self.loadmenu], menu)
class MainMenu(aspy.games.Menu):
  def options(self):
    aspy.game.game = aspy.games.OptionsMenu(MainMenu)
  def randompuzzle(self):
    aspy.game.game = aspygame.puzzle.RandomPuzzle()
  def selectpuzzle(self):
    aspy.game.game = aspygame.puzzle.PuzzleSelect()
  def __init__(self):
    aspy.games.Menu.__init__(self)
    self.addmenuitem("Random Puzzle", self.randompuzzle)
    self.addmenuitem("Puzzle Select", self.selectpuzzle)
    self.addmenuitem("", self.nothing)
    self.addmenuitem("Options", self.options)
    self.addmenuitem("", self.nothing)
    self.addmenuitem("Quit", self.exit)
def setup():
  aspy.game.game = aspy.games.Load(InitLoader(MainMenu()))
