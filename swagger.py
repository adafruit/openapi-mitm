def request(flow):
  for header in flow.request.headers:
    print(header)
