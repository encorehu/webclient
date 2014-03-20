from webclient import WebBrowser

def test_webbrowser(url):

    browser = WebBrowser(debug=False)
    html = browser._request(url)
    print type(html)
    print html[:200]

def test_cookie(url,cookies):
    browser = WebBrowser()
    html = browser._request(url,cookies=cookies)
    print type(html)
    print html[:200]

if __name__ == "__main__":
    url ='http://www.google.com' # google is a very good test url, it jumps to google.com.hk for chinese user
    test_webbrowser(url)

    #test_cookie(url, 'Me=12') #this is a wrong cookie for test, visit google.com will jump 2 times
