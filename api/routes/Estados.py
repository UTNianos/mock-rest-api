import json
from tornado.web import RequestHandler

class EstadosHandler(RequestHandler):

    # GET /estados
    def get(self):

        estados = [
        {
           "id": 5,
           "status": 2
        }, 
        {
           "id": 2,
           "status": 3
        },
        {
          "id": 6,
           "status": 3
        }]
  
        response = {'estados': estados }        

        self.set_header("Content-Type", "application/jsonp;charset=UTF-8")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_status(200, "Ok")
        self.write(response)
        return
