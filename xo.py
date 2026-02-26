from enum import Enum,auto

REGISTRY={}
REGISTRY_SWAP={}

class XO(Enum):
  """Quản lí trạng thái của một ô trên bàn cờ caro."""
  
  X=auto()
  O=auto()
  Blank=auto()
  
  def swap(self)->'XO':
    """Đổi màu."""
    return REGISTRY_SWAP[self]
  
  def __repr__(self):
    return REGISTRY[self]
  
  def __str__(self):
    return REGISTRY[self]
  
  def transition_to_text(self):
    """Trả về kí tự string đại diện cho một quân trên bàn cờ hoặc ô trống."""
    return REGISTRY[self]
  
REGISTRY[XO.X]='X'
REGISTRY[XO.O]='O'
REGISTRY[XO.Blank]='•'

REGISTRY_SWAP[XO.X]=XO.O
REGISTRY_SWAP[XO.O]=XO.X
REGISTRY_SWAP[XO.Blank]=XO.Blank
  
if __name__=='__main__':
  print(XO.X)