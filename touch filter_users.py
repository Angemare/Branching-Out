import json


def filter_users_by_input(name):
    with open("users.json", "r") as file:
        users = json.load(file)

#def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

#def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()], [user for user in users if user["age"].lower() == age.lower()],[user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name', 'age' and 'email' is supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_input(name_to_search)
        print(name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        filter_users_by_input(age_to_search)
        print(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an Email to filter users: ")
        filter_users_by_input(email_to_search)
        print(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
