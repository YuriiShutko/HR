import json
from hr.helpers import get_user_names
import spwd
import grp

def read(path):
    with open(path, 'r') as f:
        return json.load(f)

def dump(path, user_names=get_user_names()):
    users = []
    for user_name in user_names:
        password = spwd.getspnam(user_name).sp_pwd
        groups = _groups_for_user(user_name)
        users.append({
            'name': user_name,
            'groups': groups,
            'password': password
        })
    with open(path, 'w') as f:
        json.dump(users, f)

def _groups_for_user(user_name):
    return [g.gr_name for g in grp.getgrall() if user_name in g.gr_mem]
