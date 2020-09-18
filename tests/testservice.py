 
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True




# A route to return all of the available entries in our catalog.
@app.route('/api/test', methods=['POST'])
def api_all():
    resp = flask.Response("1")
    resp.headers['Cache-Control'] = 'no-cache'
    resp.headers['Pragma'] = 'no-cache'
    #resp.headers['Transfer-Encoding'] = 'chunked'
    resp.headers['Content-Type'] = 'text/plain; charset=utf-8'
    resp.headers['Content-Encoding'] = 'gzip'
    resp.headers['Expires'] = '-1'
    resp.headers['Server'] = 'Microsoft-IIS/10.0'
    resp.headers['Vary'] = 'Accept-Encoding'
    resp.headers['request-id'] = '382e2f61-f36d-443a-9b94-8248f808b16f'
    resp.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
    resp.headers['X-CalculatedBETarget'] = 'VI1PR08MB5342.eurprd08.prod.outlook.com'
    resp.headers['X-BackEndHttpStatus'] = '200'
    resp.headers['X-AspNet-Version'] = '4.0.30319'
    resp.headers['X-CafeServer'] = 'VI1PR02CA0046.EURPRD02.PROD.OUTLOOK.COM'
    resp.headers['X-BEServer'] = 'VI1PR08MB5342'
    resp.headers['X-Proxy-RoutingCorrectness'] = '1'
    resp.headers['X-Proxy-BackendServerStatus'] = '200'
    resp.headers['X-Powered-By'] = 'ASP.NET'
    resp.headers['X-FEServer'] = 'VI1PR02CA0046'
    resp.headers['X-MSEdge-Ref'] = 'Ref A: 14BC70E705EF448EA3A7D44E5F44FF70 Ref B: MAD30EDGE0706 Ref C: 2020-09-17T06:28:58Z'
    #resp.headers['Date'] = 'Thu, 17 Sep 2020 06:28:59 GMT'
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0')