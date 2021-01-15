import pwd
from getpass import getpass
from crypt import crypt, METHOD_SHA512

def get_user_names():
    return [user.pw_name for user in pwd.getpwall() if user.pw_uid >= 1000 and 'home' in user.pw_dir]

def gen_crypt_password():
    password = getpass()
    if password == getpass('Please repeat: '):
        print('\n'+crypt(password, METHOD_SHA512))
    else:
        print('\nFailed repeating.')
