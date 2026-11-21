import time
import uuid
import sys


class Account:
    def __init__(
        self,
        timestamp: int,
        account_id: str,
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
        self.name = name
        self.email = email
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.residency_status = residency_status
        self.address = address
        self.occupation = occupation

    def login(self) -> None:
        print("\nLogged in!")

    def deposit(self) -> None:
        print("\nHow much would you like to deposit?")
        amount = input().lower()

        print(f"\nDeposited {amount}")

    def withdraw(self) -> None:
        print("\nHow much would you like to withdraw?")
        amount = input().lower()
        print(f"Withdrew {amount}")

    def pay(self, timestamp: int, account_id: str, ammount: int) -> int | None:
        return 1


def create_account() -> None:
    print("\nFill out our application form:\n\t")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone number: ")
    date_of_birth = input("Date of birth (YYYY-MM-DD): ")
    residency_status = input(
        "Citizenship (U.S. Citizen / Permanent Resident Alien / Non-resident Alien): "
    )
    address = input("Address: ")
    occupation = input("Occupation (or type Unemployed): ")

    # TODO  create autoincrementer on ids - store user accoutns in an array?
    new_account = Account(
        0,
        1,
        name,
        email,
        phone,
        date_of_birth,
        residency_status,
        address,
        occupation,
    )

    print("\nAccount created!")


def print_choices_unauth() -> None | int:
    print("Please select from:\n\tCreate Account (C)\n\tLogin (L)\n\tQuit (Q)")
    choice = input().lower()

    match choice:
        case "c":
            create_account()
            return 1  # Create account - move to authenticated screen
        case "l":
            # login()
            return 1  # Move to the authenticated menu.
        case "q":
            return 2  # end program entirely
        case _:
            print("Invalid choice, try again.")
            return print_choices_unauth()  # keep program running


def print_choices_auth() -> None | int:
    print(
        "Please select from:\n\tDeposit (D)\n\tWithdraw (W)\n\tLogout (L)\n\tQuit (Q)"
    )
    choice = input().lower()

    match choice:
        case "d":
            deposit()
            return 0
        case "w":
            withdraw()
            return 0
        case "l":
            return 3  # Signal to go to main menu authenticated
        case "q":
            return 2  # end program entirely
        case _:
            print("Invalid choice, try again.")
            return print_choices_auth()  # Continue authenticated


def main() -> None:
    # text_program = 0

    while True:
        print(
            f"\nWelcome. Each choice is operation and key (case insensitive) to execute that operation."
        )
        text_program = (
            print_choices_unauth()
        )  # User selects a choice returning 0 or 1. 0 recalls this while loop prints message and calls unauth or auth text program. 1 exits this loop.
        if text_program == 2:
            return

        while True:
            choice = print_choices_auth()

            if choice == 2:
                return  # exit program
            if choice == 3:
                break  # logout -> welcome menu


if __name__ == "__main__":
    main()
