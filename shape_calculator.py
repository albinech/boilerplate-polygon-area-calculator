class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height
  
  def set_width(self,w):
    self.width = w
  
  def __str__(self):
    return f'{type(self).__name__}(width={self.width}, height={self.height})'
    
  def set_height(self,h):
    self.height = h
  
  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = (self.width+self.height)*2
    return perimeter

  def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2)**0.5
        return diagonal
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    
    patt = self.width*'*'+'\n'
    patt = self.height * patt
    return patt

  def get_amount_inside(self,shape):
    area_guest = shape.get_area()
    area_home = self.get_area()
    total = area_home // area_guest
    return total


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)

    def __str__(self):
        return f'{type(self).__name__}(side={self.width})'

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)