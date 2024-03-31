from collections import UserDict

class Field:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError()
        self.value = value
    
    def is_valid(self, value):
        return True

    def __str__(self):
        return str(self.value)

class Name(Field):
	pass

class Phone(Field):
    def is_valid(self, value):
        return len(value) == 10 and value.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        phone = Phone(number)
        self.phones.append(phone)
        return phone

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
            
    def remove_phone(self, number):
        phone = self.find_phone(number)
        if not phone:
            raise ValueError()
        self.phones.remove(phone)

    def edit_phone(self, old_number, new_number):
        phone = self.find_phone(old_number)
        if not phone:
            raise ValueError()
        self.add_phone(new_number)
        self.remove_phone(old_number)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        return record

    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        self.data.pop(name)

    def __str__(self) -> str:
        return "\n".join(str(record) for record in self.data.values)

""" book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

john.remove_phone("5555555555")

for name, record in book.data.items():
    print(record) """