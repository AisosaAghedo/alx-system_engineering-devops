#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress."""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todo_li = requests.get(url + "todos", params={"userId": argv[1]}).json()

    completed = [t.get("title") for t in todo_li if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo_li)))
    [print("\t {}".format(c)) for c in completed]
