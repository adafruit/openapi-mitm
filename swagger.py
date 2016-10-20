class Swagger:

  def __init__(self):
    self.hosts = {}

  def add_host(self, req):
    if req.host not in self.hosts:
      self.hosts[req.host] = {
        'host': req.host,
        'paths': {},
        'schemes': []
      }

  def add_path(self, req):
     if req.path not in self.hosts[req.host]['paths']:
       self.hosts[req.host]['paths'][req.path] = {}

  def add_method(self, req):
     method = req.method.lower()
     if method not in self.hosts[req.host]['paths'][req.path]:
       self.hosts[req.host]['paths'][req.path][method] = {
         'consumes': [],
         'parameters': [],
         'responses': {}
       }

  def parse_request(self, req):
    self.add_host(req)
    self.add_path(req)
    self.add_method(req)

  def request(self, flow):
    self.parse_request(flow.request)
    print(self.hosts)

def start():
    return Swagger()
