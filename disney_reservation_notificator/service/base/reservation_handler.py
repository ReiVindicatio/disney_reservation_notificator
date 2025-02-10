from pydantic import BaseModel
from abc import ABC, abstractmethod

class Metadata(BaseModel):
    use_date: str
    adult_num: int

class ReservationHandler(BaseModel, ABC):
    metadata: Metadata

    @abstractmethod
    def retrieve_reservation_info(self):
        pass