#!/usr/bin/python3
""" Module to export data in the CSV format """
from requests import get
from sys import argv
import csv


def information_employee():
    """
        Records all tasks that are owned by this employee
        Format must be: "USER_ID","USERNAME",
                        "TASK_COMPLETED_STATUS","TASK_TITLE"
        File name must be: USER_ID.csv
    """
    user_id = int(argv[1])
    user_name = ""
    task_completed_status = False
    task_title = ""
    list_task_employee = []

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
                break

        for tod in response_json_tod:
            if (tod['userId'] == user_id):
                task_completed_status = tod['completed']
                task_title = tod['title']
                list_task = [user_id, user_name,
                             task_completed_status, task_title]
                list_task_employee.append(list_task)

                with open(str(user_id) + ".csv", 'a',
                          encoding='UTF8', newline='') as csvf:
                    writer = csv.writer(csvf, quoting=csv.QUOTE_ALL)
                    writer.writerow(list_task)


if __name__ == "__main__":
    information_employee()
