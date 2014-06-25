import pygame
import aspy.games
import aspy.game
import aspygame.game
import random

P_INPUT = 0
P_BUTTONS = 1
P_SLIDY = 2

class BasePuzzle:
  def __init__(self):
    self.type = P_INPUT
    self.lines = ["Placeholder puzzle.", "These words should not be displayed."]
    self.font = pygame.font.SysFont("Comic Sans MS", 20)
    self.solutions = [""]
  def draw(self, display):
    y = 20
    for line in self.lines:
      display.blit(self.font.render(line, False, (0,0,0)), (0, y))
      y += 15
  def trySolution(self, solution):
    return solution in self.solutions
class RandomPuzzle(aspy.games.Game):
  def play(self):
    aspy.game.game = puzzles[random.randint(0, len(puzzles)-1)]
class Incorrect(aspy.games.Game):
  def __init__(self, puzzle):
    aspy.games.Game.__init__(self)
    self.puzzle = puzzle
    self.font = pygame.font.SysFont("Cambria", 50)
    self.size = (500,500)
    self.correct = self.font.render("You Fail!!", False, (255,0,0))
  def select(self, pos):
    aspy.game.game = aspygame.game.MainMenu()
  def play(self):
    self.display.fill((113, 53, 12))
    self.display.blit(self.correct, (self.size[0]/2-self.correct.get_width()/2, self.size[1]/2-self.correct.get_height()/2))
class Correct(aspy.games.Game):
  def __init__(self, puzzle):
    aspy.games.Game.__init__(self)
    self.puzzle = puzzle
    self.font = pygame.font.SysFont("Cambria", 50)
    self.size = (500,500)
    self.correct = self.font.render("Correct!!", False, (0, 255, 255))
  def select(self, pos):
    aspy.game.game = aspygame.game.MainMenu()
  def play(self):
    aspy.games.Game.play(self)
    self.display.fill((113, 53, 12))
    self.display.blit(self.correct, (self.size[0]/2-self.correct.get_width()/2, self.size[1]/2-self.correct.get_height()/2))
class Puzzle(aspy.games.Game):
  def __init__(self, puzzle):
    aspy.games.Game.__init__(self)
    self.puzzle = puzzle
    self.size = (300,400)
    self.inputLine = ""
  def inputButton(self, event):
    if self.puzzle.type == P_INPUT:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
          self.inputLine = self.inputLine[0:-1]
        elif event.key == pygame.K_RETURN:
          if (self.puzzle.trySolution(self.inputLine)):
            aspy.game.game = Correct(self)
          else:
            aspy.game.game = Incorrect(self)
        elif len(event.unicode) == 1:
          self.inputLine = self.inputLine + event.unicode
  def play(self):
    aspy.games.Game.play(self)
    self.display.fill((255,255,200))
    self.puzzle.draw(self.display)
    self.display.fill((0,0,0), (0, self.size[1]-30, self.size[0], 30))
    if self.puzzle.type == P_INPUT:
      self.display.blit(self.puzzle.font.render(self.inputLine, False, (255,255,255)), (5, self.size[1]-25))
puzzles = []
