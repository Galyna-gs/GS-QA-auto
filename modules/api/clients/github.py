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
        status_code = response.status_code
        body = response.json()
        return body