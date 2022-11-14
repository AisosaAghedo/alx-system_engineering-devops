#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todo_list = requests.get(url + "todo_list", params={"userId": argv[1]}).json()

    completed = [t.get("title") for t in todo_list if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo_list)))
    [print("\t {}".format(c)) for c in completed]
