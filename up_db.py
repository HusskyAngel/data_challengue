import subprocess
import logging  
from decouple import config 

try:
    logging.info("Levantando contenedor de la bd")

    up_instruction="""
            docker run -d \\
            --name {} \\
            -e POSTGRES_DB={} \\
            -e POSTGRES_USER={} \\
            -e POSTGRES_PASSWORD={} \\
            -v {} \\
            {}""".format(config("CON_NAME"),config("BD_NAME"),config("BD_USER"),config("BD_PASSWORD"),config("BD_PRIMARY_VOLUME"),config("IMG_POSTGRES_VERSION"))
    logging.info(up_instruction)
    subprocess.call(up_instruction,shell=True)
except ValueError: 
    logging.error("Error levantando el contenedor de la base de datos ")





