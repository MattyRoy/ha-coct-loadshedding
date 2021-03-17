from datetime import datetime

class LoadsheddingSlot:
  def __init__(self, start, end):
    self.start = datetime.strptime(start, "%H:%M").time()
    self.end = datetime.strptime(end, "%H:%M").time()
    
  def isSlotActive(self, now):
    return self.start <= now and now <= self.end