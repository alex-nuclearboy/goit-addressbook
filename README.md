# Address Book Module

This repository contains the Address Book Module, a Python module with classes designed for creating and managing a digital address book.

### Module Contents

- `Field`: The base class for entry fields, providing common logic for all fields.
- `Name`: Derived from Field, used for storing a contact's name. It's a mandatory field.
- `Phone`: Also derived from Field, handles phone number storage with format validation (10 digits).
- `Record`: Maintains information about a contact, including name and a list of phone numbers. Responsible for adding, deleting, and editing optional fields, while storing the mandatory Name field.
- `AddressBook`: Derived from UserDict, it manages contact records. Includes logic for adding, searching, and deleting entries based on contact names.

### Module Functionality

#### AddressBook Class:

- *Add Entries*: Add new contact records to the address book.
- *Search by Name*: Look up entries using the contact's name.
- *Delete by Name*: Remove entries based on the contact's name.

#### Record Class:

- *Add Phone Numbers*: Attach phone numbers to a contact.
- *Delete Phone Numbers*: Remove specific phone numbers from a contact.
- *Edit Phone Numbers*: Modify existing phone numbers.
- *Find Phone Number*: Retrieve specific phone numbers associated with a contact.

### Installation

    # Clone the repository
    git clone https://github.com/your-username/address-book-module.git

### Usage

The module is designed for import into Python scripts where contact management is needed.

### Testing
Additionally, this repository includes a testing script that verifies the functionality of the provided classes. 
It ensures that each class and method operates as intended and that the module maintains robust and error-free performance.
