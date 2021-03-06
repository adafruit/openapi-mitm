import json
import argparse
import os

class Swagger:

  def __init__(self, target):
    self.target = target
    self.hosts = {}

  def get_host(self, req):

    if req.host not in self.hosts:
      self.hosts[req.host] = {
        'swagger': '2.0',
        'info': {
          'title': req.host,
          'description': 'Generated by Adafruit\'s OAI/Swagger MITM Proxy',
          'version': '1.0.0'
        },
        'host': req.host,
        'paths': {},
        'schemes': []
      }

    if req.scheme not in self.hosts[req.host]['schemes']:
      self.hosts[req.host]['schemes'].append(req.scheme)

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
        'responses': {
          'default': {
            'description': 'Default response'
          }
        }
       }

    return path[method]

  def parse_query(self, req):
    method = self.get_method(req)
    for param in req.query:
      if not any(existing['name'] == param for existing in method['parameters']):
        method['parameters'].append({
          'in': 'query',
          'name': param,
          'type': 'string'
        })

  def parse_multipart_form(self, req):
    method = self.get_method(req)

    if req.multipart_form is None:
      return

    if 'multipart/form-data' not in method['consumes']:
      method['consumes'].append('multipart/form-data')

    for param in req.multipart_form:
      if not any(existing['name'] == param for existing in method['parameters']):
        method['parameters'].append({
          'in': 'formData',
          'name': param.decode(),
          'type': 'string'
        })

  def parse_urlencoded_form(self, req):
    method = self.get_method(req)

    if req.urlencoded_form is None:
      return

    if 'application/x-www-form-urlencoded' not in method['consumes']:
      method['consumes'].append('application/x-www-form-urlencoded')

    for param in req.urlencoded_form:
      if not any(existing['name'] == param for existing in method['parameters']):
        method['parameters'].append({
          'in': 'formData',
          'name': param.decode(),
          'type': 'string'
        })


  def parse_request(self, req):

    self.parse_query(req)
    self.parse_multipart_form(req)
    self.parse_urlencoded_form(req)

  def is_static(self, req):

    if '?' in req.path:
      path = req.path[:req.path.find('?')]
    else:
      path = req.path

    return path.endswith(('.js', '.css', '.jpg', '.jpeg', '.png', '.gif'))

  def print_debug(self, req):
    print('[{0}]: {1}'.format(req.method, req.pretty_url))

  def write_json(self):
    if not os.path.isdir('./output'):
      os.mkdir('./output')

    for host in self.hosts:
      target = open('./output/{0}.json'.format(host), 'w')
      target.truncate()
      target.write(json.dumps(self.hosts[host], sort_keys=True, indent=2, separators=(',', ': ')))

  def request(self, flow):

    if flow.request.host != self.target:
      return

    if self.is_static(flow.request):
      return

    self.parse_request(flow.request)
    self.print_debug(flow.request)
    self.write_json()


def start():
    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str)
    args = parser.parse_args()
    return Swagger(args.host)
