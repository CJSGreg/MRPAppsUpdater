import requests
from github import Github

class GitHub:

    def __init__(self):
        self.accessToken = open("keys.txt", "r").readlines()[0]
        self.base_url = "https://raw.githubusercontent.com/CJSGreg/"
        self.headers = {"Authorization": f"Bearer {self.accessToken}"}
        self.verFileName = "ver.txt"

    def get_from_repo(self, name_of_repo, path_to_file):


    def check_ver_match(self, curr_ver, name_of_repo):

