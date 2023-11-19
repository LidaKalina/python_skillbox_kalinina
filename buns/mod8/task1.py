class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        if len(coordinates) == 2 and all(type(item) is int for item in coordinates):
            self._coordinates = coordinates
        else:
            raise TypeError('Expected list of int values')

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if type(speed) is int:
            self._speed = speed
        else:
            raise TypeError('Expected int value')

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if type(brand) is str:
            self._brand = brand
        else:
            raise TypeError('Expected str value')

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if type(year) is int:
            self._year = year
        else:
            raise TypeError('Expected int value')

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if type(number) is str:
            self._number = number
        else:
            raise TypeError('Expected str value')

    def __str__(self) -> str:
        '''
           Представление всей информации для вывода в методе print()
        '''

        return ('Coordinates: {}\n'
                'Speed: {}\n'
                'Brand: {}\n'
                'Year: {}\n'
                'Number: {}').format(self._coordinates,
                                     self._speed,
                                     self._brand,
                                     self._year,
                                     self._number)


def is_in_area(self, pos_x, pos_y, length, width) -> bool:
    '''
    Присутствие транспортного средства в пределах заданнй области
    pos_x, pos_y - координата левого верхнего угла области
    length, width - длина и ширина области
    '''
    pass
    x, y = self._coordinates
    if x >= pos_x and x <= pos_x + length:
        if y >= pos_y and y <= pos_y + width:
            return True
    else:
        return False


class Passenger:
    def __init__(self, passengers_capacity, number_of_passengers):
        self._passengers_capacity = passengers_capacity
        self._number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if type(passengers_capacity) is int:
            self._passengers_capacity = passengers_capacity
        else:
            raise TypeError('Expected int value')

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if type(number_of_passengers) is int:
            self._number_of_passengers = number_of_passengers
        else:
            raise TypeError('Expected int value')


class Cargo:
    def __init__(self, carrying, cargo_size):
        self._carrying = carrying
        self._cargo_size = cargo_size

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, carrying):
        if type(carrying) is int:
            self._carrying = carrying
        else:
            raise TypeError('Expected int value')

    @property
    def cargo_size(self):
        return self._cargo_size

    @cargo_size.setter
    def cargo_size(self, cargo_size):
        if type(cargo_size) is int:
            self._cargo_size = cargo_size
        else:
            raise TypeError('Expected int value')


class Plane(Transport):
    def __init__(self, height, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if type(height) is int:
            self._height = height
        else:
            raise TypeError('Expected int value')


class Auto(Transport):
    def __init__(self, engine_type, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
        self._engine_type = engine_type

    @property
    def engine_type(self):
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        if type(engine_type) is str:
            self._engine_type = engine_type
        else:
            raise TypeError('Expected str value')


class Ship(Transport):
    def __init__(self, port, name, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
        self._port = port
        self._name = name

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        if type(port) is str:
            self._port = port
        else:
            raise TypeError('Expected str value')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) is str:
            self._name = name
        else:
            raise TypeError('Expected str value')


class Car(Auto):
    def __init__(self, gearbox_type, engine_type, coordinates, speed, brand, year, number):
        super().__init__(engine_type, coordinates, speed, brand, year, number)
        self._gearbox_type = gearbox_type

    @property
    def gearbox_type(self):
        return self._gearbox_type

    @gearbox_type.setter
    def gearbox_type(self, gearbox_type):
        if type(gearbox_type) is str:
            self._gearbox_type = gearbox_type
        else:
            raise TypeError('Expected str value')


class Bus(Auto, Passenger):
    def __init__(self, engine_type, coordinates, speed, brand, year, number,
                 passengers_capacity, number_of_passengers):
        super().__init__(coordinates, speed, brand, year, number, engine_type)
        super().__init__(passengers_capacity, number_of_passengers)

    def bus_boarding(self):
        if self.number_of_passengers <= self.passengers_capacity:
            return 'Bus boarding successfully'
        else:
            return ('Bus boarding failed. Left {} passengers'
                    .format(self.number_of_passengers - self.passengers_capacity))


class CargoAuto(Auto, Cargo):
    def __init__(self, engine_type, coordinates, speed, brand, year, number,
                 carrying, cargo_size):
        super().__init__(coordinates, speed, brand, year, number, engine_type)
        super().__init__(carrying, cargo_size)

    def cargo_auto_loading(self):
        if self.cargo_size <= self.carrying:
            return 'Loading onto a cargo auto successfully'
        else:
            return ('Loading onto a cargo auto failed. Overload - {}'
                    .format(self.cargo_size - self.carrying))


class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port, name,
                 type_of_boat):
        super().__init__(port, name, coordinates, speed, brand, year, number)
        self._type_of_boat = type_of_boat

    @property
    def type_of_boat(self):
        return self._type_of_boat

    @type_of_boat.setter
    def type_of_boat(self, type_of_boat):
        if type(type_of_boat) is str:
            self._type_of_boat = type_of_boat
        else:
            raise TypeError('Expected str value')


class PassengerShip(Ship, Passenger):
    def __init__(self, port, name, coordinates, speed, brand, year, number,
                 passengers_capacity, number_of_passengers):
        super().__init__(port, name, coordinates, speed, brand, year, number)
        super().__init__(passengers_capacity, number_of_passengers)

    def ship_boarding(self):
        if self.number_of_passengers <= self.passengers_capacity:
            return 'Ship boarding successfully'
        else:
            return ('Sip boarding failed. Left {} passengers'
                    .format(self.number_of_passengers - self.passengers_capacity))


class CargoShip(Ship, Cargo):
    def __init__(self, port, name, coordinates, speed, brand, year, number,
                 carrying, cargo_size):
        super().__init__(port, name, coordinates, speed, brand, year, number)
        super().__init__(carrying, cargo_size)

    def cargo_ship_loading(self):
        if self.cargo_size <= self.carrying:
            return 'Loading onto a cargo ship successfully'
        else:
            return ('Loading onto a cargo ship failed. Overload - {}'
                    .format(self.cargo_size - self.carrying))


class PassengerPlane(Plane, Passenger):
    def __init__(self, height, coordinates, speed, brand, year, number,
                 passengers_capacity, number_of_passengers):
        super().__init__(height, coordinates, speed, brand, year, number)
        super().__init__(passengers_capacity, number_of_passengers)

    def plane_boarding(self):
        if self.number_of_passengers <= self.passengers_capacity:
            return 'Plane boarding successfully'
        else:
            return ('Plain boarding failed. Left {} passengers'
                    .format(self.number_of_passengers - self.passengers_capacity))


class CargoPlane(Plane, Cargo):
    def __init__(self, height, coordinates, speed, brand, year, number,
                 carrying, cargo_size):
        super().__init__(height, coordinates, speed, brand, year, number)
        super().__init__(carrying, cargo_size)

    def cargo_plane_loading(self):
        if self.cargo_size <= self.carrying:
            return 'Loading onto a cargo plane successfully'
        else:
            return ('Loading onto a cargo plane failed. Overload - {}'
                    .format(self.cargo_size - self.carrying))


class Seaplane(Plane, Ship):
    def __init__(self, height, port, name, coordinates, speed, brand, year, number,
                 runway_length):
        super().__init__(height, coordinates, speed, brand, year, number)
        super().__init__(port, name)
        self._runway_length = runway_length

    @property
    def runway_length(self):
        return self._runway_length

    @runway_length.setter
    def runway_length(self, runway_length):
        if type(runway_length) is int:
            self._runway_length = runway_length
        else:
            raise TypeError('Expected int value')
