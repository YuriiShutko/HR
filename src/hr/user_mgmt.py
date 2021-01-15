import subprocess
import sys
import pwd

from hr.helpers import get_user_names

def create_user(userinfo):
    print(f'Creating user with username: "{userinfo["name"]}" and groups: "{userinfo["groups"]}"')
    try:
        subprocess.run(['useradd', '-p', userinfo['password'], '-G', _get_user_groups_str(userinfo), userinfo['name']], stdout=subprocess.PIPE)
    except:
        print(f'Failed to add user "{userinfo["name"]}"')
        sys.exit(1)

def update_user(userinfo):
    print(f'Updating user with "{userinfo["name"]}"')
    try:
        subprocess.run(['usermod', '-p', userinfo['password'], '-G', _get_user_groups_str(userinfo), userinfo['name']], stdout=subprocess.PIPE)
    except:
        print('Failed to update user info "{userinfo["name"]}"')
        sys.exit(1)

def delete_user(userinfo):
    print(f'Deleting user "{userinfo["name"]}"')
    try:
        subprocess.run(['userdel', '-r', userinfo['name']], stdout=subprocess.PIPE)
    except:
        print(f'Failed to remove user "{userinfo["name"]}"')
        sys.exit(1)

def sync_users(users, existing_usernames=None):
    existing_usernames = existing_usernames or get_user_names()
    usernames = [user['name'] for user in users]
    for user in users:
        if user['name'] not in existing_usernames:
            create_user(user)
        elif user['name'] in existing_usernames:
            update_user(user)
    for user in existing_usernames:
        if user not in usernames:
            delete_user({'name': user})

def _get_user_groups_str(userinfo):
    return ','.join(userinfo['groups']) or ''
