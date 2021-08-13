from requests import Request, Session
s = Session()
url = 'https://www.cnblog.com'
data = {"s":"Golang"}
header = {'Accept-Encoding': 'identity, deflate, compress, gzip',
'Accept': '*/*', 'User-Agent': 'python-requests/0.13.1'}
req = Request('GET', url,
    data=data,
    headers=header
)
prepare_obj = req.prepare()

resp = s.send(prepare_obj,
    stream=stream,
    verify=verify,
    cert=cert,
    timeout=timeout
)

print(resp.status_code)