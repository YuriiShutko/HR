import pytest
import subprocess
import crypt

from hr import user_mgmt

password = crypt.crypt('password', crypt.mksalt(crypt.METHOD_SHA512))
userinfo = {
    'name': 'kevin',
    'groups': ['wheel', 'dev'],
    'password': password
}

def test_user_creation(mocker):
    """
    Given a user dictionary, `user_mgmt.create_user(...)` should utilize `useradd` to create the user.
    """
    mocker.patch('subprocess.run')
    user_mgmt.create_user(userinfo)
    subprocess.run.assert_called_with(['useradd', '-p', password, '-G', 'wheel,dev', 'kevin'], stdout=subprocess.PIPE)

def test_user_deletion(mocker):
    """
    Given a user dictionary, `user_mgmt.delete_user(...)` should utilize `userdel` to delete the user.
    """
    mocker.patch('subprocess.run')
    user_mgmt.delete_user(userinfo)
    subprocess.run.assert_called_with(['userdel', '-r', 'kevin'], stdout=subprocess.PIPE)

def test_user_update(mocker):
    """
    Given a user dictionary, `user_mgmt.update_user(...)` should utilize `usermod` to update the user.
    """
    mocker.patch('subprocess.run')
    user_mgmt.update_user(userinfo)
    subprocess.run.assert_called_with(['usermod', '-p', password, '-G', 'wheel,dev', 'kevin'], stdout=subprocess.PIPE)

def test_users_sync(mocker):
    """
    Given a user dictionary, `user_mgmt.sync_users(...)` should utilize `usermod` to update the user.
    """
    users = [
        userinfo,
        {
            'name': 'jose',
            'groups': ['wheel'],
            'password': password
        }
    ]
    existing_users = ['kevin', 'kyle']
    mocker.patch('subprocess.run')
    user_mgmt.sync_users(users, existing_users)
    subprocess.run.assert_has_calls([
            mocker.call(['usermod', '-p', password, '-G', 'wheel,dev', 'kevin'], stdout=subprocess.PIPE),
            mocker.call(['useradd', '-p', password, '-G', 'wheel', 'jose'], stdout=subprocess.PIPE),
            mocker.call(['userdel', '-r', 'kyle'], stdout=subprocess.PIPE)
   ])

