# AutoUpdateIP [![Build Status](https://travis-ci.org/raboof/nethogs.svg?branch=master)](https://travis-ci.org/raboof/nethogs)
This Python code will auto update current user IP Address in Smart DNS Proxy website

### Why?
1. Unblock content - access geo-restricted content.
2. Netflix will disconnect user IP address when their detect usage of VPN into their service every 3 minute.
3. User need to Activate/Update their IP Address again in Smart DNS Proxy website to enable access Netflix.

### How to use
1. Create an free trial account at [Smart DNS Proxy](https://www.smartdnsproxy.com/SignUp) 
2. Change current network adapter DNS setting with 2 server near your physical server at [Smart DNS Proxy Servers](https://www.smartdnsproxy.com/Servers) 
3. Clone this [repository](https://github.com/saifulaffendy21/AutoUpdateIP) into your local machine [repository](https://github.com/saifulaffendy21/AutoUpdateIP)
4. Save downloaded [WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads) depending current the version of Chrome you using into path.
5. Navigate to the folder [path](https://github.com/saifulaffendy21/AutoUpdateIP) using Windows PowerShell.
6. Run command [`python .\Auto_Reload_Netflix.py`]

### Required
1. Window 10
2. Python 3.6
3. Selenium 2.0
4. ChromeDriver - WebDriver for Chrome
