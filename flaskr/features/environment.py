# from browser import Browser
# from selenium import webdriver
# driver = webdriver.Chrome()
# import SimpleHTTPServer
# import SocketServer
# import threading
#
# def before_all(context):
#   context.browser = Browser()
#   PORT = 8000
#   Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
#   context.server = SocketServer.TCPServer(("", PORT), Handler)
#   context.thread = threading.Thread(target=context.server.serve_forever)
#   context.thread.start()
#
# def after_all(context):
#   context.browser.close()
#   context.server.server_close()
#   context.thread.join()