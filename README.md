# NEW LINE QR LOGIN [![Status](https://img.shields.io/uptimerobot/status/m784649310-76a691bfaa786fd2ebc99ed7?style=for-the-badge)]()
Generate Line's Cert/AuthToken by QRCode 

Example
------------
```python
from newqr import NewQRLogin

# HEADER must be same as config.py

newqr = NewQRLogin()

print("Headers: %s" % (", ".join(newqr.HEADERS)))
header = input("Header: ")

method = newqr.loginWithQrCode
token, cert = newqr.parseLogin(method(header))

print("Access Token: " + token)
print("Certificate: " + cert)
```
[LINEPY](https://github.com/crash-override404/linepy-modified) required
