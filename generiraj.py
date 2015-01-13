import datetime
from random import randint

def datumi():
    '''
    Zgeneriramo tabelo datumov od leta 2012 do danes.
    '''
    tabela = []
    zacetniDatum = datetime.datetime(2014, 3, 1)
    delta = datetime.timedelta(days = 1)
    while (zacetniDatum < datetime.datetime.now()):
        tabela.append(zacetniDatum.strftime('%Y-%m-%d'))
        zacetniDatum += delta
    return tabela

def generirajVstopnice(imeDat):
    datoteka = open(imeDat, 'w')
    dat = datumi()
    film = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    zaposleni = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'] 
    datum = ''
    for j in dat:
        datum = j
        for l in zaposleni:
            IDzaposlenega = l
            for k in film:
                filem = k
                ukaz = "INSERT INTO vstopnice (filmi, zaposleni, datum) VALUES (" + str(filem) +" , " +str(IDzaposlenega) + " , '"  + datum + "'); \n"
                datoteka.write(ukaz)
    datoteka.close()
    print('Konec')


def generirajSpored(imeDat):
    datoteka = open(imeDat, 'w')
    dat = datumi()
    film = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    dvorane1 = ['1','2','3','4','5','6']
    datum = ''
    for j in dat:
        datum = j
        for k in film:
            stFilma = k
            for l in dvorane1:
                dvorane = l
                ukaz = "INSERT INTO spored (stevilka_filma, dvorana, datum) VALUES (" + str(stFilma) + "," +str(dvorane) + ",'" + datum + "'); \n"
                datoteka.write(ukaz)
    datoteka.close()
    print('Konec')

datumi()
generirajVstopnice('vstopnice.txt')
generirajSpored('spored.txt')


                
            
            


        
