from address import Address
from mailing import Mailing


to_address = Address("465757", "Пермь", "Садовая", "10", "5")

from_address = Address("8745", "Орск", "Высокая", "23", "45")

mailing = Mailing(to_address, from_address, 300, "trk67854")

print(mailing)
