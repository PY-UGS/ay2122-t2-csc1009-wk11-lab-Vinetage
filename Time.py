class clockTime:
    # Constructor
    def __init__(self):
        self.hour = 0
        self.minutes = 0
        self.seconds = 0
    # Setters
    def setHours(self,hours):
        self.hour = hours
    # Setters
    def setMinutes(self,minutes):
        self.minutes = minutes
    # Setters
    def setSeconds(self,seconds):
        self.seconds = seconds
    # Set all
    def setTime(self,hours,minutes,seconds):
        self.setHours(hours)
        self.setMinutes(minutes)
        self.setSeconds(seconds)
    # Getter show time
    def showTime(self):
        return str(self.hour) + ":" + str(self.minutes) + ":" + str(self.seconds)

# Main
if __name__=="__main__":
    # Create clock time object
    clockObj = clockTime()
    # Ask user for hour, min, sec
    hour = int(input("Input hour value: "))
    minute = int(input("Input minute value: "))
    seconds = int(input("Input seconds value: "))
    clockObj.setTime(hour,minute,seconds)
    print("Time: ", clockObj.showTime())
