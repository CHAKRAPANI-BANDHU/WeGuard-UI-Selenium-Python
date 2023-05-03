import re

def getCurlEquivalent( response ):
    req = response.request

    command = "curl -v -X {method} -H {headers} -d '{data}' '{uri}'"
    method = req.method
    uri = req.url
    data = ""
    if not (req.body is None or len(req.body) == 0):
        data = str(req.body)
        data = re.sub(r"b'(.*)'", r"\1", data)
        #data = data.replace("b'{", "'{")
    headers = ['"{0}: {1}"'.format(k, v) for k, v in req.headers.items() if str(k).startswith("Authorization") or str(k).startswith("Content-Type")]
    headers = " -H ".join(headers)
    return command.format(method=method, headers=headers, data=data, uri=uri)