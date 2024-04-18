#Therese Burns & Anastacia Aguirre

#Part D: Fabric Class

class Fabric:
    def __init__(self, COO, color):
        self.COO= COO
        self.color= color

    def __str__(self):
        return self.COO + "(" + self.color + ")"

shirt1= Fabric("China", "Green")

print(shirt1)