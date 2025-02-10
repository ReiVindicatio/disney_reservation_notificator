from typing import Type
from disney_reservation_notificator.service.base.reservation_handler import ReservationHandler
from disney_reservation_notificator.service import (
    hotel_reservation_handler
)

cls_dict = {
    "hotel": hotel_reservation_handler.HotelReservationHandler
}

def get_handler_cls(
    reserve_type: str
) -> Type[ReservationHandler]:
    if reserve_type not in cls_dict:
        RuntimeError("reserve type is invalid.")
    return cls_dict[reserve_type]