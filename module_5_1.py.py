class house:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors
    def go_to (self, new_floor):
        self.new_floor = new_floor

        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не сущесвтует')
        else:
            for i in range(1, new_floor+1):
                print(i)

house1 = house('olympus', 30)
house2 = house('Viktoria', 3)

house1.go_to(3)
house2.go_to(5)
