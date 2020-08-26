import heapq
from abc import ABC
from enum import Enum


class VehicleType(Enum):
    BIKE, CAR, BUS, TRUCK = 1, 2, 3, 4


class ParkingSpotType(Enum):
    SMALL, MEDIUM, LARGE, XLARGE = 1, 2, 3, 4


class Vehicle(ABC):
    def __init__(self, licenceNum, vehicle_type, ticket=None):
        self.__vehicle_type = vehicle_type
        self.__licenceNum = licenceNum
        self.__ticket = ticket

    def assignTicket(self, ticket):
        self.ticket = ticket

    def getVehicleType(self):
        return self.__vehicle_type


class Bike(Vehicle):
    def __init__(self, licenceNum, ticket=None):
        super().__init__(licenceNum, VehicleType.BIKE, ticket)


class Car(Vehicle):
    def __init__(self, licenceNum, ticket=None):
        super().__init__(licenceNum, VehicleType.CAR, ticket)


class Bus(Vehicle):
    def __init__(self, licenceNum, ticket=None):
        super().__init__(licenceNum, VehicleType.BUS, ticket)


class Truck(Vehicle):
    def __init__(self, licenceNum, ticket=None):
        super().__init__(licenceNum, VehicleType.TRUCK, ticket)


class ParkingSpot(ABC):

    def __init__(self, spot_id, spot_type, distance):
        self.__spot_id = spot_id
        self.__spot_type = spot_type
        self.__is_free = True
        self.__vehicle = None
        self.__distance = distance

    def isFree(self):
        return self.__is_free

    def assign(self, vehicle):
        self.__is_free = False
        self.__vehicle = vehicle

    def remove(self):
        self.__is_free = True
        self.__vehicle = None

    def getNumber(self):
        return self.__spot_id

    def getType(self):
        return self.__spot_type

    def getDistance(self):
        return self.__distance


class SmallSpot(ParkingSpot):
    def __init__(self, spot_id, distance):
        super().__init__(spot_id, ParkingSpotType.SMALL, distance)


class MediumSpot(ParkingSpot):
    def __init__(self, spot_id, distance):
        super().__init__(spot_id, ParkingSpotType.MEDIUM, distance)


class LargeSpot(ParkingSpot):
    def __init__(self, spot_id, distance):
        super().__init__(spot_id, ParkingSpotType.LARGE, distance)


class XLargeSpot(ParkingSpot):
    def __init__(self, spot_id, distance):
        super().__init__(spot_id, ParkingSpotType.XLARGE, distance)


class ParkingLot:
    def __init__(self, name):
        self.__name = name
        self.__small_spots = {}
        self.__large_spots = {}
        self.__medium_spots = {}
        self.__xlarge_spots = {}
        self.heap_small = []
        self.heap_medium = []
        self.heap_large = []
        self.heap_xlarge = []

    def addParkingSpot(self, parking_spot):

        spot_type = parking_spot.getType()
        if spot_type == ParkingSpotType.SMALL:
            self.__small_spots[parking_spot.getNumber()] = parking_spot
            heapq.heappush(self.heap_small, (parking_spot.getDistance(), parking_spot.getNumber()))

        elif spot_type == ParkingSpotType.LARGE:
            self.__medium_spots[parking_spot.getNumber()] = parking_spot
            heapq.heappush(self.heap_medium, (parking_spot.getDistance(), parking_spot.getNumber()))

        elif spot_type == ParkingSpotType.MEDIUM:
            self.__large_spots[parking_spot.getNumber()] = parking_spot
            heapq.heappush(self.heap_large, (parking_spot.getDistance(), parking_spot.getNumber()))

        elif spot_type == ParkingSpotType.XLARGE:
            self.__xlarge_spots[parking_spot.getNumber()] = parking_spot
            heapq.heappush(self.heap_xlarge, (parking_spot.getDistance(), parking_spot.getNumber()))

        print("added", self.__small_spots, self.heap_small)

    def assignParkingSpot(self, vehicle, parking_spot):
        parking_spot.assign(vehicle)
        print("Parking Spot Assigned", vehicle.getVehicleType())

    def free_parkingSpot(self, parking_spot):

        spot_type = parking_spot.getType()
        if spot_type == ParkingSpotType.SMALL:
            heapq.heappush(self.heap_small, (parking_spot.getDistance(), parking_spot.getNumber()))

        elif spot_type == ParkingSpotType.LARGE:
            heapq.heappush(self.heap_medium, (parking_spot.getDistance(), parking_spot.getNumber()))

        elif spot_type == ParkingSpotType.MEDIUM:
            heapq.heappush(self.heap_large, (parking_spot.getDistance(), parking_spot.getNumber()))

        elif spot_type == ParkingSpotType.XLARGE:
            heapq.heappush(self.heap_xlarge, (parking_spot.getDistance(), parking_spot.getNumber()))

        parking_spot.remove()

    def getParkingSpot(self, vehicle):
        spot_type = vehicle.getVehicleType()
        if spot_type == VehicleType.BIKE:
            distance, number = heapq.heappop(self.heap_small)
            return self.__small_spots[number]

        elif spot_type == VehicleType.CAR:
            distance, number = heapq.heappop(self.heap_medium)
            return self.__medium_spots[number]

        elif spot_type == VehicleType.BUS:
            distance, number = heapq.heappop(self.heap_large)
            return self.__large_spots[number]

        elif spot_type == VehicleType.TRUCK:
            distance, number = heapq.heappop(self.heap_xlarge)
            return self.__xlarge_spots[number]


if __name__ == "__main__":
    spot1 = SmallSpot("dh101", 10)
    parkingLot = ParkingLot("Pullman")
    parkingLot.addParkingSpot(spot1)
    bike = Bike("LIC220")
    pLot = parkingLot.getParkingSpot(bike)
    parkingLot.assignParkingSpot(bike, pLot)
    parkingLot.free_parkingSpot(pLot)
    bike2 = Bike("LIC221")
    pLot = parkingLot.getParkingSpot(bike2)
    parkingLot.assignParkingSpot(bike2, pLot)
