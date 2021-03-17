from .slot import LoadsheddingSlot

class LoadsheddingStage:
    def __init__(self, stage):
        self.days = []
        for day in range(len(stage)):
            slots = []
            for slot in range(len(stage[day])):
                slots.append(LoadsheddingSlot(**stage[day][slot]))
            self.days.append(slots)

    def isCurrentlyLoadshedding(self, now):
        slots = self.days[now.date.day-1]
        active = False
        for slot in range(len(slots)):
            active = active or slots[slot].isSlotActive(now.time)
        return active
    
    def loadsheddingSlots(self, now):
        return self.days[now.date.day - 1]