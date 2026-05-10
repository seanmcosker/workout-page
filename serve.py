import http.server, functools

handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory='/Users/seanm/Desktop/workout-page')
httpd = http.server.HTTPServer(('', 3456), handler)
httpd.serve_forever()
