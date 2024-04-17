import requests
from bs4 import BeautifulSoup

from typing import List, Dict

def rechercher_produits(mot_clef: str, site_web: str) -> List[Dict]:

  produits = []

  # Envoyer une requête GET au site web avec le mot-clé dans la requête
  response = requests.get(site_web + "&q=" + mot_clef)

  # Vérifier le statut de la requête
  if response.status_code == 200:
    # print(response.content)
    # Analyser le contenu HTML de la page de résultats
    soup = BeautifulSoup(response.content, 'html.parser')
    soup.prettify()

    # Extraire les produits des résultats de recherche
    for produit in soup.find_all('div', {'class':'grid-item search-result large--one-fifth medium--one-third small--one-half on-sale'}):  
      nom_element = produit.find('a')  
      nom = nom_element.text if nom_element else "N/A"

      photo = produit.find('img')['src']  
      prix_element = produit.find('span', class_='product-item--sale-price')  
      prix = prix_element.text if prix_element else "N/A"

      produit_dict = {
          'nom': nom,
          'photo': photo,
          'prix': prix
      }
      
      # Ajouter le dictionnaire à la liste des produits
      produits.append(produit_dict)
      # print(produits)

  else:
    print(f"Erreur lors de la requête sur {site_web} : {response.status_code}")
  return produits


produits_kmerphone = []
# Exemple d'utilisation
mot_clef = "iphone"
# produits_glotelho = rechercher_produits(mot_clef, "https://glotelho.cm/")
produits_kmerphone = rechercher_produits(mot_clef, "https://kmerphone.com/search?type=product")

# print("Produits sur Glotelho:")
# for produit in produits_glotelho:
#   print(f"Nom: {produit['nom']}")
#   print(f"Photo: {produit['photo']}")
#   print(f"Quantité: {produit['quantite']}")
#   print(f"Prix: {produit['prix']}")
#   print("--------------------")

print("Produits sur Kmerphone:")
for produit in produits_kmerphone:
  print(f"Nom: {produit['nom']}")
  print(f"Photo: {produit['photo']}")
  # print(f"Quantité: {produit['quantite']}")
  print(f"Prix: {produit['prix']}")
  print("--------------------")
