import json
from tornado.web import RequestHandler
from tornado.gen import coroutine


class MateriasHandler(RequestHandler):
    
	# GET /materias
    @coroutine
    def get(self):
        materias = [{
            "a": "0",
            "e": "0",
            "x": "1",
            "v": [{
                "t": "M\u00f3dulo A",
                "v": "416"
            }, {
                "t": "M\u00f3dulo B",
                "v": "417"
            }]
        }, {
            "a": "1",
            "e": "0",
            "x": "0",
            "v": [{
                "t": "\u00c1lgebra y Geometr\u00eda Anal\u00edtica",
                "v": "5"
            }, {
                "t": "Algoritmos y Estructuras de Datos",
                "v": "2"
            }, {
                "t": "An\u00e1lisis Matem\u00e1tico I",
                "v": "7"
            }, {
                "t": "Arquitectura de Computadoras",
                "v": "3"
            }, {
                "t": "Ingenier\u00eda y Sociedad",
                "v": "4"
            }, {
                "t": "Matem\u00e1tica Discreta",
                "v": "6"
            }, {
                "t": "Qu\u00edmica General",
                "v": "69"
            }, {
                "t": "Sistemas y Organizaciones",
                "v": "1"
            }]
        }, {
            "a": "2",
            "e": "0",
            "x": "0",
            "v": [{
                "t": "An\u00e1lisis de Sistemas",
                "v": "10"
            }, {
                "t": "An\u00e1lisis Matem\u00e1tico II",
                "v": "14"
            }, {
                "t": "F\u00edsica I",
                "v": "67"
            }, {
                "t": "Ingl\u00e9s I",
                "v": "64"
            }, {
                "t": "Paradigmas de Programaci\u00f3n",
                "v": "8"
            }, {
                "t": "Probabilidad y Estad\u00edstica",
                "v": "12"
            }, {
                "t": "Sintaxis y Sem\u00e1ntica de los Lenguajes",
                "v": "11"
            }, {
                "t": "Sistemas de Representaci\u00f3n",
                "v": "66"
            }]
        }, {
            "a": "3",
            "e": "0",
            "x": "0",
            "v": [{
                "t": "Dise\u00f1o de Sistemas",
                "v": "15"
            }, {
                "t": "Econom\u00eda",
                "v": "71"
            }, {
                "t": "F\u00edsica II",
                "v": "68"
            }, {
                "t": "Gesti\u00f3n de Datos",
                "v": "17"
            }, {
                "t": "Ingl\u00e9s II",
                "v": "65"
            }, {
                "t": "Legislaci\u00f3n",
                "v": "72"
            }, {
                "t": "Matem\u00e1tica Superior",
                "v": "70"
            }, {
                "t": "Sistemas Operativos",
                "v": "9"
            }]
        }, {
            "a": "3",
            "e": "1",
            "x": "0",
            "v": [{
                "t": "Algoritmos Complejos para Estructuras de Datos Avanzadas",
                "v": "422"
            }, {
                "t": "Comunicaciones y Redes",
                "v": "76"
            }, {
                "t": "Creatividad",
                "v": "20"
            }, {
                "t": "Gesti\u00f3n de Recursos Humanos",
                "v": "21"
            }, {
                "t": "Ingenier\u00eda de Requisitos",
                "v": "33"
            }, {
                "t": "Innovaci\u00f3n Tecnol\u00f3gica",
                "v": "22"
            }, {
                "t": "Investigaci\u00f3n Tecnol\u00f3gica",
                "v": "23"
            }, {
                "t": "Metodolog\u00eda de la Conducci\u00f3n de Equipos de Trabajo",
                "v": "75"
            }, {
                "t": "Seguridad Inform\u00e1tica",
                "v": "24"
            }, {
                "t": "T\u00e9cnicas Avanzadas de Programaci\u00f3n",
                "v": "25"
            }, {
                "t": "T\u00e9cnicas de Gr\u00e1ficos por Computadoras",
                "v": "26"
            }]
        }, {
            "a": "4",
            "e": "0",
            "x": "0",
            "v": [{
                "t": "Administraci\u00f3n de Recursos",
                "v": "27"
            }, {
                "t": "Comunicaciones",
                "v": "16"
            }, {
                "t": "Ingenier\u00eda de Software",
                "v": "73"
            }, {
                "t": "Investigaci\u00f3n operativa (Sistemas)",
                "v": "358"
            }, {
                "t": "Redes de Informaci\u00f3n",
                "v": "18"
            }, {
                "t": "Simulaci\u00f3n (Sistemas)",
                "v": "360"
            }, {
                "t": "Teor\u00eda de Control",
                "v": "29"
            }]
        }, {
            "a": "4",
            "e": "1",
            "x": "0",
            "v": [{
                "t": "Administraci\u00f3n de Personal",
                "v": "30"
            }, {
                "t": "Criptograf\u00eda",
                "v": "35"
            }, {
                "t": "Emprendimientos Digitales",
                "v": "446"
            }, {
                "t": "Gerenciamiento de Proyectos Inform\u00e1ticos",
                "v": "40"
            }, {
                "t": "Inform\u00e1tica Industrial",
                "v": "447"
            }, {
                "t": "Programaci\u00f3n de la Producci\u00f3n Industrial",
                "v": "34"
            }, {
                "t": "Seguridad en Redes",
                "v": "31"
            }, {
                "t": "Sistemas de Informaci\u00f3n Geogr\u00e1fica",
                "v": "37"
            }, {
                "t": "Tecnolog\u00edas Avanzadas en la Construcci\u00f3n de Software",
                "v": "36"
            }]
        }, {
            "a": "5",
            "e": "0",
            "x": "0",
            "v": [{
                "t": "Administraci\u00f3n Gerencial",
                "v": "43"
            }, {
                "t": "Inteligencia Artificial",
                "v": "44"
            }, {
                "t": "Proyecto (Sistemas)",
                "v": "41"
            }, {
                "t": "Sistemas de Gesti\u00f3n",
                "v": "74"
            }]
        }, {
            "a": "5",
            "e": "1",
            "x": "0",
            "v": [{
                "t": " Sistemas Embebidos Aplicados a Rob\u00f3tica",
                "v": "477"
            }, {
                "t": "Arquitecturas de Proyectos en TI",
                "v": "58"
            }, {
                "t": "Aspectos Legales de las Nuevas Tecnolog\u00edas de la Informaci\u00f3n",
                "v": "46"
            }, {
                "t": "Bioinform\u00e1tica ",
                "v": "426"
            }, {
                "t": "Ciudades Digitales, Gobierno y Sociedad",
                "v": "478"
            }, {
                "t": "Comunicaci\u00f3n y Comercializaci\u00f3n de Productos y Servicios de IT",
                "v": "425"
            }, {
                "t": "Desarrollo de Aplicaciones para Dispositivos Moviles",
                "v": "479"
            }, {
                "t": "Desarrollo Emprendedor",
                "v": "427"
            }, {
                "t": "Financiamiento de Proyectos de Internet",
                "v": "54"
            }, {
                "t": "Gesti\u00f3n del Cambio Organizacional",
                "v": "51"
            }, {
                "t": "Implementaci\u00f3n de Arquitecturas de Software Concurrente",
                "v": "448"
            }, {
                "t": "Implementaci\u00f3n de Bases de datos NoSQL",
                "v": "421"
            }, {
                "t": "Infraestructura y Virtualizaci\u00f3n",
                "v": "423"
            }, {
                "t": "Inteligencia Artificial Avanzada",
                "v": "444"
            }, {
                "t": "Inteligencia de Negocios",
                "v": "59"
            }, {
                "t": "Marcos de Referencia en TI",
                "v": "445"
            }, {
                "t": "Marketing en Internet y Nueva Econom\u00eda",
                "v": "56"
            }, {
                "t": "Modelos de Negocios en Internet",
                "v": "49"
            }, {
                "t": "Modelos Organizacionales",
                "v": "45"
            }, {
                "t": "Pericias Inform\u00e1ticas",
                "v": "55"
            }, {
                "t": "Procesamiento de Se\u00f1ales",
                "v": "52"
            }, {
                "t": "Seguridad en Aplicaciones Web",
                "v": "475"
            }, {
                "t": "Sistemas Avanzados de Bases de Datos",
                "v": "50"
            }, {
                "t": "Sistemas de Costos y Presupuestos",
                "v": "53"
            }, {
                "t": "Sistemas Integrados de Gesti\u00f3n (Sistemas)",
                "v": "362"
            }, {
                "t": "Sistemas Mainframe",
                "v": "60"
            }, {
                "t": "Tecnolog\u00eda y Discapacidad",
                "v": "48"
            }, {
                "t": "Tecnolog\u00edas Aplicadas a Soluciones de Datos",
                "v": "476"
            }, {
                "t": "Tecnolog\u00edas Avanzadas en Redes ",
                "v": "424"
            }, {
                "t": "Tecnolog\u00edas Para la Explotaci\u00f3n de Informaci\u00f3n",
                "v": "61"
            }]
        }, {
            "a": None,
            "e": "0",
            "x": "1",
            "v": [{
                "t": "Pr\u00e1ctica Profesional Supervisada (Sistemas)",
                "v": "108"
            }]
        }]

        response = {'materias': materias}
        json.dumps(response)
        self.set_header("Content-Type", "application/jsonp;charset=UTF-8")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)
