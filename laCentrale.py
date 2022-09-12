import requests
import json
import http.client, urllib
import time,datetime

class laCentrale:
        
    def __init__(self, brand, model, categories, energies, priceMin, priceMax, goodDealBadges, firstHand, regions, yearMin, yearMax, mileageMin, mileageMax, gearbox, options, doors, seats, ratedHorsePowerMin, ratedHorsePowerMax, critAirMax, consumptionMax, externalColors, internalColors, allWarranty, customerFamilyCodes, order, sort):
        self.brand = brand
        self.model = model
        self.categories = categories
        self.energies = energies
        self.priceMin = priceMin
        self.priceMax = priceMax
        self.goodDealBadges = goodDealBadges
        self.regions = regions
        self.yearMin = yearMin
        self.yearMax = yearMax
        self.mileageMin = mileageMin
        self.mileageMax = mileageMax
        self.firstHand = firstHand
        self.gearbox = gearbox
        self.options = options
        self.doors = doors
        self.seats = seats
        self.ratedHorsePowerMin = ratedHorsePowerMin
        self.ratedHorsePowerMax = ratedHorsePowerMax
        self.critAirMax = critAirMax
        self.consumptionMax = consumptionMax
        self.externalColors = externalColors
        self.internalColors = internalColors
        self.allWarranty = allWarranty
        self.customerFamilyCodes = customerFamilyCodes
        self.order = order
        self.sort = sort
        self.results = []
        self.newResults = []
       
    def printList(self):
        for element in self.results:
            print(element)
            print()
    
    @staticmethod 
    def getInfo(data, parameter):
        try:
            return data["item"][parameter]
        except:
            return False
    
    @staticmethod 
    def getInfo2(data, parameter):
        try:
            return data["item"]["vehicle"][parameter]
        except:
            return False

    @staticmethod 
    def getAllThePhotos(link,length):
        photosLinks = []
        for i in range(0,length):
            photosLinks.append(link[:-5]+str(i)+".jpg")
        return photosLinks
    
    def getRecentResults(self,delta,results):
        l = []
        for element in results:
            if time.time() - time.mktime(datetime.datetime.strptime(element[15], "%Y-%m-%d").timetuple()) < delta*2:
                l.append(element)
        self.newResults = l.copy()
        return l
    
    @staticmethod 
    def send_notification(liste):
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
          urllib.parse.urlencode({
            "token": "",
            "user": "",
            "message":
              str(liste[0]) + " \n" + str(liste[-1]),
          }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()
        return print("Notification sent")
    

    def recherche(self):

        url = "https://recherche.lacentrale.fr/v3/search"

        querystring = {"makesModelsCommercialNames":self.brand+":"+self.model, "sort":self.sort, "order":self.order, "page":"0", "pageSize":"100", "categories":self.categories, "energies":self.energies, "goodDealBadges":self.goodDealBadges, "priceMin":self.priceMin, "priceMax":self.priceMax, "firstHand":self.firstHand, "regions":self.regions, "yearMin":self.yearMin, "yearMax":self.yearMax, "mileageMin":self.mileageMin, "mileageMax":self.mileageMax, "gearbox":self.gearbox, "options":self.options, "doors":self.doors, "seats":self.seats, "ratedHorsePowerMin":self.ratedHorsePowerMin, "ratedHorsePowerMax":self.ratedHorsePowerMax, "externalColors":self.externalColors, "internalColors":self.internalColors, "consumptionMax":self.consumptionMax, "critAirMax":self.critAirMax, "allWarranty":self.allWarranty, "customerFamilyCodes":self.customerFamilyCodes}

        payload = ""
        headers = {
            "Accept": "application/json",
            "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Authorization": "Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjEwODcwNjMsInZlcnNpb24iOiIyMDE4LTA3LTE2IiwidXNlckNvcnJlbGF0aW9uSWQiOm51bGwsInVzZXJfY29ycmVsYXRpb25faWQiOm51bGwsImxvZ2dlZFVzZXIiOnsiY29ycmVsYXRpb25JZCI6bnVsbCwicmVmcmVzaFRva2VuVFRMIjoxNjYxMTczMTYzfSwibW9kZU1hc3F1ZXJhZGUiOmZhbHNlLCJhdXRob3JpemF0aW9ucyI6eyJ2ZXJzaW9uIjoiMjAxOC0wNy0xNiIsInN0YXRlbWVudHMiOlt7InNpZCI6IioiLCJlZmZlY3QiOiJEZW55IiwiYWN0aW9ucyI6WyIqIl0sInJlc291cmNlcyI6WyIqIl19XX0sImlhdCI6MTY2MTA4Njc2M30.SocI9ckkW1-3xtt14SAwD-KdaW8Bq4_tgImDEW9FKefrRyoCmXeTZSa-_vTnbTeEvOFCb9_CxLxgXvVz2N0W9NHufmk5b9fL6-pI7uegLt98RcJcz89OtYyUuk-a30UiRr8eos_sMp-k4AQRh4UROXDU-xf6B8OA226-W4-US3DX8WTwcOhy0dQmUlh2dsrlN1AnneONlQSplVC_bKorvjjrxXPPRE5vcDbYwUDc2RUH0gF0pmTacJh8jJ41vsaQO-8g2pz29mHtyYsETtev5S0HnifYuj5969yduRXeFejgbhgEO8ZpiWwCTmUmx7rnLvQNSVHkUdSnprmDWyb0sA",
            "Connection": "keep-alive",
            "Origin": "https://www.lacentrale.fr",
            "Referer": "https://www.lacentrale.fr/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-GPC": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36",
            "X-Client-Source": "lc:recherche:front",
            "x-api-key": "2vHD2GjDJ07RpNvbGYpJG7s6bQNwRNkI9SEkgQnR"
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        jsonData = json.loads(response.text)["hits"]
        jsonDisplay = json.dumps(jsonData, indent=4, sort_keys=True)

        listResults = []
        listLength = len(jsonData)


        for element in jsonData:
            ref = laCentrale.getInfo(element,"reference")
            link = "https://www.lacentrale.fr/auto-occasion-annonce-" + str(ord(ref[0])) + str(ref[1:]) + ".html"
            constructorWarrantyDate = laCentrale.getInfo(element,"constructorWarrantyDate")
            manufacturerWarrantyDuration= laCentrale.getInfo(element,"manufacturerWarrantyDuration")
            year = laCentrale.getInfo2(element,"year")
            model = laCentrale.getInfo2(element,"model")
            category = laCentrale.getInfo2(element,"category")
            make = laCentrale.getInfo2(element,"make")
            version = laCentrale.getInfo2(element,"version")
            mileage = laCentrale.getInfo2(element,"mileage")
            commercialName = laCentrale.getInfo2(element,"commercialName")
            picturesCount = laCentrale.getInfo(element,"picturesCount")
            customerType = laCentrale.getInfo(element,"customerType")
            price = laCentrale.getInfo(element,"price")
            try:
                location = element["item"]["location"]["visitPlace"]
            except:
                location = False
            firstOnlineDate = laCentrale.getInfo(element,"firstOnlineDate")
            try:
                photoUrl = str(laCentrale.getInfo(element,"photoUrl")).split('/')
                photoUrl = photoUrl[0]+"//"+photoUrl[1]+"/"+photoUrl[2]+"/852x640/"+photoUrl[4]
                photosUrl = laCentrale.getAllThePhotos(photoUrl, picturesCount)
            except:
                photosUrl=[]
                pass

            listResults.append([ref,link,constructorWarrantyDate,manufacturerWarrantyDuration,year,model,category,make,version,mileage,commercialName,picturesCount,customerType,price,location,firstOnlineDate,photosUrl])
        self.results = listResults
        return self.results

# Marque de la voiture
brand = "ALPINE"

# Modèle de la voiture
model = "A110"

# Catégorie de la voiture
# 47 : 4x4, SUV, Crossover
# 40 : Citadine
# 41_42 : Berline
# 43 : Break
# 46 : Cabriolet
# 45 : Coupé
# 44 : Monospace
# 82 : Bus & Minibus
# 85 : Fourgonnette
categories = ""

# Energie pour alimenter la voiture
# dies : Diesel
# ess : Essence
# elec : Electrique
# hyb : Hybride
# plug_hyb : Hybride rechargeable
# gpl : Bicarburation essence / GPL
# eth : Bicarburation essence éthanol
# alt : Autres énergies alternatives
energies = ""

# Prix minimum et maximum de la voiture
priceMin = ""
priceMax = ""

# Badge estimatif de la voiture
# VERY_GOOD_DEAL : Très bonne affaire
# GOOD_DEAL : Bonne affaire
# EQUITABLE_DEAL : Offre équitable
# BAD_DEAL : Au dessus du marché
# OFF_DEAL : Hors marché
goodDealBadges = ""

# Région où se situe la voiture
# FR-ARA : Auvergne-Rhône-Alpes
# FR-BFC : Bourgogne-Franche-Comté
# ...
regions = ""

# Année de mise en circulation de la voiture
yearMin = ""
yearMax = ""

# Kilométrage de la voiture
mileageMin = ""
mileageMax = ""

# Première main
# false / true
firstHand = ""

# Boite de vitesse de la voiture
# AUTO : Automatique
# MANUAL : Mécanique
gearbox = ""

# Options de la voiture
# TOIT_OUVRANT : Toit ouvrant
# ATTELAGE : Crochet d'attelage
# CLIMATISATION : Climatisation
# GPS : GPS
# CAMERA_RECUL : Caméra de recul
# RADAR_RECUL : Radar de recul
# CUIR : Cuir
# BLUETOOTH : Bluetooth
# TOIT_PANORAMIQUE : Toit panoramique
# REGULATEUR : Régulateur
# CARPLAY : CarPlay
# Palette : Palette au volant
# GRIP_CONTROL : Grip control
options = ""

# Nombres de portes
# 2, 3, 4, 5, 6 ou plus
doors = ""

# Nombres de places
# 1, 2, 3, 4, 5, 6, 7, 8, 9
seats = ""

# Puissance fiscale de la voiture
ratedHorsePowerMin = ""
ratedHorsePowerMax = ""

# Crit'air maximum de la voiture
# 0,1,2,3,4,5
critAirMax = ""

# Consommation maximum de la voiture 
# 4, 5, 6, 7, 9, 13, 17 (L/100km)
consumptionMax = ""

# Couleur extérieure de la voiture
# Argent, Beige, Blanc, Bleu, Bordeaux, Gris, Ivoire, Jaune, Marron, Noir, Orange, Rose, Rouge, Vert, Violet
externalColors = ""

# Couleur intérieure de la voiture
# Beige, Blanc, Bleu, Fauve, Gris, Ivoire, Marron, Noir, Rouge, Vert
internalColors = ""

# Garantie de la voiture
# false / true
allWarranty = ""

# Type de vendeur de la voiture
# PART : Particulier
# CONCESSIONNAIRE : Concessionnaire
# AGENT : Agent
# CENTRE_MULTIMARQUES : Centre multimarques
# LOUEUR : Loueur
# GARAGISTE : Garagiste
# REPARATEUR_AGREE : Réparateur agréé
# INTERMEDIAIRE : Intermédiaire
# DISTANCE : 100 % à distance
customerFamilyCodes = ""

# SORT / ORDER
# price / asc : Prix croissant
# price / desc : Prix décroissant
# firstOnlineDate / desc : Annonces plus récentes
# firstOnlineDate / asc : Annonces moins récentes
# mileage / asc : Kilométrage croissant
# mileage / desc : Kilométrage décroissant
# goodDealBadge / asc : Meilleures affaires
sort="firstOnlineDate"
order="desc"

objet = laCentrale(brand, model, categories, energies, priceMin, priceMax, goodDealBadges, firstHand, regions, yearMin, yearMax, mileageMin, mileageMax, gearbox, options, doors, seats, ratedHorsePowerMin, ratedHorsePowerMax, critAirMax, consumptionMax, externalColors, internalColors, allWarranty, customerFamilyCodes, order, sort)
resultats = objet.recherche()
print(objet.getRecentResults(86400,resultats))
for elements in objet.newResults:
    # laCentrale.send_notification(elements)