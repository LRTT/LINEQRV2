from newqr import NewQRLogin
from linepy import LINE

def sendToChat(client, to, header):
    newqr = NewQRLogin(lambda output: client.sendMessage(to, output))
    method = newqr.loginQRWithWebPinCode
    token, cert = newqr.parseLogin(method(header))
    client.sendMessage(to, "TOKEN: %s\nCERT: %s" % (token, cert))
