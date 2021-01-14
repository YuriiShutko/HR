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
    users_list = inventory.read(test_inventory.name)
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

def test_inventory_dump(mocker):
    """
    inventory_dump function should take a destination path and and optional list of users to export then exports the existing user information
    """
    destination_file = tempfile.NamedTemporaryFile(delete=False)
    destination_file.close()

    # spwd.getspnam can't be used by non-root user normally. To test it use Mock
    mocker.patch('spwd.getspnam', return_value=mocker.Mock(sp_pwd='password'))

    # grp.getgrall will return the values from the test machine.
    # To get consistent results we need to mock this.
    mocker.patch('grp.getgrall', return_value=[
        mocker.Mock(gr_name='super', gr_mem=['bob']),
        mocker.Mock(gr_name='other', gr_mem=[]),
        mocker.Mock(gr_name='wheel', gr_mem=['bob', 'kevin']),
    ])

    inventory.dump(destination_file.name, ['kevin', 'bob'])

    with open(destination_file.name) as f:
        assert f.read() == """[{"name": "kevin", "groups": ["wheel"], "password": "password"}, {"name": "bob", "groups": ["super", "wheel"], "password": "password"}]"""
