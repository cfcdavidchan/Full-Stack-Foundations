#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from http.server import BaseHTTPRequestHandler, HTTPServer
class webServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				message = b""
				#message += b"<html><body>Hello!\nHow are you On9 Ben</html>"
				message += b"<div>Hello!</div><div>How are you On9 Ben</div>"
				self.wfile.write(message)
				print (message)
				return
		except IOError:
			self.send_error(404, 'File Not Found: %s' % self.path)

def main():
	try:
		port = 1099 
		server = HTTPServer(('', port), webServerHandler)
		print ("Web Server running on port %s"  % port)
		server.serve_forever()
	except KeyboardInterrupt:
		print (" ^C entered, stopping web server....")
		server.socket.close()
		server.shutdown()

if __name__ == '__main__':
	main()
