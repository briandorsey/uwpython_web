from DocXMLRPCServer import DocXMLRPCServer

# Create server
server = DocXMLRPCServer(("localhost", 8000))

# Register a function
def echo(message):
    "Accepts a message parameter and returns it unchanged."
    return message

server.register_function(echo)

# Run the server's main loop
server.serve_forever()

# DocXMLRPCServer classes automatically create and serve documentation to 
# browsers, visit http://localhost:8000/ to see it.
