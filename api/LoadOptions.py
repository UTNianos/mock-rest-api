from tornado.options import define, options

def load_options(config_file):

    # General application settings
    define('port', type=int, group='application', help='Port to run the application from.')
    define('compress_response', type=bool, group='application', help='Whether or not to compress the response.')

    # Security options
    define('serve_https', type=bool, group='application', help='Whether to serve the application via HTTPS or not.')
    define('ssl_cert', type=str, group='application', help='Path to the SSL certificate.')
    define('ssl_key', type=str, group='application', help='Path to the SSL key.')
    define('cookie_secret', type=str, group='application', help='Cookie signing secret.')
        
    options.parse_config_file(config_file)

    return options.group_dict('application')
