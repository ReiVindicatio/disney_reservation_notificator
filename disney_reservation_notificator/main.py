import yaml
from disney_reservation_notificator.discord.discord_client import send_message
from disney_reservation_notificator.service.get_handler_cls import get_handler_cls

def main():
    with open('config.yaml', 'r') as f:
        reservation_config = yaml.safe_load(f)
    for reserve_type, config in reservation_config["config"]["reservation"].items():
        handler_cls = get_handler_cls(reserve_type=reserve_type)
        res = handler_cls(**config).retrieve_reservation_info()
        if res['hotels']:
            message = f"Room Vacancy Found.\n url：[予約サイト]({res['url']})\n"
            for hotel in res['hotels']:
                message += '- ' + hotel['name'] + '\n'
                for room in hotel['rooms']:
                    message += '  - ' + room + '\n'
        send_message(message=message)

if __name__ == '__main__':
    main()