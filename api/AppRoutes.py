# Route imports
from api.routes.Estados import EstadosHandler
from api.routes.Materias import MateriasHandler
from api.routes.Correlativas import CorrelativasHandler

def get_app_routes(static_path):

    routes = [
        (r"/api/correlativas", CorrelativasHandler),
        (r"/api/estados", EstadosHandler),
        (r"/api/materias", MateriasHandler)
    ]

    return routes