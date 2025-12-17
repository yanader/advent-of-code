class Reindeer:
    def __init__(self, name, speed, movingTime, restingTime):
        self.name = name
        self.speed = speed
        self.movingTime = movingTime
        self.restingTime = restingTime
    
    def secondsInOneUnit(self):
        return self.movingTime + self.restingTime

    def distanceInOneUnit(self):
        return (self.speed * self.movingTime)
    
    def fullUnitsAndRemainingSeconds(self, seconds):
        return (seconds // self.secondsInOneUnit(), seconds % self.secondsInOneUnit())
    
    def race(self, seconds):
        full_units, remaining  = self.fullUnitsAndRemainingSeconds(seconds)
        distance = full_units * self.distanceInOneUnit()
        distance += min(remaining, self.movingTime) * self.speed
        return distance