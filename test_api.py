import pytest
from api import add_task


def test_api_add():
    name = "task1"
    due = "2020-06-20"
    desc = "Some task"
    response = add_task(name, due, desc)
    expected = {"name": name, "due_date": due, "description": desc}
    assert response == expected, "Did not get expected response"
