import requests
import urllib.parse

class NewQRLogin:
    API_URL = "https://api.lrtt.icu/secondaryQrCodeLogin.do"

    def parseLogin(this, loginInfo):
        return (loginInfo["token"], loginInfo["certificate"])

    def loginWithQrCode(self, header, certificate="", callback=lambda output: print(output)):
        resp = requests.post(self.API_URL + "/login?" + urllib.parse.urlencode({"header": header, "certificate": certificate}))
        res = resp.json()
        if resp.status_code != 200:
            raise Exception(res)
        callback("Login URL: %s" % (res["url"]))

        while "token" not in res:
            resp = requests.post(self.API_URL + res["callback"])
            res = resp.json()
            if resp.status_code != 200:
                raise Exception(res)

            if "pin" in res:
                callback("Input PIN: %s" % (res["pin"]))

        return res

if __name__ == "__main__":
    qrv2 = NewQRLogin()
    qrv2.loginWithQrCode("android_lite")
