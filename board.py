from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))
from Caro.xo import XO

class Board:
  """Quản lí bàn cờ caro."""
  
  def __init__(self,size:int=20):
    self.size=size
    self.board=[[XO.Blank for _ in range(size)] for _ in range(size)]
    
  def get_piece(self,x:int,y:int)->XO:
    """Trả về quân cờ thực sự tại một toạ độ trên bàn cờ"""
    return self.board[x][y]
  
  def in_board(self,x:int,y:int)->bool:
    """Kiểm tra xem một toạ độ có nằm trong bàn cờ hay không?"""
    return 0<=x<self.size and 0<=y<self.size
    
  def set_xo(self,x:int,y:int,Piece:XO):
    """Đặt một quân cờ tại một vị trí cụ thể trên bàn cờ"""
    self.board[x][y]=Piece
    
  def end_game_checker_vector(self,x:int,y:int,vector:tuple[int,int])->bool:
    """Kiểm tra xem đã kết thúc ván đấu chưa
      (bắt đầu dò tìm theo một phương nhất định các dòng quanh vị trí (x, y))"""
    i,count=1,1
    while True:
      a,b=i*vector[0]+x,i*vector[1]+y
      if self.in_board(a,b) and self.get_piece(x,y)!=XO.Blank \
        and self.get_piece(x,y)==self.get_piece(a,b):
        count+=1
        i+=1
      else:break
    a,b=a,b=i*vector[0]+x,i*vector[1]+y
    if self.in_board(a,b):
      if self.get_piece(a,b)==XO.Blank:k_1=True
    else:k_1=False
    i=1
    while True:
      a,b=-i*vector[0]+x,-i*vector[1]+y
      if self.in_board(a,b) and self.get_piece(x,y)!=XO.Blank \
        and self.get_piece(x,y)==self.get_piece(a,b):
        count+=1
        i+=1
      else:break
    a,b=-i*vector[0]+x,-i*vector[1]+y
    if self.in_board(a,b):
      if self.get_piece(a,b)==XO.Blank:k_2=True
    else:k_2=False
    if count>=6:return True
    elif count==5:
      if k_1 or k_2:return True
    return False
  
  def end_game_checker(self,x:int,y:int)->bool:
    """Kiểm tra xem đã kết thúc ván đấu chưa (bắt đầu dò tìm các dòng quanh vị trí (x, y))"""
    vertical_vector=(1,0)
    horizontal_vetcor=(0,1)
    diognal_vector=(1,1)
    other_dio_vector=(1,-1)
    if self.end_game_checker_vector(x,y,vertical_vector):return True
    if self.end_game_checker_vector(x,y,horizontal_vetcor):return True
    if self.end_game_checker_vector(x,y,diognal_vector):return True
    if self.end_game_checker_vector(x,y,other_dio_vector):return True
    return False
    
  def __repr__(self):
    res=""
    for i in range(self.size):
      for j in range(self.size):
        res+=self.board[i][j].transition_to_text()+' '
      res+='\n'
    return res
  
if __name__=='__main__':
  b=Board(20)
  b.set_xo(3,3,XO.X)
  b.set_xo(3,4,XO.X)
  b.set_xo(3,5,XO.X)
  b.set_xo(3,6,XO.X)
  b.set_xo(3,7,XO.X)
  print(b.end_game_checker(3,8))