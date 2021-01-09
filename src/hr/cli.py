from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(description='CLI utility to create/export system users using JSON')
    parser.add_argument('--export', action='store_true', help='Trigger to export all the system users to the destination file')
    parser.add_argument('path', help='Path to the file from where or where read/write usernames')
    return parser
