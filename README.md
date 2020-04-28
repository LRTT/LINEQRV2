# NEW LINE QR LOGIN [![Status](https://img.shields.io/uptimerobot/status/m784649310-76a691bfaa786fd2ebc99ed7?style=for-the-badge)]()
Generate Line's Cert/AuthToken by QRCode 

Example
------------
```python
from newqr import NewQRLogin
from linepy import LINE

# HEADER must be same as linepy/config.py

newqr = NewQRLogin()

# Available headers: ['android_lite', 'android', 'ios_ipad', 'ios', 'chrome', 'desktopwin', 'desktopmac']
header = input("Header: ")

method = newqr.loginWithQrCode
token, cert = newqr.parseLogin(method(header))

client = LINE(token)
```
[LINEPY](https://github.com/crash-override404/linepy-modified) required
