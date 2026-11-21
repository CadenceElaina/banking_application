from account import Account, accounts, create_account, login


def print_choices_unauth() -> Account | None:
    print("Please select from:\n\tCreate Account (C)\n\tLogin (L)\n\tQuit (Q)")
    choice = input().lower()

    match choice:
        case "c":
            new_account = create_account()
            accounts.append(new_account)
            return new_account
        case "l":
            account = login()
            return account if account else print_choices_unauth()
        case "q":
            return None  # end program entirely
        case _:
            print("Invalid choice, try again.")
            return print_choices_unauth()  # keep program running


def print_choices_auth(user: Account) -> int:
    print(f"\nWelcome back {user.name}!")
    print(
        "Please select from:\n\tBalance (B)\n\tDeposit (D)\n\tWithdraw (W)\n\tLogout (L)\n\tQuit (Q)"
    )
    choice = input().lower()

    match choice:
        case "b":
            user.get_balance()
            return 0
        case "d":
            user.deposit()
            return 0
        case "w":
            user.withdraw()
            return 0
        case "l":
            return 3  # Signal to go to main menu authenticated
        case "q":
            return 2  # end program entirely
        case _:
            print("Invalid choice, try again.")
            return print_choices_auth(user)  # Continue authenticated


def main() -> None:
    # text_program = 0

    while True:
        print(
            f"\nWelcome. Each choice is operation and key (case insensitive) to execute that operation."
        )
        user = (
            print_choices_unauth()
        )  # User selects a choice returning 0 or 1. 0 recalls this while loop prints message and calls unauth or auth text program. 1 exits this loop.

        if user is None:  # User selected quit
            return

        while True:
            choice = print_choices_auth(user)
            if choice == 2:
                return  # exit program
            if choice == 3:
                break  # logout -> welcome menu


if __name__ == "__main__":
    main()
