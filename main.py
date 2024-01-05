from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        super().__init__(value)

    def __str__(self):
        return self.value


class Phone(Field):
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not self.validate(value):
            raise ValueError("Invalid phone format")
        self._value = value

    @staticmethod
    def validate(phone_number):
        return phone_number.isdigit() and len(phone_number) == 10
    
    def __str__(self):
        return self.value
   

class Birthday(Field):
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not self.validate(value):
            raise ValueError("Invalid date format")
        self._value = value

    @staticmethod
    def validate(birthday):
        try:
            datetime.strptime(birthday, "%Y-%m-%d")
            return True
        except ValueError:
            return False
        
    def __str__(self):
        return self.value


class Record:
    def __init__(self, name, phones=None, birthday=None):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in phones] if phones else []
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        self.phones = [
            phone for phone in self.phones if phone.value != phone_number]
    
    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                return
        raise ValueError(f"Phone number {old_number} not found")

    def find_phone(self, phone_number):
        return next((phone for phone in self.phones if phone.value == phone_number), None)
    
    def days_to_birthday(self):
        if not self.birthday:
            return "Birthday not set"
        bday = datetime.strptime(self.birthday.value, "%Y-%m-%d")
        now = datetime.now()
        next_bday = bday.replace(year=now.year)
        if now > next_bday:
            next_bday = next_bday.replace(year=now.year + 1)
        return (next_bday - now).days

    def __str__(self):
        phones = ', '.join([str(phone) for phone in self.phones])
        birthday = f"{str(self.birthday)}" if self.birthday else ""
        if birthday:
            return f"Contact name: {self.name.value}; Phones: {phones}; Birthday: {birthday}"
        else:
            return f"Contact name: {self.name.value}; Phones: {phones}"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):        
        name = record.name.value
        self.data[name] = record

    def find(self, name):
        return self.data.get(name, None)
       
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Contact '{name}' has been deleted."
        else:
            return f"Contact '{name}' not found."

    def iterator(self, n):
        records = list(self.data.values())
        for i in range(0, len(records), n):
            yield records[i:i + n]
 
