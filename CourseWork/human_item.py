class Human:

    def __init__(self, first_name, last_name, city, date_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.date_birth = date_birth

    def __str__(self) -> str:
        return "{};{};{};{}".format(self.first_name, self.last_name, self.city, self.date_birth)

    def __eq__(self, other):
        return str.lower(other) in str.lower(self.first_name) or str.lower(other) in str.lower(self.last_name)
