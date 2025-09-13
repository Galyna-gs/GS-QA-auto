import requests

class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        
        body = r.json()
        return body

    def search_repo(self, name):
        r = requests.get("https://api.github.com/search/repositories", params = {"q": name})

        body = r.json()
        return body 
    
    def get_emoji(self):
        response = requests.get('https://api.github.com/emojis')
        body = response.json()
        return body
    
    def get_last_commit(self, owner, reponame, branch):
        response = requests.get(f'https://api.github.com/repos/{owner}/{reponame}/commits', params = {"sha": branch, "per_page": 1})
        body = response.json()
        return body
    