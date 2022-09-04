class House():
    def __init__(self, owner, color, material, roof, house_size, construction_year, floor_number, number_of_rooms, number_of_stairs, cost, water, gas, electricity ):
        self.owner = owner
        self.color = color
        self.material = material
        self.roof = roof
        self.house_size = house_size
        self.construction_year = construction_year
        self.floor_number = floor_number
        self.number_of_rooms = number_of_rooms
        self.number_of_stairs = number_of_stairs
        self.cost = cost
        self.water = water
        self.gas = gas
        self.electricity = electricity

    def ShowInfo(self):
        print( "Владелец -> " + self.owner)
        print( "Цвет ->" + self.color)
        print( "Материал ->" + self.material)
        print( "Сколько ярусов крыши ->" + self.roof)
        print( "Размер дома ->" + self.house_size)
        print( "Год постройки ->" + self.construction_year)
        print( "Сколько этажей ->" + self.floor_number)
        print( "Сколько комнат ->" + self.number_of_rooms)
        print( "Сколько лестниц ->" + self.number_of_stairs)
        print( "Цена ->" + self.cost)

    def wt(self):
        if(self.water == "On"):
            self.water == "Off"
        else:
            self.water == "On"

    def gas(self):
        if(self.gas == "On"):
            self.gas == "Off"
        else:
            self.gas == "On"

    def elec(self):
        if(self.electricity == "On"):
            self.electricity == "Off"
        else:
            self.electricity == "On"


FirstHouse = House("Olezha<З", "Orange", "Brick", "1", "100x80", "1995", "3", "15", "2", "68.000$", "On", "On", "On")
SecondHouse = House("Maxim", "White", "Brick", "2", "90x70", "1990", "2", "10", "1", "60.000$", "On", "Off", "On")

FirstHouse.ShowInfo()
print("----------------")
SecondHouse.ShowInfo()
