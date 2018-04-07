from lxml import etree
import PNR
import Client

WebSender = Client.Client("convertisseur") 
hosts = set(["localhost", "192.168.11.23"])

def converter(fichier,hosts):
	f = fichier
	tree = etree.parse(f)
	balises = ['id','nom', 'prenom', 'telephone', 'compagnie', 'depart', 'arrivee']
	values = []
	for balise in balises :
		for branch in tree.xpath("/reservation/" + balise):
			values.append(branch.text)
	outPNR= PNR.PNR(values[0],values[1],values[2],values[3],values[4],values[5],values[6])
	print(outPNR)
	
	for host in hosts:
		WebSender.conToNode(host, 4254)
		WebSender.webTrans(outPNR)
	return(outPNR)


if __name__ == '__main__':
	monPNR = converter("templates/recapitulatif.xml", hosts)



