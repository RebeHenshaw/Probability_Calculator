import copy
import random

class Hat:
  def __init__(self, **kwargs):
    """Create a hat object with unspecified options for colored balls and number of each ball."""
    self.contents = self.converttolist(**kwargs)

  
  def converttolist(self, **kwargs):
    """Convert dictionary items to list."""
    return [key for key, value in kwargs.items() for i in range(value)] 
    

  def draw(self, number):
    """Remove balls from hat."""
    if number > len(self.contents):
      return self.contents
    drawn_balls = [] # This seemed too complicated for a list comp
    for each in range(number):
      ball = random.choice(self.contents)
      drawn_balls.append(ball)
      self.contents.remove(ball)
    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  """Repeat experiment to return probability"""
  success = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls_ret = hat_copy.draw(num_balls_drawn)
    color_count = 0
    for color in expected_balls:
      if balls_ret.count(color) >= expected_balls[color]:
          color_count += 1
    if color_count == len(expected_balls):
      success += 1
    
  return success / num_experiments
