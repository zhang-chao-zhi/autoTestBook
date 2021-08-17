import browsercookie
chrome_cookie = browsercookie.chrome()
for cookie in chrome_cookie:
    if '__zp_stoken_' in str(cookie):
        tmp_cookie = str(cookie)
        tmp_cookie = tmp_cookie.replace("<Cookie ", "")
        tmp_cookie = tmp_cookie.replace(" for .zhipin.com/>", "")

        print(tmp_cookie)

# <Cookie