class TiredStudent:
    """I'm so tired
    9/19 CS160 so tired today. We are talking about constructor parameters!
    """
    def __init__(self,isTired=True, hoursOfSleep=0, age=-1):
        self.isTired = isTired
        self.hoursOfSleep = hoursOfSleep
        self.age = age
    def sleepReport(self):
        slept = "Nice job! you got enough sleep!"
        if self.age < 0 or self.age <= 18:
            # age is not defined by user, assume user is child, or check if child
            if self.hoursOfSleep < 9:
                return "Not enough sleep. Get at least 9 hours of sleep per night."
            else:
                # got enough sleep!!
                return slept
        else:
            # student is not child
            if self.hoursOfSleep < 8:
                return "Not enough sleep. Get at least 8 hours of sleep per night."
            else:
                return  slept
    
if __name__=="__main__":
    tiredInput  = input("Are you tired? ")
    hoursInput  = int(input("How many hours of sleep did you get? "))
    ageInput    = int(input("What is your age? "))
    if tiredInput.lower().find("n") != -1:
        # if the input contains n...
        tiredInput = False
    else:
        tiredInput = True
    
    student1 = TiredStudent(tiredInput, hoursInput, ageInput)
    print(student1.sleepReport())