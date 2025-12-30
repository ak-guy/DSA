from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod
from enum import IntEnum
from datetime import datetime


class VehicleType(IntEnum):
    TWOWHEELER = 1
    FOURWHEELER = 2


class Vehicle:
    def __init__(self, vehicle_number: str, vehicle_type: VehicleType) -> None:
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

    def __repr__(self) -> str:
        return f"Vehicle(vehicle_number={self.vehicle_number}, vehicle_type={self.vehicle_type})"


class ParkingSpot:
    def __init__(
        self, spot_number: int, vehicle: Vehicle, is_empty: bool = False
    ) -> None:
        self.spot_number = spot_number
        self.__price = None
        self.is_empty = is_empty
        self.vehicle = vehicle
        # self.__ticket = None

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def __repr__(self):
        return f"ParkingSpot(id={self.id},vehicle={self.vehicle},price={self.price},is_empty={self.is_empty})"

    def parkVehicle(self): ...

    def removeVehicle(self): ...

    # @property
    # def ticket(self):
    #     return self.__ticket

    # @ticket.setter
    # def ticket(self, ticket_obj: Ticket):
    #     self.__ticket = ticket_obj


class TwoWheelerParkingSpot(ParkingSpot):
    def __init__(self, spot_number: int, vehicle: Vehicle, is_empty: bool = False):
        super().__init__(spot_number, vehicle, is_empty)
        self.__price = 10


class FourWheelerParkingSpot(ParkingSpot):
    """FourWheelerParkingSpot"""

    def __init__(self, spot_number: int, vehicle: Vehicle, is_empty: bool = False):
        super().__init__(spot_number, vehicle, is_empty)
        self.__price = 20


class IParkingSpotManager:
    def __init__(self, parking_spot_list: List[ParkingSpot]):
        self.parking_spot_list = parking_spot_list
        self.__parking_strategy = DefaultParkingStrategy()

    @property
    def parking_strategy(self):
        return self.__parking_strategy

    @parking_strategy.setter
    def paking_strategy(self, parking_strategy: IParkingStrategy):
        assert isinstance(parking_strategy, IParkingStrategy)
        self.__parking_strategy = parking_strategy

    def findParkingSpace(self):
        self.parking_strategy.find_space()

    def addParkingSpace(self): ...

    def removeParkingSpace(self): ...

    def parkVehicle(self): ...

    def removeVehicle(self): ...


class TwoWheelerParkingSpotManager(IParkingSpotManager):
    def __init__(self, parking_spot_list: List[ParkingSpot]):
        assert isinstance(parking_spot_list, list(TwoWheelerParkingSpot))
        super().__init__(parking_spot_list)


class FourWheelerParkingSpotManager(IParkingSpotManager):
    def __init__(self, parking_spot_list: List[ParkingSpot]):
        assert isinstance(parking_spot_list, list(FourWheelerParkingSpot))
        super().__init__(parking_spot_list)


class IParkingStrategy(ABC):
    @abstractmethod
    def find_space(self): ...


class NearToEntrance(IParkingStrategy):
    def find_space(self): ...


class NearToExit(IParkingStrategy):
    def find_space(self): ...


class DefaultParkingStrategy(IParkingStrategy):
    def find_space(self): ...


class Ticket:
    def __init__(self, vehicle: Vehicle, parking_spot: ParkingSpot):
        self.entry_time: datetime = datetime.now()
        self.vehicle = vehicle
        self.parking_spot = parking_spot

    def __repr__(self) -> str:
        return f"Ticket(vehicle={self.vehicle}, parking_spot={self.parking_spot}, entry_time={self.entry_time})"


class IParkingSpotManagerFactory(ABC):
    def __init__(self, vehicle_type: VehicleType):
        self.__vehicle_type = vehicle_type

    @property
    def vehicle_type(self):
        return self.__vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type: VehicleType):
        self.__vehicle_type = vehicle_type

    @abstractmethod
    def getParkingSpotManager(self): ...


class ParkingSpotManagerFactoryA(IParkingSpotManagerFactory):
    """Creating object of class IParkingSpotManager based on vehicle type"""

    def getParkingSpotManager(self):
        if self.__vehicle_type == 1:
            return TwoWheelerParkingSpotManager
        elif self.__vehicle_type == 2:
            return FourWheelerParkingSpotManager


class EntranceGate:
    def __init__(
        self, vehicle: Vehicle, parking_spot_manager_factory: IParkingSpotManagerFactory
    ):
        self.vehicle = vehicle
        self.parking_spot_manager_obj = parking_spot_manager_factory(
            self.vehicle.vehicle_type
        )

    def getParkingSpace(self):
        self.parking_spot_manager_obj.findParkingSpace()

    def bookParkingSpace(self) -> ParkingSpot:
        self.parking_spot_manager_obj.parkVehicle()

    def generateTicket(self) -> Ticket: ...
