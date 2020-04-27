import requests

class NewQRLogin:
    HEADERS = ["android_lite", "android", "ios_ipad", "ios", "chrome", "desktopwin", "desktopmac"]
    BASE_HOST = "https://api.lrtt.icu/secondaryQrCodeLogin.do/"

    def __init__(this, callback=lambda x: print(x)):
        this.callback = callback

    def get(this, URL):
        return requests.get(URL).json()

    def getHeaders(this, URL):
        return requests.get(URL).json()

    def parseLogin(this, loginInfo):
        return (loginInfo["token"], loginInfo["certificate"])

    def loginQR(this, header):
        assert header in this.HEADERS
        result = this.get(this.BASE_HOST + "login?headers=" + header)
        if result["status"] != 200:
            raise Exception(result["reason"])
        this.callback("Login Url: %s" % (result["url"]))
        result = this.get(this.BASE_HOST + result["callback"])
        if result["status"] != 200:
            raise Exception(result["reason"])
        this.callback("Pin Code: %s" % (result["pincode"]))
        result = this.get(this.BASE_HOST + result["callback"])
        if result["status"] != 200:
            raise Exception(result["reason"])
        return result

    def loginQR(this, header):
        assert header in this.HEADERS
        result = this.get(this.BASE_HOST + "login?headers=" + header)
        if result["status"] != 200:
            raise Exception(result["reason"])
        this.callback("Login Url: %s" % (result["url"]))
        result = this.get(this.BASE_HOST + result["callback"])
        if result["status"] != 200:
            raise Exception(result["reason"])
        this.callback("Pin Code: %s" % (result["pincode"]))
        result = this.get(this.BASE_HOST + result["callback"])
        if result["status"] != 200:
            raise Exception(result["reason"])
        return result

    def loginQRWithWebPinCode(this, header, lang="en"):
        # SUPPORT LANGUAGE: [en, th, jp]
        assert header in this.HEADERS
        result = this.get(this.BASE_HOST + "login?headers=" + header)
        if result["status"] != 200:
            raise Exception(result["reason"])
        this.callback(
            "Pin Url: %sawaitPinCode?session=%s&lang=%s" % (this.BASE_HOST, result["session"], lang) + "\n"
            "Login Url: %s" % (result["url"])
        )
        result = this.get(this.BASE_HOST + result["callback"])
        if result["status"] != 200:
            raise Exception(result["reason"])
        result = this.get(this.BASE_HOST + result["callback"])
        if result["status"] != 200:
            raise Exception(result["reason"])
        return result

    def loginQRWithCert(this, header, certificate):
        assert header in this.HEADERS
        result = this.get(this.BASE_HOST + "login?headers=" + header + "&certificate=" + certificate)
        if result["status"] != 200:
            raise Exception(result["reason"])
        this.callback("Login Url: %s" % (result["url"]))
        result = this.get(this.BASE_HOST + result["callback"])
        if result["status"] != 200:
            raise Exception(result["reason"])
        return result

    def loginQRWithCertV2(this, header, certificate=""):
        assert header in this.HEADERS
        result = this.get(this.BASE_HOST + "login?headers=" + header + "&certificate=" + certificate + "&type=2")
        if result["status"] != 200:
            raise Exception(result["reason"])
        this.callback("Login Url: %s" % (result["url"]))
        result = this.get(this.BASE_HOST + result["callback"])
        if result["status"] == 500:
            raise Exception(result["reason"])
        if result["status"] != 409:
            return result
        this.callback("Pin Code: %s" % (result["pincode"]))
        result = this.get(this.BASE_HOST + result["callback"])
        if result["status"] != 200:
            raise Exception(result["reason"])
        return result
