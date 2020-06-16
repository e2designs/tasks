from datetime import datetime

def add_task(name, due_date, description):
    """
    Adds a task

    :param name: Name of task
    :param due_date: Due date of task
    :param description: task description

    :return: locals
    """
    print(locals())
    try:
        date = datetime(due_date)
    except Exception:
        print("Ran into an exception")

    return locals()


