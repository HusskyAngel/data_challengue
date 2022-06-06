from datetime import date 
import os 
import requests
import json 
import logging

def download_data(data:str):
    """
    download data from json urls.  
    data-> str  -> {museos, cines, bibliotecas}  
    """
    #load urls 
    file=open("urls.json","r") 
    urls=json.load(file) 
    #get current date 
    today=date.today()
    month=today.strftime("%B")
    year=today.year
    path=os.path.join("data",data,str(year)+"-"+month)
    #test if the data already exists
    if os.path.isfile(os.path.join(path, data+"-"+today.strftime("%b-%d-%Y")+".csv")):  
        logging.debug ("Ya hay un archivo con la misma fecha, voy a eliminar el archivo.")
        os.remove(os.path.join(path, data+"-"+today.strftime("%b-%d-%Y")+".csv"))
    elif not os.path.isdir(path): 
        logging.debug ("creando path") 
        os.makedirs(path)
    #download and write data
    w=open(os.path.join(path,data+"-"+today.strftime("%b-%d-%Y")+".csv"),"bw+")
    logging.debug ("descargando la información de "+ urls[data])
    try:
        r=requests.get(urls[data],allow_redirects=True)
        w.write(r.content)
    except ValueError:
        logging.error("error descargando el archivo")


download_data("museos")
     



