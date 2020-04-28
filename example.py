from newqr import NewQRLogin

# HEADER must be same as config.py

newqr = NewQRLogin()

print("Headers: %s" % (", ".join(newqr.HEADERS)))
header = input("Header: ")

method = newqr.loginWithQrCode
token, cert = newqr.parseLogin(method(header))

print("Access Token: " + token)
print("Certificate: " + cert)
