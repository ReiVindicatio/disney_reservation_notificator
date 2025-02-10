from pydantic import BaseModel
from abc import ABC, abstractmethod

class ReservationHandler(BaseModel, ABC):

    @abstractmethod
    def retrieve_reservation_info(self):
        pass