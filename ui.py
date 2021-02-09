class UI:
    def input_user_data(self):
        print("Welcome to Josh's Flight Club.")
        print("We find the best flight deals and email you.\n")

        user_data = {}
        user_data["f_name"] = input("What is your first name? ")
        user_data["l_name"] = input("What is your last name? ")

        while True:
            user_data["email"] = input("What is your email? ")
            email_confirmation = input("Please type your email again: ")

            if user_data["email"] == email_confirmation:
                print("\nYou're in the club!")
                break
            else:
                print("\nThe 2 email addressess don't match.")
                print("Try again.")

        return user_data
