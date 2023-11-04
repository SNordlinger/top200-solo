from geekmail import sender
from dotenv import load_dotenv

load_dotenv()


def main():
    sender.send_geekmail("return1", "Hello!", "[thing=40692][/thing]")


if __name__ == "__main__":
    main()
