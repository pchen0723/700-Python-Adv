class Cloud:
    # __setattr__: same as cloud.color='pink'
    def __setattr__(self, name, value):
        self.__dict__[name] = value.upper()

cloud = Cloud()
cloud.color = 'pink'
print ('cloud.color:', cloud.color)