import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("index.html")


class GameHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("2048.html")


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("register.html")


class ShanHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("shan.html")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/index", IndexHandler),
        (r"/2048", GameHandler),
        (r"/login", LoginHandler),
        (r"/register", RegisterHandler),
        (r"/shan", ShanHandler)
    ], template_path="templates", static_path='static')


if __name__ == "__main__":
    app = make_app()
    app.listen(8008)
    print("Server is running at http://localhost:8008")
    tornado.ioloop.IOLoop.current().start()
