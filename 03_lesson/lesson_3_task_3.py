from address import Address
from mailing import Mailing


to_address = Address("465757", "Пермь", "Садовая", "10", "5")

from_address = Address("8745", "Орск", "Высокая", "23", "45")

mailing = Mailing(to_address, from_address, 300, "trk67854")

print(
    f"Отправление {mailing.track} из {mailing.to_address.index}, "
    f"{mailing.to_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в {mailing.from_address.index}, "
    f"{mailing.from_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
