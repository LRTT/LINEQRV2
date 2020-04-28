# NEW LINE QR LOGIN [![Status](https://img.shields.io/uptimerobot/status/m784649310-76a691bfaa786fd2ebc99ed7?style=for-the-badge)]()
Generate Line's Cert/AuthToken by QRCode 

Example
------------
```python
from newqr import NewQRLogin

newqr = NewQRLogin()

print("Headers: %s" % (", ".join(newqr.HEADERS)))
header = input("Header: ")

token, cert = newqr.loginWithQrCode(header)

print("Access Token: " + token)
print("Certificate: " + cert)
```
