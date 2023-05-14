class Musician :
   def __init__(self,name) :
      self.name = name

   def __str__(self):
    return f'My name is {self.name} and I play {self.inst}'
   
   def __repr__(self):
      return f'{self.tool} instance. Name = {self.name}'
   
   def get_instrument(self):
    return f'{self.inst}'
   

class Guitarist(Musician):
   inst ='guitar'
   tool='Guitarist'
   def play_solo(self):
     return 'face melting guitar solo'
   

class Bassist(Musician):
    inst ='bass'
    tool='Bassist'
    def play_solo(self):
     return 'bom bom buh bom'
    

class Drummer(Musician):
    inst ='drums'
    tool='Drummer'
    def play_solo(self):
     return 'rattle boom crash'
    

class Band():
   def __init__(self,name,members) :
      self.name = name
      self.members = members
   def play_solos(self):
    member_list=[]
    for i in self.members:
      member_list.append(i.play_solo())
    return member_list