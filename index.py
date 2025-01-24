import json
from http.server import BaseHTTPRequestHandler

with open('q-vercel-python.json','r') as f:
    json_obj=json.loads(f.read())
print(json_obj[0]['marks'])

for names in json_obj:
    if names['name']=='sLrcyw82t6':
        print(names['marks'])

def getMarks(l,name):
    d={"marks":[]}
    for names in l:
        
        if names['name']==name:
            d['marks'].append(names['marks'])
           
    return d




class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
        return