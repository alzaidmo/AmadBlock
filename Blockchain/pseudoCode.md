AmadBlock Pseudo Code
----------------------

Ini mempool

Ini liste noeuds


THREAD Serveur
---
0. INIT
---
- Choix du port
- Démarrage du serveur sur le noeud
- Broadcast Request "Nouveau Noeud"
- Listening

1. LIEN CLIENT WEB (Automatiser)
---
- Recieve Request
- Identify "Web Request"
- Parse Request
	- Récupération du fichier .xml
- Create "ObjetPython" from xml data
	- Extract data
	- Assignation aux attributs 
- Mise en Mempool de l'objet
- Broadcast Request "MaJMempool"
- Listen

2. LIEN NOEUDS (Automatiser)
---
- Receive Request
- Identify "Node Request"
- Si "Nouveau noeud"
	- Ajouter IP noeud entrant à sa liste de noeud
- Si "Consensus"
	- Goto Consensus (Pipe vers Thread Mineur/Consensus) 
- Si "MaJMempool"
	- Si "ObjetPython" not in Mempool
		- Ajout "ObjetPython" à la Mempool


THREAD Mineur/Consensus
---
3. MINING (Alternatives)
---
- Preuve de travail (mining - en continu)
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
- Interconnexion des noeuds sans noeud central (Réseau local)
- Le client web envoie des données à 1 seul noeud, c'est ce dernier qui relaie.


Configuration de TEST
---
Thread 1/
- Connecter plusieurs machines sur un réseau local (192.168...)
- Lancer le serveur sur chacunes d'elles
- Constater la découverte des machines entre-elles
- Simuler l'arrivée d'une requête Web
- Constater l'ajout des infos au Mempool

Thread 2/
