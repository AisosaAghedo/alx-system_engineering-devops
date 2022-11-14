#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress."""

if __name__ == "__main__":
    import requests
    from sys import argv

    i = 0
    name = ""
    total = 0
    complete = 0

    req = requests.get("https://jsonplaceholder.typicode.com/users",
                       params={"id": argv[1]})
    name = req.json()[0].get("name")
    req = requests.get("https://jsonplaceholder.typicode.com/todos",
                       params={"userId": argv[1]})
    total = len(req.json())
    req = requests.get("https://jsonplaceholder.typicode.com/todos",
                       params={"userId": argv[1], "completed": "true"})
    complete = len(req.json())
    print("Employee {} is done with tasks({:d}/{:d}):".format(
            name, complete, total))
    while i < len(req.json()):
        print("\t {}".format(req.json()[i].get("title")))
        i += 1
