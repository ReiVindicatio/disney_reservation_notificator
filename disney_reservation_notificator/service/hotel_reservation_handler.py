from pydantic import BaseModel
from disney_reservation_notificator.service.base.reservation_handler import ReservationHandler


class Room(BaseModel):
    room_id: str
    logical_name: str
    is_monitored: bool

class Hotel(BaseModel):
    hotel_id: str
    logical_name: str
    is_monitored: bool
    rooms: list[Room]

class HotelReservationHandler(ReservationHandler):
    hotels: list[Hotel]

    def retrieve_reservation_info(self):
        return super().retrieve_reservation_info()