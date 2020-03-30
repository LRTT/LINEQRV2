# NEW LINE QR LOGIN [![Status](https://img.shields.io/website?label=API&style=for-the-badge&url=https%3A%2F%2Fusqf.cf%2Fstatus%2FsecondaryQrCodeLogin)]()
Generate Line's Cert/AuthToken by QRCode 

Example
------------
```python
from newqr import NewQRLogin
from linepy import LINE

# HEADER must be same as linepy/config.py

newqr = NewQRLogin()

print("Headers: %s" % (", ".join(newqr.HEADERS)))
header = input("Header: ")

method = newqr.loginQRWithWebPinCode
token, cert = newqr.parseLogin(method(header))

client = LINE(token)
```
[LINEPY](https://github.com/crash-override404/linepy-modified) required
