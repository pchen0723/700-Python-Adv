class Thing:
    number_of_things = 0
    def __init__(self):
        Thing.number_of_things += 1
        self.thing_no = self.number_of_things
print (Thing().thing_no)