#!/usr/bin/python3
""" Module in script to export data in the JSON format """
from requests import get
from sys import argv
import json


def information_employee():
    """ Records all tasks that are owned by this employee
       Format must be: { "USER_ID": [{"task": "TASK_TITLE",
       "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
       {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
       "username": "USERNAME"}, ... ]}
       File name must be: USER_ID.json
    """
    user_id = int(argv[1])
    user_name = ""
    task_completed_status = False
    task_title = ""
    dict_id = {}
    list_task = []
    dict_task = {}

    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    response_one = get(url_users)
    response_two = get(url_todos)

    if response_one.status_code == 200:
        response_json_usr = response_one.json()
        response_json_tod = response_two.json()

        for usr in response_json_usr:
            if usr['id'] == user_id:
                user_name = usr['username']

                dict_id[str(user_id)] = list_task

                for tod in response_json_tod:
                    if (tod['userId'] == user_id):
                        task_completed_status = tod['completed']
                        task_title = tod['title']
                        dict_task = {"task": task_title,
                                     "completed": task_completed_status,
                                     "username": user_name}
                        list_task.append(dict_task)

                break

        with open(str(user_id) + ".json", 'w',
                  encoding='UTF8') as fjson:
            json.dump(dict_id, fjson)


if __name__ == "__main__":
    information_employee()
