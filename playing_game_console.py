from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from Caro.game import Game

def main():
  G=Game()
  G.make_move(1,1)
  G.make_move(0,0)
  G.make_move(1,2)
  G.make_move(0,0)
  G.make_move(1,3)
  G.make_move(0,0)
  G.make_move(1,4)
  G.make_move(0,0)
  G.make_move(1,5)
  G.make_move(4,5)
  
  
if __name__=='__main__':
  main()