class CurrencyConverter:
    def __init__(self, exchange_rate):
        """
        Ініціалізація конвертера з заданим курсом обміну.
        :param exchange_rate: Курс гривні до долара США.
        """
        self.exchange_rate = exchange_rate

    def convert_to_usd(self, amount_uah):
        """
        Конвертує суму в гривнях до доларів США.
        :param amount_uah: Сума в гривнях.
        :return: Еквівалентна сума в доларах США.
        """
        return amount_uah / self.exchange_rate

def main():
    exchange_rate = 41.689

    converter = CurrencyConverter(exchange_rate)

    try:
        amount_uah = float(input("Введіть суму в гривнях: "))
        amount_usd = converter.convert_to_usd(amount_uah)
        print(f"Еквівалент у доларах США: {amount_usd:.2f} USD")
    except ValueError:
        print("Будь ласка, введіть коректне числове значення.")

if __name__ == "__main__":
    main()
