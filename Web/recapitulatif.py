# coding=utf-8

#Import du module
from lxml import etree

#Création de la racine de notre document
recapitulatif = etree.Element('recapitulatif')
liste = [['Hidderley','Quentin','+33643582284','','Air France', 'Paris Charles de Gaulle', 'Douala International']]
for perso in liste:
        #Création de la nouvelle personne
        personne = etree.SubElement(recapitulatif,'personne')
        #Nom
        nom = etree.SubElement(personne,'nom')
        nom.text = perso[0]
        #prenom
        prenom = etree.SubElement(personne,'prenom')
        prenom.text = perso[1]
        #Details de la réservation
        Reservation = etree.SubElement(personne, 'reservation')
        Compagnie = etree.SubElement(Reservation, 'Compagnie')
        Compagnie.text = perso[4]
        Depart = etree.SubElement(Reservation, 'Depart')
        Depart.text = perso[5]
        Arrivee = etree.SubElement(Reservation, 'Arrivee')
        Arrivee.text = perso[6]
        #Téléphone fixe
        if perso[2] != '':
                telephone = etree.SubElement(personne,'telephone')
                telephone.set('type','fixe')
                telephone.text = perso[2]
        #Téléphone mobile
        if perso[3] != '':
                telephone = etree.SubElement(personne,'telephone')
                telephone.set('type','mobile')
                telephone.text = perso[3]

try:
        #On ouvre (ou crée) le fichier xml pour travailler avec
        with open('recapitulatif.xml','w') as fichier:
                #En-tête du fichier xml
                fichier.write('<?xml version="1.0" encoding="UTF_8"?>\n')
                #On écrit tous les éléments précédemment déclarer
                fichier.write(etree.tostring(recapitulatif,pretty_print=True).decode('utf-8'))
except IOError:
        print('Problème rencontré lors de l\'écriture ...')
        exit(1)