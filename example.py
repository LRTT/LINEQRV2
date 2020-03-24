from newqr import NewQRLogin
from linepy import LINE

# HEADER must be same as config.py

newqr = NewQRLogin()

print("Headers: %s" % (", ".join(newqr.HEADERS)))
header = input("Header: ")

method = newqr.loginQRWithWebPinCode
token, cert = newqr.parseLogin(method(header))

client = LINE(token)