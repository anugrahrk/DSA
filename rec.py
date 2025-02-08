def f(self,name,count=0):
    if count==4:
        return
    # self.name=name
    print(name)
    f(name,count+1)
f('Abhi',1)
    