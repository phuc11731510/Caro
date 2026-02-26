from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))
from typing import NamedTuple
from Caro.board import Board
from Caro.xo import XO

class WinNot_Turn(NamedTuple):
  WinNot:bool
  Turn:XO

class Game:
  """Quản lí trạng thái trò chơi (liên quan tới người chơi và thắng thua)"""
  
  def __init__(self,turn:XO=XO.X,board:Board=Board()):
    self.board=board
    self.size=board.size
    self.turn=turn
    self.winner=None
    
  def winer_checker(self,x:int,y:int)->WinNot_Turn:
    """Kiểm tra xem ván cờ có ai thắng không và trả về (True/False, self.turn)"""
    if self.board.end_game_checker(x,y):
      return WinNot_Turn(True,self.turn)
    return WinNot_Turn(False,self.turn)
    
  def make_move(self,x:int,y:int):
    """Thực hiện hoàn chỉnh một nước đi và chờ nước đi tiếp theo trong bàn cờ"""
    if self.winner==None:
      self.board.set_xo(x,y,self.turn)
      res=self.winer_checker(x,y)
      if res.WinNot:
        print(f"{res.Turn} đã thắng")
        self.winner=self.turn
      else:
        self.switch_turn()
    else:
      print("Đã có người chiến thắng")
  
  def switch_turn(self):
    """Đổi trạng thái lượt đi trong ván cờ"""
    if self.turn==XO.O:self.turn=XO.X
    else:self.turn=XO.O
    
  def __repr__(self):
    res=self.board.__repr__()
    res+=f"Lượt đi: {self.turn.transition_to_text()}"
    return res
    
if __name__=='__main__':
  G=Game()
  print(G)