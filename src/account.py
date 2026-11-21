import time
import uuid
import sys

# accounts: Account[] = []


class Account:
    def __init__(
        self,
        timestamp: int,
        account_id: str,
        balance: int,
        username: str,
        password: str,
        name: str,
        email: str,
        phone: str,
        date_of_birth: str,
        residency_status: str,
        address: str,
        occupation: str,
    ) -> None:
        self.__timestamp = timestamp
        self.account_id = account_id
        self.balance = balance
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.residency_status = residency_status
        self.address = address
        self.occupation = occupation

    def get_balance(self) -> None:
        print(f"\nBalance: ${self.balance}")

    def deposit(self) -> None:
        print("\nHow much would you like to deposit?")
        amount = int(input())
        if amount <= 0:
            print("You must deposit a positive amount")
            return
        self.balance += amount
        print(f"\nDeposited ${amount}. New balance: ${self.balance}")

    def withdraw(self) -> None:
        print("\nHow much would you like to withdraw?")
        amount = int(input())
        if amount <= 0:
            print("You must withdraw a positive amount.")
            return
        if (self.balance - amount) < 0:
            print("You cannot withdraw more than your current balance.")
            return
        self.balance -= amount
        print(f"\nWithdrew ${amount}. New balance: ${self.balance}")

    def pay(self, timestamp: int, account_id: str, ammount: int) -> int | None:
        return 1


accounts: list[Account] = [
    Account(
        timestamp=int(time.time()) - 864000,
        account_id=str(uuid.uuid4())[:8],
        balance=5400,
        username="alice_w",
        password="password123",
        name="Alice Walker",
        email="alice.walker@example.com",
        phone="555-0101",
        date_of_birth="1992-04-15",
        residency_status="U.S. Citizen",
        address="101 Maple St, Charlotte, NC",
        occupation="Software Engineer",
    ),
    Account(
        timestamp=int(time.time()) - 750000,
        account_id=str(uuid.uuid4())[:8],
        balance=1250,
        username="bob_m",
        password="password123",
        name="Bob Miller",
        email="bob.miller@example.com",
        phone="555-0102",
        date_of_birth="1988-09-22",
        residency_status="U.S. Citizen",
        address="202 Oak Ave, Austin, TX",
        occupation="Graphic Designer",
    ),
    Account(
        timestamp=int(time.time()) - 620000,
        account_id=str(uuid.uuid4())[:8],
        balance=9800,
        username="charlie_c",
        password="password123",
        name="Charlie Chen",
        email="charlie.chen@example.com",
        phone="555-0103",
        date_of_birth="1995-11-03",
        residency_status="Permanent Resident Alien",
        address="303 Pine Rd, Seattle, WA",
        occupation="Data Analyst",
    ),
    Account(
        timestamp=int(time.time()) - 510000,
        account_id=str(uuid.uuid4())[:8],
        balance=320,
        username="diana_p",
        password="password123",
        name="Diana Prince",
        email="diana.prince@example.com",
        phone="555-0104",
        date_of_birth="1990-06-18",
        residency_status="U.S. Citizen",
        address="404 Cedar Ln, Denver, CO",
        occupation="Museum Curator",
    ),
    Account(
        timestamp=int(time.time()) - 430000,
        account_id=str(uuid.uuid4())[:8],
        balance=15000,
        username="evan_t",
        password="password123",
        name="Evan Torres",
        email="evan.torres@example.com",
        phone="555-0105",
        date_of_birth="1985-01-30",
        residency_status="U.S. Citizen",
        address="505 Birch Blvd, Chicago, IL",
        occupation="Architect",
    ),
    Account(
        timestamp=int(time.time()) - 340000,
        account_id=str(uuid.uuid4())[:8],
        balance=0,
        username="fiona_g",
        password="password123",
        name="Fiona Gallagher",
        email="fiona.g@example.com",
        phone="555-0106",
        date_of_birth="1999-08-12",
        residency_status="U.S. Citizen",
        address="606 Elm St, Boston, MA",
        occupation="Unemployed",
    ),
    Account(
        timestamp=int(time.time()) - 250000,
        account_id=str(uuid.uuid4())[:8],
        balance=4150,
        username="george_k",
        password="password123",
        name="George Kim",
        email="george.kim@example.com",
        phone="555-0107",
        date_of_birth="1994-03-27",
        residency_status="Non-resident Alien",
        address="707 Spruce Way, Atlanta, GA",
        occupation="Graduate Researcher",
    ),
    Account(
        timestamp=int(time.time()) - 180000,
        account_id=str(uuid.uuid4())[:8],
        balance=760,
        username="hannah_b",
        password="password123",
        name="Hannah Brooks",
        email="hannah.brooks@example.com",
        phone="555-0108",
        date_of_birth="1997-12-05",
        residency_status="U.S. Citizen",
        address="808 Willow Ct, Portland, OR",
        occupation="Barista",
    ),
    Account(
        timestamp=int(time.time()) - 90000,
        account_id=str(uuid.uuid4())[:8],
        balance=22300,
        username="ian_s",
        password="password123",
        name="Ian Scott",
        email="ian.scott@example.com",
        phone="555-0109",
        date_of_birth="1982-07-19",
        residency_status="Permanent Resident Alien",
        address="909 Ash Dr, Phoenix, AZ",
        occupation="Pharmacist",
    ),
    Account(
        timestamp=int(time.time()) - 3600,
        account_id=str(uuid.uuid4())[:8],
        balance=890,
        username="julia_r",
        password="password123",
        name="Julia Reyes",
        email="julia.reyes@example.com",
        phone="555-0110",
        date_of_birth="2001-02-14",
        residency_status="U.S. Citizen",
        address="1010 Poplar Pl, Miami, FL",
        occupation="Student",
    ),
]


def login() -> Account | None:
    username = input("\nUsername:")
    password = input("\nPassword:")
    for a in accounts:
        if a.username == username and a.password == password:
            return a

    print("Invalid username or password.")
    return None

    # uname_correct=1
    # password_correct=1
    # account_id = 0
    # for i, a in enumerate(accounts):
    #   for key, value in a.items():
    #      if key == "username" and value == username:
    #          uname_correct=0
    #      if key == "password" and value == password:
    #           password_correct=0
    #            account_id = accounts[i].account_id
    # if uname_correct and password_correct:
    #   return


def create_account() -> Account:
    prompts = {
        "name": "Name",
        "email": "Email",
        "phone": "Phone number",
        "date_of_birth": "DOB",
        "residency_status": "Citizenship (U.S. Citizen / Permanent Resident Alien / Non-resident Alien)",
        "address": "Address",
        "occupation": "Occupation Name or type Unemployed (same :3)",
    }
    print("\nFill out our application form:")
    form_data = {
        field: input(f"\t{label}:") for field, label in prompts.items()
    }  # Dictionary comprehension: prompt.items() loops through each (key, value) pair in prmopts. field gets the key name like "name" or "email" and label gets the prompt text "Name" "Email" etc. For each pair print the label (key name) and take users input to stor the result in a new dictionary under that exact field key.

    print("\nAccount created!")
    login = create_login()
    username, password = login[0], login[1]
    print("\nLogin created!")
    choice = input("\nWould you like to deposit? Enter amount or (C) to continue:\n")
    balance = 0
    if choice.lower() != "c":
        balance += int(choice)

    return Account(
        timestamp=int(
            time.time()
        ),  # time.time() returns current Unix timestamp as a float - casting to int takes off the decimal milliseconds
        account_id=str(uuid.uuid4())[
            :8
        ],  # generate random 128-bit UUID object casted to a string and [:8] is Python string slicing - grabing from index 0 up to index 8
        balance=balance,
        username=username,
        password=password,
        **form_data,  # Dictionary unpacking: ** operator inside a function call unpacks a dictionary into keyword arguments key=value --- name="user_inputed_name", email="example@example.com",etc
    )


def create_login() -> tuple[str, str]:
    print("\nPlease create your username and password:")
    username = ""
    password = ""
    while True:
        username = input("username:")
        if any(a.username == username for a in accounts):
            print("Username already exists, please choose a different one.")
            continue  # restart the while loop to ask again
        # for a in accounts:
        #    for key, value in a.items():
        #        if key == "username" and value == username:
        #            print("Username already exists please choose a different one.")
        #            break
        password = input("password:")
        break
    return username, password
