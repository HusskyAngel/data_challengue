from datetime import date 
from decouple import config
import datetime 
import os 
import requests
import json 
import logging
import sys 

def download_data(data:str):
    """
    download data from json urls.  
    data-> str  -> {museos, cines, bibliotecas}  
    """
    #logging configuration 
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.FileHandler(os.path.join(config("LOGS_STORAGE"),str(datetime.datetime.now())+".log")),
                              logging.StreamHandler()])
    #load urls 
    file=open(config("URLS_FILE"),"r") 
    urls=json.load(file) 
    #get current date 
    today=date.today()
    month=today.strftime("%B")
    year=today.year
    path=os.path.join(config("DATA_STORAGE"),data,str(year)+"-"+month)
    #test if the data already exists
    if os.path.isfile(os.path.join(path, data+"-"+today.strftime("%b-%d-%Y")+".csv")):  
        logging.info("Ya hay un archivo con la misma fecha, voy a eliminar el archivo.")
        os.remove(os.path.join(path, data+"-"+today.strftime("%b-%d-%Y")+".csv"))
    elif not os.path.isdir(path): 
        logging.info("creando path") 
        os.makedirs(path)
    #download and write data
    w=open(os.path.join(path,data+"-"+today.strftime("%b-%d-%Y")+".csv"),"bw+")
    logging.info("descargando la información de "+ urls[data])
    try:
        r=requests.get(urls[data],allow_redirects=True)
        w.write(r.content)
        logging.info("archivo guardado con exito con exito")
    except ValueError:
        logging.error("error descargando el archivo " + str(ValueError))
        sys.exit()

     



