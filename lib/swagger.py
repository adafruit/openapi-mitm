class Swagger:

  def __init__(self):
    self.hosts = {}

  def get_host(self, req):

    if req.host not in self.hosts:
      self.hosts[req.host] = {
        'host': req.host,
        'paths': {},
        'schemes': []
      }

    return self.hosts[req.host]

  def get_path(self, req):
     host = self.get_host(req)

     if '?' in req.path:
       path = req.path[:req.path.find('?')]
     else:
       path = req.path

     if path not in host['paths']:
       host['paths'][path] = {}

     return host['paths'][path]

  def get_method(self, req):
     method = req.method.lower()
     path = self.get_path(req)

     if method not in path:
       path[method] = {
         'consumes': [],
         'parameters': [],
         'responses': {}
       }

     return path[method]

  def parse_request(self, req):
    self.get_method(req)

  def print_debug(self):
    for host in self.hosts:
      print(self.hosts[host]['host'])

      for path in self.hosts[host]['paths']:
        print('  - {0}'.format(path))

    print('--------------------------------')

  def request(self, flow):
    self.parse_request(flow.request)
    self.print_debug()


def start():
    return Swagger()
