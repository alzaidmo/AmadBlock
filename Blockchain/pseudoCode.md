AmadBlock Pseudo Code
----------------------

Code de noeud
---


0. INIT
---
- Installation Client/Serveur sur le noeud
	* Flask *

1. LIEN CLIENT (Automatiser)
---
- Communicatin avec le client continue
- Mise en Mempool des transactions arrivantes


2. LIEN NOEUDS (Automatiser)
---
- Echanges entre noeuds (HTTP/TCP)
	- mise à jour de l'état du réseau
		- liste des noeuds directement connectés
	- diffusion des transactions arrivantes aux voisins directs
	- réception des transactions arrivantes ( ! doublons)
	- Mise en Mempool des nouvelles transactions


3. MINING (Alternatives)
---
- Preuve de travail (mining)
	- Création d'un bloc de transactions
	- Calcul d'une preuve de travail avec la preuve de travail du bloc précédent
	- Ajout du bloc à la Blockchain locale
	- Emission d'ue requête de consensus


4. CONSENSUS (Alternatives)
---
- Vérification de l'intégrité de la Blockchain
- Vérification de la preuve de travail
- Calcul de longueur
- Choix de la bonne blockchain
- Mise à jour
	- Diffusion et recopie de la Blockchain qui fait autorité



CONTRAINTES
---
- Même code sur tous les noeuds
- Interconnexion des noeuds sans noeud central
