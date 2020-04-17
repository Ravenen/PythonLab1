class Squeezer(object):

    number_of_blades = 2

    def __init__(self, color="White", max_juice_amount_in_litres_per_hour=20, power_in_kw=500, producer="China Inc",
                 volume_in_square_cm=30, weight_in_kg=5, price_in_uah=1200):
        self.color = color
        self.max_juice_amount_in_litres_per_hour = max_juice_amount_in_litres_per_hour
        self.power_in_kw = power_in_kw
        self.producer = producer
        self.volume_in_square_cm = volume_in_square_cm
        self.weight_in_kg = weight_in_kg
        self.price_in_uah = price_in_uah

    def __del__(self):
        pass

    def __str__(self) -> str:
        return f"Color: {self.color}, max juice amount in litres per hour: " \
               f"{self.max_juice_amount_in_litres_per_hour}, power in kilowatts: {self.power_in_kw}, " \
               f"producer: {self.producer}, volume in square centimetres: {self.volume_in_square_cm}, " \
               f"weight in kilograms: {self.weight_in_kg}, price in UAH: {self.price_in_uah}"

    @staticmethod
    def get_number_of_blades():
        return Squeezer.number_of_blades


if __name__ == '__main__':
    first_squeezer = Squeezer("Red", 15, 450, "Bosh", 25, 4, 1500)
    second_squeezer = Squeezer("Black", 25, 45, "LG")
    third_squeezer = Squeezer("Blue", 30, 750)
    print(first_squeezer, second_squeezer, third_squeezer, sep="\n")

