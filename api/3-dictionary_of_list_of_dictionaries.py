#!/usr/bin/python3
""" script to export data in the JSON format """
from requests import get
import json


def information_employee():
    """ Records all tasks that are owned by this employee
       Format must be: { "USER_ID": [ {"username": "USERNAME",
       "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
       {"username": "USERNAME", "task": "TASK_TITLE", "completed":
       TASK_COMPLETED_STATUS}, ... ], "USER_ID":
       [ {"username": "USERNAME", "task": "TASK_TITLE", "completed":
       TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE",
       "completed": TASK_COMPLETED_STATUS}, ... ]}
       File name must be: todo_all_employees.json
    """
    user_id = 0
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
            user_id = usr['id']
            user_name = usr['username']
            dict_id[str(user_id)] = list_task
            for tod in response_json_tod:
                if (tod['userId'] == user_id):
                    task_completed_status = tod['completed']
                    task_title = tod['title']
                    dict_task = {"username": user_name,
                                 "task": task_title,
                                 "completed": task_completed_status}
                    list_task.append(dict_task)
            list_task = []
            dict_task = {}

        with open("todo_all_employees.json", 'w',
                  encoding='UTF8') as fjson:
            json.dump(dict_id, fjson)


if __name__ == "__main__":
    information_employee()
