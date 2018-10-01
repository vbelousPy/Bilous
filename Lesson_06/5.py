import urllib3


class Browser:

    def get(self, url):
        http = urllib3.PoolManager()
        response = http.request("GET", url)
        return response.data.decode("UTF-8")


url = "http://google.com"
my_browser = Browser()
print(my_browser.get(url))
