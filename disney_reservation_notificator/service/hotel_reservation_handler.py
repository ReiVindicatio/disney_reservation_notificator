from pydantic import BaseModel
from selenium import webdriver
from bs4 import BeautifulSoup
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

class Metadata(BaseModel):
    use_date: str
    adult_num: int

class HotelReservationHandler(ReservationHandler):
    metadata: Metadata
    hotels: list[Hotel]
    base_url: str = ""

    def model_post_init(self, __context) -> None:
        self.base_url = f"https://reserve.tokyodisneyresort.jp/hotel/list/?useDate={self.metadata.use_date}&stayingDays=1&roomsNum=1&adultNum={self.metadata.adult_num}&childNum=0&childAgeBedInform=&displayType=data-hotel"
        return super().model_post_init(__context)

    def retrieve_reservation_info(self) -> dict:
        # html: str = self._retrieve_html()
        with open('resources/test.html', 'r') as f:
            html = f.read()
        hotel_info = self._parse_hotel_info(html)
        res = {'url': self.base_url, 'rooms': []}
        for hotel in self.hotels:
            if not hotel.is_monitored:
                continue
            for room in hotel.rooms:
                if not room.is_monitored:
                    continue
                if hotel_info[hotel.hotel_id][room.room_id]:
                    res['rooms'].append(hotel.logical_name + " " + room.logical_name)
        return res
    
    def _retrieve_html(self) -> str:
        driver = webdriver.Chrome()
        driver.get(self.base_url)
        return driver.page_source
    
    def _parse_hotel_info(self, html: str) -> dict:
        soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
        hotel_content_div = soup.find('div', id='content').find('div', {'data-role': 'content'}, class_='hotelContent')
        hotel_vacant_info = {}
        for hotel in hotel_content_div.find_all('div', {'data-hotel': True}, class_='sectionHotel01'):
            if not hotel:
                continue
            hotel_id: str = hotel['data-hotel']
            hotel_vacant_info[hotel_id] = {}
            rooms_div = hotel.find('div', class_='boxHotel01')
            for room_div in rooms_div.find_all('div', recursive=False):
                room_id: str = room_div['data-hotel']
                is_vacant: bool = (room_div.get('style', '') != 'display: none;')
                hotel_vacant_info[hotel_id][room_id] = is_vacant
        return hotel_vacant_info