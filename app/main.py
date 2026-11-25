import requests

def check_website(url):
    try:
        response = requests.get(url, timeout=10)
        print(f"website:{url}")
        print(f"status code: {response.status_code}")
    except requests.RequestException as error:
        print(f"request failed:{error}")

if __name__=="__main__":
    check_website("https://example.com")