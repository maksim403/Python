from smartphone import Smartphone


catalog = [
    Smartphone("Poco", "X6", "+79875674567"),

    Smartphone("Apple", "14", "+79088765643"),

    Smartphone("Xiaomi", "Radmi5", "+79078765645"),

    Smartphone("Samsung", "Galaxi10", "+79067895692"),

    Smartphone("Honor", "T15", "+79046789065")
]

for smartphone in catalog:

    print(
        f"{smartphone.phone_brand} -"
        f"{smartphone.phone_model}."
        f"{smartphone.subscriber_number}")
