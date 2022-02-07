from datetime import date



class Fish:

    def __init__(self, name_of_fish:str, weight_of_all_fishes: float, price_in_uah_per_kilo: float, body_only: bool, origin_country : str, catch_date):
        self.name = name_of_fish
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = catch_date
        self.origin = origin_country
        self.body_only = body_only
        self.weight = weight_of_all_fishes


class FishShop:
    def __init__(self):
        self.list_of_fish = {}

    def add_fish(self, fish_name: str, total_weight: float, price_of_fish_in_uah: float, body_only: bool, origin_country: str, catch_date):
        self.list_of_fish.update({price_of_fish_in_uah: Fish(name_of_fish=fish_name, weight_of_all_fishes=total_weight, price_in_uah_per_kilo=price_of_fish_in_uah, body_only=body_only, origin_country=origin_country, catch_date=catch_date)})

    def get_fish_names_sorted_by_price(self):
        self.list_of_fish=dict(sorted(self.list_of_fish.items()))
        buffer_list = self.list_of_dict_elements = [value for value in self.list_of_fish.values()]
        sorted_list = []
        for i in buffer_list:
            sorted_list.append(i.name)
        return sorted_list

    def sell_fish(self, fish_name: str, weight: float):
        for i in self.list_of_dict_elements:
            if weight <=i.weight:
                if(i.name==fish_name):
                    total_price = weight*i.price_in_uah_per_kilo
                    self.list_of_fish.update({i.price_in_uah_per_kilo: Fish(i.name, i.weight-weight, i.price_in_uah_per_kilo, i.body_only, i.origin, i.catch_date)})
                    return total_price
            else:
                print("too much fish")
                return 0

    def cast_out_old_fish(self):
        self.list_of_dict_elements = [value for value in self.list_of_fish.values()]
        for i in self.list_of_dict_elements:
            if (date.today() - i.catch_date).days<6:
                del self.list_of_fish[i.price_in_uah_per_kilo]
            else:
                continue
        buffer_list = self.list_of_dict_elements = [value for value in self.list_of_fish.values()]
        sorted_list = []
        for i in buffer_list:
            sorted_list.append(i.name)
        return sorted_list


class Seller:
    def sell_fish(self):
        pass


class Buyer:
    def buy_fish(self):
        pass


shop1 = FishShop()
shop1.add_fish("salmon", 10.5, 23.1, True, "sahaline", date(2022, 2, 7))
shop1.add_fish("pike", 23.4, 42.5, True, "Ukraine",  date(2021, 2, 7))
shop1.add_fish("mackerel", 53.1, 12.0, True, "Iceland", date(2020, 2, 7))
print(shop1.get_fish_names_sorted_by_price())
print(shop1.cast_out_old_fish())
print(shop1.sell_fish("pike", 10))
