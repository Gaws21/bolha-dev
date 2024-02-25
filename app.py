import os
from app.config import config_dict
from app import app


# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

if DEBUG:
    app.logger.info('DEBUG            = ' + str(DEBUG)             )
    app.logger.info('FLASK_ENV        = ' + os.getenv('FLASK_ENV') )
    app.logger.info('Page Compression = ' + 'FALSE' if DEBUG else 'TRUE' )

if __name__ == "__main__":
    app.run()
