class NewQRLogin:
    API_URL = "https://api.lrtt.icu/secondaryQrCodeLogin.do"
    HEADERS = {
        "android_lite": {
            "User-Agent": "LLA/2.12.0 SKR-H0 9",
            "X-Line-Application": "ANDROIDLITE 2.12.0 Android OS 9;SECONDARY"
        },
        "android": {
            "User-Agent": "Line/10.1.1",
            "X-Line-Application": "ANDROID\t10.1.1\tAndroid OS\t5.1.1"
        },
        "ios_ipad": {
            "User-Agent": "Line/10.1.1",
            "X-Line-Application": "IOSIPAD\t10.1.1\tiPhone 8\t11.2.5"
        },
        "ios": {
            "User-Agent": "Line/10.1.1",
            "X-Line-Application": "IOS\t10.1.1\tiPhone 8\t11.2.5"
        },
        "chrome": {
            "User-Agent": "MozilX-Line-Application/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
            "X-Line-Application": "CHROMEOS\t2.3.2\tChrome OS\t1"
        },
        "desktopwin": {
            "User-Agent": "Line/5.12.3",
            "X-Line-Application": "DESKTOPWIN\t5.21.3\tWindows\t10"
        },
        "desktopmac": {
            "User-Agent": "Line/5.12.3",
            "X-Line-Application": "DESKTOPMAC\t5.21.3\tMAC\t10.15"
        }
    }

    def parseLogin(this, loginInfo):
        return (loginInfo["token"], loginInfo["certificate"])

    def loginWithQrCode(self, header, certificate="", callback=lambda output: print(output)):
        assert header in self.HEADERS, "invaild header"
        resp = requests.post(self.API_URL + "/login?" + urllib.parse.urlencode({"custom_headers": self.HEADERS[header], "certificate": certificate}))
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

    def loginQrCodeWithWebPinCode(self, header, certificate="", callback=lambda output: print(output)):
        assert header in self.HEADERS, "invaild header"
        resp = requests.post(self.API_URL + "/login?" + urllib.parse.urlencode({"custom_headers": self.HEADERS[header], "certificate": certificate}))
        res = resp.json()
        if resp.status_code != 200:
            raise Exception(res)
        callback("Pincode URL: %s" % (res["web"]))
        callback("Login URL: %s" % (res["url"]))

        while "token" not in res:
            resp = requests.post(self.API_URL + res["callback"])
            res = resp.json()
            if resp.status_code != 200:
                raise Exception(res)

        return res

if __name__ == "__main__":
    qrv2 = NewQRLogin()
    qrv2.loginQrCodeWithWebPinCode("android_lite")
