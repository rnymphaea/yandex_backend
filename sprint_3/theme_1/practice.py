class BacteriaProducer:
    # Допишите инициализатор класса 
    def __init__(self, ...):
        ...

    # Допишите метод
    def create_new(self):
        ...

    # Допишите метод
    def remove_one(self):
        ...


# Пример запуска для самопроверки
bacteria_producer = BacteriaProducer(max_bacteria=3)
bacteria_producer.remove_one()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.remove_one()
