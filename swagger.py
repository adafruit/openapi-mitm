class Swagger:

  def __init__(self):
    self.hosts = {}

  def add_host(self, req):
    if req.host not in self.hosts:
      self.hosts[req.host] = {}

  def add_path(self, req):
     if req.path not in self.hosts[req.host]:
       self.hosts[req.host][req.path] = {}

  def add_method(self, req):
     method = req.method.lower()
     if method not in self.hosts[req.host][req.path]:
       self.hosts[req.host][req.path][method] = {}

  def parse_request(self, req):
    self.add_host(req)
    self.add_path(req)
    self.add_method(req)

  def request(self, flow):
    self.parse_request(flow.request)
    print(self.hosts)

def start():
    return Swagger()
