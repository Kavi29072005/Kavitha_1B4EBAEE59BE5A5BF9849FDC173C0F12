class player:
  def play(self):
    print("The player is playing cricket")

class batsman(player):
  def play(self):
    print("The Batsman is Batting")

class bowler(player):
  def play(self):
    print("The Bowler is Bowling")

bman=batsman()
bow=bowler()
bman.play()
bow.play()
  