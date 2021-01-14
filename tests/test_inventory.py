import pytest
import subprocess
import tempfile

from hr import inventory

def test_inventory_read():
    """
    Given an inventory file in JSON format. In the result function inventory_read should return a list of user dictionaries from the inventory
    """
    test_inventory = tempfile.NamedTemporaryFile(delete=False)
    test_inventory.write(b'''
            [
                {
                    "name": "kevin",
                    "groups": ["wheel", "dev"],
                    "password": "pass1"
                },
                {
                    "name": "lisa",
                    "groups": ["wheel"],
                    "password": "pass2"
                },
                {
                    "name": "jim",
                    "groups": [],
                    "password": "pass3"
                }
            ]
    ''')
    test_inventory.close()
    users_list = inventory.inventory_read(test_inventory.name)
    assert users_list[0] == {
        "name": "kevin",
        "groups": ["wheel", "dev"],
        "password": "pass1"
    }
    assert users_list[1] == {
        "name": "lisa",
        "groups": ["wheel"],
        "password": "pass2"
    }
    assert users_list[2] == {
        "name": "jim",
        "groups": [],
        "password": "pass3"
    }
