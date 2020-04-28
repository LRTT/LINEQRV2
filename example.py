from newqr import NewQRLogin

newqr = NewQRLogin()

print("Headers: %s" % (", ".join(newqr.HEADERS)))
header = input("Header: ")

token, cert = newqr.loginWithQrCode(header)

print("Access Token: " + token)
print("Certificate: " + cert)
