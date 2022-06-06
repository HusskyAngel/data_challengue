from datetime import date 
import os 
import requests
import json 

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
        os.remove(os.path.join(path, data+"-"+today.strftime("%b-%d-%Y")+".csv"))
    else: 
        os.makedirs(path)
    #download and write data
    w=open(os.path.join(path,data+"-"+today.strftime("%b-%d-%Y")+".csv"),"bw+")
    r=requests.get(urls[data],allow_redirects=True)
    w.write(r.content)


download_data("museos")
     



