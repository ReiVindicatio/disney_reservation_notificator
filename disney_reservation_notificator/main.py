import yaml
from disney_reservation_notificator.discord.discord_client import send_message

def main():
    with open('config.yaml', 'r') as f:
        reservation_config = yaml.safe_load(f)
    print(reservation_config)
    send_message("hoge")

if __name__ == '__main__':
    main()