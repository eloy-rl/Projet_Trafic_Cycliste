import pandas as pd
import streamlit as st




# Configuration de la page

st.set_page_config(
    page_title="Projet trafic Cycliste",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded",
)
   # Ajouter une image
st.image("images/couv.png", caption="Projet Trafic Cycliste - DataScientest - DEC24_BOOTCAMP_DA", use_container_width=True)


def main():
    st.title("Projet trafic Cycliste")
    
    

    # Sidebar pour la navigation
    st.sidebar.title("Navigation")
    sections = [
        "Introduction",
        "1. Cadre du projet",
        "2. Axes d'analyses",
        "3. Clustering des données",
        "4. Conclusions"
    ]
    choice = st.sidebar.radio("Aller à", sections)

    if choice == "Introduction":
        introduction()
    elif choice == "1. Cadre du projet":
        cadre_projet()
    elif choice == "2. Axes d'analyses":
        axes_analyses()
    elif choice == "3. Clustering des données":
        clustering()
    elif choice == "4. Conclusions":
        conclusions()

def introduction():
    st.header("Introduction")
    st.write("""Paris est une ville où la mobilité douce occupe une place centrale dans les politiques publiques. Elle est engagée dans une transformation urbaine accélérée, avec pour objectif de réduire la pollution et d’améliorer la qualité de vie de ses habitants.
              
La capitale française, avec ses rues emblématiques investit massivement sur son ambition de devenir une référence mondiale en promouvant l’usage du vélo comme mode de transport quotidien.
 
Le Plan Vélo, c’est 150 millions d’euros au budget 2015-2020 du département ainsi que 250 millions d’euros pour 2021-2026. Il prévoit sur cette seconde période, la création de 180 km de pistes cyclables supplémentaires, la sécurisation des intersections dangereuses et le développement d’infrastructures adaptées et illustre pleinement l’ambition de la ville.

Cependant, malgré ces investissements significatifs, des défis subsistent pour comprendre et optimiser les conditions favorisant l’utilisation du vélo dans la ville.

Ce projet d’étude a donc pour objectif d’avancer sur cette question cruciale : quels sont les facteurs déterminants qui encouragent ou freinent l’usage du vélo dans une ville comme Paris ?

En particulier, l’impact des facteurs suivants mérite d’être étudié :

- Les caractéristiques socio-économiques des quartiers, telles que la densité de population et la présence d’entreprises, de commerces,
- La présence de zones touristiques dans la ville,
- L’accès aux infrastructures cyclables, telles que les pistes sécurisées ou les zones de stationnement pour vélos,
- Les politiques publiques, comme les restrictions ou  incitations financières sur les véhicules motorisés,
- etc...

En approfondissant ces aspects, nous espérons mettre en lumière des outils pouvant être travailléser pour contribuer à l’atteinte des objectifs de la mairie de Paris et à l’amélioration des différents endroits cyclables de la ville.
""")

def cadre_projet():
    st.header("1. Cadre du projet et prise de connaissance des données fournies")
    
    st.subheader("a. Equipe")
    st.write("""Notre équipe, composée de quatre passionnés de données, habite en Ile-de-France et pour moitié directement dans Paris. Elle est donc directement concernée par la politique de la ville, dans le cadre de son lieu d’habitation et/ou dans ses déplacements personnels et professionnels.
             
Nous, Eloy, Erick, Philippe et Delphine, souhaitons mettre à profit les compétences acquises au cours de notre formation de Data Analyse pour explorer cette problématique en profondeur.

Novices en développement Python notamment, ce projet axé sur la data visualisation nous a rassemblé.
""")
    
    
    st.subheader("b. Jeux de données")
    st.write("""Le projet s’appuie initialement sur un fichier .csv en open data fourni par la Mairie de Paris et contenant une analyse des données récoltées par des compteurs vélo. En effet, la ville de Paris déploie depuis plusieurs années des compteurs à vélo permanents pour évaluer le développement de la pratique cycliste.
             
Au cours du projet, afin d’atteindre nos objectifs de mesure d’impact de différents paramètres sur le trafic cycliste, d’autres fichiers de données seront étudiés et croisés avec le fichier initial. Tous proviennent d’open data fournies par les acteurs suivants : 
             
- la Mairie de Paris
    - Délimitation des arrondissements de la ville
    - Zones touristiques internationales 
    - Zones de rencontres
    - Zones piétonnes
    - Zones tarifaires du stationnement sur voies publiques pour les véhicules motorisés
    - Le stationnement vélo sur voies publiques
    - Les aménagements cyclables
    - L’emplacement des stations Vélib
    
- la Région Ile-de-France    
    - Principaux sites touristiques en Ile-de-France
    
- l’INSEE    
    - Tableau comparatif des arrondissements de Paris selon des critères sociaux-démographiques
- Ile-de-France Mobilité    
    - Coordonnées des "**pôles d’échanges internationaux**"
""")
    
    st.subheader("c. Analyse du premier jeu de données, Cleaning et Pre-Processing")
    st.write(""" Notre jeu de données initial comporte 952 142 lignes pour 16 colonnes.
Chaque ligne correspond :
- à un comptage des vélos, 
- passés par heure ,
- devant un compteur, 
- sur un site de comptage donné. 

Tout comptage est lié à une photo enregistrée. Chaque ligne de comptage horaire référencie donc les photos prises chaque heure.


__Liste des colonnes et description__

__(TABLEAU)__

*Identifiant du compteur
2 séries de 9 chiffres séparées par un tiret : représente un indication géographique combinée à une orientation de prise de vue.
Nom du compteur
Nom du compteur. D'habitude l'adresse avec des précisions quand plus d'un compteur par site de comptage. Example: 28 boulevard Diderot O-E et 28 boulevard Diderot E-O
Identifiant du site de comptage
Idem au nom de la colonne
Nom du site de comptage
Nom du site de comptage correspond fréquemment à son adresse. Parfois, on trouve des détails ajoutés à l'adresse pour plus de précision. Example: "Face au 49 boulevard du Général Martial(...)"
Comptage horaire
Nombre de vélos comptés dans l'heure
Date et heure de comptage
Idem au nom de la colonne
Date d'installation du site de comptage
Idem au nom de la colonne
Lien vers photo du site de comptage
Lien d'une photo prise depuis le compteur
Coordonnées géographiques
Coordonnées géographiques du site de comptage = Latitude, Longitude
Identifiant technique compteur
Identifiant technique qui correspond au site de comptage plutôt qu'aux compteurs. On peut trouver deux fois le même ID technique pour deux compteurs différents, mais pas pour deux sites de comptage différents
ID Photos
Lien qui ne marche pas
test_lien_vers_photos_du_site_de_comptage_
Lien d'une photo prise depuis le compteur
id_photo_1
Seul valeur : "https:"
url_sites
Lien qui ne marche pas
type_dimage
décrit le format de l'image prise: jpeg
mois_annee_comptage
Idem au nom de la colonne*


    
Pour la suite du projet, nous n’avons pas considéré comme pertinentes au regard de nos objectifs les colonnes du fichier de données traitant des photos : “Lien vers photo du site de comptage”, “ID Photos” ,  “test_lien_vers_photos_du_site_de_comptage_”, “id_photo_1”, “url_sites, type_dimage”.  


Le fichier nécessite un nettoyage avant traitement car de nombreuses données sont manquantes.
- Correction des noms de compteurs
    - Certains noms de compteurs ont été mal écrits alors qu’ils correspondent au même site (ex : 'Face au 48 quai de la marne Face au 48 quai de la marne Vélos NE-SO' et 'Face au 48 quai de la marne NE-SO'

- Traitement des valeurs manquantes
  - Les données manquantes sont regroupées sur les mêmes lignes et sont dûes aux erreurs sur les noms de compteur. 
    Plusieurs colonnes peuvent être complétées à l’aide des données connues des autres lignes : 
    - Identifiant du compteur
    - Identifiant du site de comptage
    - Nom du site de comptage
    - Date d'installation du site de comptage
    - Identifiant technique compteur
    - Coordonnées géographiques
- Les NA d’autres colonnes ne sont pas gérés car les colonnes ne sont pas utilisées pour les analyses.

- Correction des types de données
Les dates doivent être mises au format Datetime

- Adaptation du DataFrame aux analyses à venir
    - Split de la colonne 'Coordonnées géographiques' en 2 colonnes ‘latitude’ et ‘longitude’
    - Création de colonnes "Date et heure de comptage_annee", "Date et heure de comptage_mois", "Date et heure de comptage_jour”, "Date et heure de comptage_heure" à partir de la colonne "Date et heure de comptage"
    - Création de colonnes "Date d'installation_annee", "Date d'installation_mois" à partir de la colonne "Date d'installation du site de comptage"
    - Création de colonnes "Date d'installation_annee", "Date d'installation_mois" à partir de la colonne "Date d'installation du site de comptage"
    - Création d’une colonne "c_ar" correspondant à l’arrondissement du site de comptage.""")
    
    st.subheader("d. Visualisations du jeu de données initial")
    st.write(""" __Exploration globale__

L’étude de la date d’installation des compteurs est cohérente avec les phases du Plan vélo mis en place au niveau de la ville de Paris.

En 2019, le nombre de compteurs passe de 10 à une 40aine de compteurs installés. Ce chiffre est doublé en 2020 pour atteindre environ 80 compteurs.

2021 marque le début de la seconde phase du plan vélo. Il faut attendre 2023 pour observer une 3ème vague d’installation de compteurs permettant d’approcher la centaine.

L’analyse de la distribution par site de comptage démontre que le passage vélo devant les compteurs est très hétérogène.
Par ailleurs, il y a énormément d’outliers sur tous les sites : la nature des données nous fait supposer qu’il s’agit de pics de comptage liés sans doute à des événements exceptionnels.

L’identification d’adresses dans Paris nous invite à étudier leur localisation géographique en prenant en main la librairie Folium de Python.



La répartition des compteurs n’est pas homogène sur l’ensemble du territoire de la ville de Paris. 


Le 6eme, le 9ème et le 18ème arrondissement n’en comptent aucun. Il faut garder en tête cet aspect avant de généraliser nos analyses.

La vue des nombreux outliers nous incite à travailler avec la médiane de comptage horaire préférentiellement à la moyenne. En effet, la médiane sera moins influencée par nos valeurs extrêmes.

3 arrondissements se distinguent largement sur le nombre de photos prises par heure : le 2ème, le 10ème ainsi que le 11ème arrondissement. 
Nous trouvons d’ailleurs dans ces arrondissements des compteurs localisés dans le top 10 en termes de médiane de comptage horaire.


Nous observons par ailleurs que 5 des 10 compteurs situés dans le bottom 10 sont localisés en extrême périphérie de la ville. 
Les Top 10 sont quant à eux plutôt vers le centre.

Explorons individuellement quelques compteurs :


On remarque sur la carte que le compteur Quai d'Orsay E-O, dans le top 10, est très proche des sites de comptage Totem Cours la Reine O-E et Quai des Tuileries SE-NO qui appartiennent au bottom 10 (croisée des arrondissements 8 / 7 et 1).
Pour essayer de comprendre, on regarde de plus près ces 3 sites de comptage : 
Environ 20% d’enregistrements sont à zéro sur les sites de comptage Totem Cours la Reine et Quai des Tuileries. 
Ces enregistrements à 0 sont particulièrement importants sur la période d’avril à septembre.
Nombre de comptage à 0 sur le site 
Totem Cours la Reine O-E 

Cette donnée nous rappelle que pendant la période des jeux olympiques 2024 à Paris, un périmètre de sécurité limitant la circulation de tout type autour du Grand Palais a été mis en place. Nous supposons que les 2 compteurs Bottom analysés ont été impactés par ces mesures.
Source : Le Parisien
”Les premières fermetures de voies interviennent à Paris dès ce vendredi 17 mai. Idem pour le métro. La ligne 12 ne marquera plus l’arrêt à Concorde à partir de ce jour. Objectif : permettre l’installation des infrastructures pour les JO de Paris 2024.”


Source : Mairie de Paris
“Des circulations vélo modifiées pour l'organisation des Jeux”

""")
   
    
    st.write(""" __Tendances de passage vélo en fonction du temps__ 
             
La date et l’heure de comptage nous permettent d’étudier des tendances de passage vélo en fonction des différents moments de la journée ou de l’année. 

Notre jeu de données initial comprend des enregistrements sur 13 mois calendaires que nous choisissons de réduire à l’année 2024.

Deux pics de comptage sont très clairement identifiés du lundi au vendredi entre 6h et 8h le matin puis entre 16h et 18h le soir.
Les déplacements professionnels ou scolaires semblent jouer un rôle sur le trafic cycliste. 
Le samedi et le dimanche la courbe est beaucoup plus arrondie entre 8h et 18h.
Ce schéma est confirmé par l’analyse de tendance sur l’année. 

Nous notons également que les mois de juin et septembre semblent les mois les plus denses pour le trafic cycliste. 
Il y a d’ailleurs une légère augmentation de janvier à juin. 
Les mois de décembre et d’août sont par contre les mois les plus faibles : nous émettons l’hypothèse des conditions climatiques pour décembre et des congés d’été pour le mois d’Août.
""")
    
    
    st.subheader("e. Observations à l'issue de cette étape")
    st.write("""Pour répondre à notre objectif de quels sont les facteurs déterminants qui encouragent ou freinent l’usage du vélo dans une ville comme Paris, notre base de données n’est pas suffisante et nécessite d’être croisée avec des données complémentaires.
Le champ des possibles est très large et nous devons nécessairement faire des choix étant donné le temps d’étude sur ce projet dans le cadre du bootcamp Datascientest.
Plusieurs axes identifiés ci-dessus par exemple ne seront pas étudiés : influence des conditions climatiques, influence des périodes de congés et jours fériés.
""")


#def axes_analyses():
 #   st.header("2. Axes d'analyses")
  #  axes = [
   #     "a.",
    #    "b. Interdiction de stationnement motorisé sur la voie publique et trafic cycliste",
     #   "c. c. Caractéristiques statistiques INSEE des arrondissements et trafic cycliste",
      #  "d. Stationnements vélo",
       # "e. Infrastructure des pistes cyclables",
       # "f. Localisation des bornes vélib",
        #"g. Zones / sites touristiques"
       # ]     
   
def axes_analyses():
    st.header("2. Axes d'analyses")
    axes = [
        "Coût de stationnement sur voies publiques des véhicules motorisés et trafic vélo",
        "Interdiction de stationnement motorisé sur la voie publique et trafic cycliste",
        "Caractéristiques statistiques INSEE des arrondissements et trafic cycliste",
        "Stationnements vélo",
        "Infrastructure des pistes cyclables",
        "Localisation des bornes vélib",
        "Zones / sites touristiques"
        ]     
    
    #selected_axes = st.multiselect("Choisissez les axes d'analyse à afficher :", axes)
    
    
    #for axe in axes:
     #   st.subheader(axe)
      # st.write(f"""  
              
              
    analyses = {
        "Coût de stationnement sur voies publiques des véhicules motorisés et trafic vélo",
        "Interdiction de stationnement motorisé sur la voie publique et trafic cycliste",
        "Caractéristiques statistiques INSEE des arrondissements et trafic cycliste", 
        "Stationnements vélo disponibles et trafic cycliste.",
        "Infrastructure des pistes cyclables",
        "Localisation des bornes vélib et trafic cycliste", "Zones / sites touristiques et trafic cycliste"
        }              
                
    for axe in axes:
            with st.expander(axe, expanded=False):
                st.write(f"""Analyse pour {axe}...    


"Coût de stationnement sur voies publiques des véhicules motorisés et trafic vélo"
Le fichier Geojson des zones de stationnement pour véhicules motorisés est récupéré sur le site de la mairie de Paris.
Nous utilisons Folium pour mettre sur la même carte les sites de comptage en fonction de la médiane des comptages horaires.

Globalement, on peut voir que les médianes du comptage horaire sont plus élevées dans ala zone tarifaire 1 où l'heure de stationnement coûte entre 4€ et 6€, par rapport à la zone tarifaire 2 ou l'heure de stationnement coûte entre 2,4€ et 6€ (source).
Cette carte identifie clairement que le trafic vélo le plus dense est localisé dans la zone 1 de stationnement des véhicules motorisés, c'est-à-dire la plus chère. 
Il semblerait donc que le prix du stationnement sur la voie publique des véhicules motorisés ait une influence positive sur le trafic vélo.""")


   

    for axe in axes:
            with st.expander(axe, expanded=False):
                st.write(f"""Analyse pour {axe}...
                  
"Interdiction de stationnement motorisé sur la voie publique et trafic cycliste" 
            
Toujours dans le cadre du trafic motorisé, nous nous sommes intéressés à l'influence du nombre de places de stationnement interdites pour les véhicules motorisés dans une zone donnée, et à son impact sur le trafic vélo. Nous avons récupéré la base de données de la Mairie de Paris à ce sujet, puis l'avons croisée avec les médianes des comptages horaires des sites de comptage, à l'aide d'une carte thermique (heatmap). Sur cette carte, les points blancs représentent les sites de comptage, et leur taille varie en fonction de la médiane du comptage horaire des vélos sur ces sites.

On peut observer sur la carte deux éléments qui attirent notre attention. D'une part, les arrondissements du centre de Paris semblent présenter une forte concentration de zones d’interdiction de stationnement (zones jaunes, orange et rouges), avec peu de zones dégagées. Autrement dit, à l’exception des Tuileries, peu de places de stationnement sur la voie publique sont disponibles dans ces arrondissements. Dans le même sens, ces arrondissements affichent les médianes des comptages horaires de vélos les plus élevées de Paris.
Une autre observation concerne le 11ème arrondissement, où l’on note un regroupement de zones interdites au stationnement motorisé autour des sites de comptage affichant une médiane élevée. Tous ces éléments nous permettent de réaffirmer l’hypothèse d’un lien potentiel entre les mesures contre le trafic motorisé et l’affluence de vélos.""")
      
    for axe in axes:
            with st.expander(axe, expanded=False):
                st.write(f"""Analyse pour {axe}...          
        
"Caractéristiques statistiques INSEE des arrondissements et trafic cycliste"
_Nous récupérons du site INSEE différentes statistiques sur Paris en fonction des arrondissements:__")

- 'Population en 2021'
- 'Densité de la population - nombre d''habitants au km² - en 2021'
- 'Superficie en 2021, en km²'
- 'Nombre d''établissements actifs fin 2022'
- 'Part du commerce, transports et services divers, en %'
    ,

    __Nous allons analyser ces paramètres et les comparer aux médianes de comptage horaire.__
    __Analyse en fonction de la population et de sa densité__


    Les arrondissements 15, 20, 18, 19, et 13 sont les 5 arrondissements les plus peuplés de Paris. On se demandait si le nombre de sites de comptage par arrondissement avait un lien avec sa population.
    Les deux visualisations ci-dessus ne vont pas nécessairement dans notre sens. 
    Certes dans le 15ème et le 19ème arrondissement, on trouve plus de sites de comptage par rapport à d''autres arrondissements moins peuplés. Malgré tout, un arrondissement comme le 20ème, qui occupe la 2ème place en termes de population, compte moins de compteurs que le 7ème, 8ème ou 17ème, moins peuplés.

    Peut-être y a-t-il un lien avec la surface des arrondissements?
    Nous recommençons cette même analyse en étudiant cette fois la densité de population.

    La lecture n'kwargs='est ici pas simple.
    Le 11ème arrondissement est celui le plus densément peuplé de Paris et il occupe aussi la 3ème position des arrondissements avec la médiane du comptage horaire de vélos la plus élevée. 
    Il semblerait logique, pour cet arrondissement, de voir dans la densité de population un facteur d''influence sur le trafic vélo.
    Inversement, le 7ème arrondissement est l''un des moins densément peuplés et  on y trouve un site de comptage avec des pics de trafic vélo (max = 1429). et c''est celui du Quai d''Orsay, sens E-O (vers le centre de Paris). Pour cet arrondissement,  on ne peut donc pas établir de lien entre la densité de la population et le trafic vélo.

    __Analyse en fonction de la présence d’entreprises__

    L'INSEE définit les établissements actifs comme des établissements ayant employé au moins un salarié pendant l’année (source).
    Le trafic vélo peut-il être en lien avec la présence d’établissements employeurs ?

    On peut apprécier sur cette carte que le 8ème arrondissement est celui avec le plus d'établissements actifs. En revanche, aucun compteur du top 10 ne s'y trouve. Il est cependant  proche d’un arrondissement avec un site de comptage aux médianes élevées: Quai d'Orsay, notamment en direction E-O.
    Les arrondissements 1 et 2, les deux avec un nombre relativement important d'établissements actifs sont proches de 3 des compteurs avec les médianes horaires les plus élevées.
    Cette visualisation nous démontre que l’analyse par arrondissement a ses limites : en effet des distances faibles ici ne nous permettent pas de lier les données.

    Poussons malgré tout l’analyse sur la part des activités de Commerce et Réparation automobile :

    Parmi les établissements actifs, les commerces et ceux de réparation automobile se trouvent notamment dans le centre et le nord-ouest de Paris. On peut voir sur la carte que, fréquemment, les sites de comptage avec des médianes élevées se trouvent aussi dans des zones à haute concentration des commerces et des établissements de réparation automobile.
    On peut penser qu'il y a une influence entre le nombre de commerces ainsi que d'établissements de réparation automobile et le trafic vélo dans Paris.""")
                


   
    for axe in axes:
            with st.expander(axe, expanded=False):
                st.write(f"""Analyse pour {axe}...
                         
    d. Stationnements vélo disponibles et trafic cycliste

    Le site Open Data Paris propose les données de toutes les places de stationnement présentes à Paris, y compris autocars, voitures ou trottinettes :

    Dans le cadre de notre étude, nous allons filtrer ce jeu de données sur les typologies liées au vélo comme suit :

    Il apparaît que les lieux et les places de vélos et vélib sont majoritaires par rapport aux box et aux emplacements vélos-cargos : 

    Le type de mobilier est peu varié : 

    Au total, Paris compte plus de 150 000 places pour presque 15 000 lieux.

    Si l’on regarde le nombre de places par arrondissement, une disparité apparaît : 

    Les 21 et 22 arrondissements sont en fait les bois de Boulogne et de Vincennes qui auront un traitement particulier ultérieurement.

    Il existe de nombreux lieux de stationnement, parfois très proches. Ainsi si l’on considère la rue de l’Abbé Groult dans le 15eme arrondissement, on compte 26 lieux pour 132 places :

    De même, la rue Perrée dans le 3eme arrondissement compte 190 places pour 11 lieux parfois très proches.

    L’offre de stationnement de vélos est donc relativement dense.
    Nous allons le visualiser sur des cartes de Paris.

    Ces 2 cartes confirment que Paris est plutôt bien équipée en termes de stationnement vélo. Seuls les bois de Vincennes et Boulogne en sont peu pourvus.

    Tentons à présent de déterminer si l’offre de stationnement est adaptée aux usages de  la ville et à sa population en représentant sur une même carte zones touristiques internationales, zones piétonnes et zones de rencontre.

    Les lieux de stationnement vélos ne sont pas uniquement présents aux endroits représentant des points d'intérêt touristique, ou zones piétonnes ou zones de rencontre. Ils sont beaucoup plus développés et présents sur la globalité du territoire parisien.

    Les arrondissements de Paris ont des surfaces hétérogènes. Aussi est-il plus judicieux d’étudier un ratio de places selon la surface de l’arrondissement considéré.

    De plus, les bois de Boulogne et de Vincennes peuvent biaiser ces ratios. Aussi ne prenons nous pas en compte la surface des bois dans cette analyse.

    La surface d'un arrondissement ne semble pas être un critère pour l'installation des places de stationnement vélo, on peut apprécier sur le graphique que les arrondissements du 2 à 6 sont ceux avec le plus grand nombre de places de stationnement vélo. D'un autre côté, les arrondissements 12 et 16 (les plus grands de Paris) semblent avoir le moins de places vélo dans Paris.
    On a vu précédemment, que le centre de Paris est la zone avec le trafic vélo le plus important de la ville, mais c'est aussi une zone touristique, avec un nombre très important d'établissements actifs du type commerce, services divers, etc. 

    De même pour une analyse en fonction de la population par arrondissement, nous allons considérer un ratio pour 1 000  habitants.

    Sous cet angle d’analyse, les 10 premiers arrondissements sont clairement mieux lotis que les autres avec proportionnellement à leur population plus de places. 

    Ces différentes représentations démontrent que __le nombre d'habitants n’est pas un critère clé pour la promotion du trafic vélo dans Paris.__""")
                
  
  
  
    for axe in axes:
            with st.expander(axe, expanded=False):
                st.write(f"""Analyse pour {axe}...
           
         
       
    e. Infrastructure des pistes cyclables

    Les pistes cyclables à Paris peuvent être de différentes natures : 

    Le type de piste le plus présent à Paris est le "double-sens cyclable simple", avec plus de 400k mètres de longueur. 
    On entend par ce type d'aménagement :
    des voies à sens unique pour les véhicules motorisés (présence de sens interdits), autorisation pour les cyclistes de rouler dans les 2 sens, sans voie réservée.
    Les pistes cyclables suivent. Les pistes cyclables sont définies ainsi :
    Voie réservée aux cyclistes, séparée physiquement du reste de la circulation générale
    On pourrait conclure que dans Paris on compte avec des pistes cyclables protégées de la circulation motorisée, mais ce n'est pas le type d'aménagement le plus présent. Pour approfondir dans notre analyse, on va s'intéresser aux aménagements par arrondissements.(Source : Mairie de Paris)

    Pour l’analyse, nous allons nous concentrer sur les pistes purement dédiées au vélo, c’est à dire : 'bande cyclable', 'double-sens cyclable simple', et 'piste cyclable'.

    Le 12ème arrondissement est celui avec le plus de pistes cyclables dans Paris, avec près de 100.000 mètres de pistes. A l'autre extrême, on trouve que les arrondissements du centre de Paris sont ceux avec le moins de pistes cyclables.
    Ces chiffres semblent logiques, puisque le 12ème arrondissement est le deuxième plus grand de Paris (en termes de surface) alors que les arrondissements de 1 à 4 sont les plus petits.

    De même que pour les places de stationnement, nous préférons analyser des ratios plus explicites.

    En enlevant le biais lié à la surface des bois de Boulogne et Vincennes, les arrondissements périphériques semblent moins avantagés en pistes pures. 

    Nous pouvons conclure sur cet axe d’analyse que Paris dispose d’un réseau cyclable assez développé, mais que les pistes protégées restent minoritaires.
    Ces aménagements réservés sont inégalement répartis entre les arrondissements, ce qui peut influencer l’usage du vélo en fonction de la zone.""")
    



    for axe in axes:
            with st.expander(axe, expanded=False):
                st.write(f"""Analyse pour {axe}...
   
                 
    f. Localisation des bornes vélib
            
    A partir de données de Paris Data, nous récupérons les stations vélib au format “json”

    L’affichage de toutes les stations ne permet pas une lecture confortable des informations. Elle souligne cependant un nombre important de stations Vélib présentes dans Paris.

    Nous testons donc d’autres modalités de carte avec clustering automatique et sélection d’affichage.

    Nous étudions ces clusters Vélib avec la population de la ville de Paris. Cet affichage nous semble  pertinent et graphiquement parlant pour affirmer que le nombre de stations Vélib n’a pas de lien avec la population d’un arrondissement.7

    On observe effectivement que les arrondissements du cœur de Paris disposent de plus de stations Vélib que ceux de la périphérie plus peuplés (hormis le 15ème arrondissement).

    Afin de mieux visualiser cet aspect nous calculons le nombre de station pour 1 000 habitants : 

    Il apparaît que le 1er et le 8eme arrondissements comptent proportionnellement à leur population, plus de stations Vélib. 

    De même, si l’on considère le nombre de stations par rapport à la surface de l’arrondissement, des disparités émergent : 


    Cela signifie que le positionnement des stations Vélib n’est pas conditionné par la population ou la surface de l’arrondissement.

    Par ailleurs, si on regarde la capacité des stations Vélib parisiennes par rapport à la population et à la surface de l’arrondissement : 


    De très fortes disparités existent.

    Cela s’explique tout simplement car population et surface ne sont pas les critères d’installation et dimensionnement des stations Vélib.


    Positionnons maintenant sur la même carte les grands pôles d’échanges internationaux sur la carte (Gare du Nord, Châtelet, Gare de Lyon…).

    Nous notons une très forte quantité de stations Vélib autour de Gare du Nord / Magenta notamment. Cela est moins clair pour les autres points mais cette carte nous invite à émettre l’hypothèse d’un lien entre station Vélib et Gares.""")




    for axe in axes:
            with st.expander(axe, expanded=False):
                st.write(f"""Analyse pour {axe}...

    g. Zones / sites touristiques
    
    Les sites open data de la Région Ile-de-France, d’Ile-de-France Mobilité et de la Mairie de Paris nous permettent assez facilement de construire une carte composée des principaux sites touristiques de la ville, des zones touristiques internationales et des lieux d’échange international des transports. 
    Nous ajoutons sur cette carte les sites de comptage vélo de notre jeu de données initial/

    Nous cherchons à analyser s’il existe un lien entre la distance-gare et le comptage vélo d’une part ainsi qu’entre la distance-site touristique et le comptage vélo.
    Grâce à geodesic de geopy.distance, nous mesurons des distances minimales aux gares et aux sites touristiques.

    Résultats obtenus : 

    Corrélation distance-gare / nombre de vélos : -0.39254065291336526
    Corrélation distance-site touristique / nombre de vélos : -0.15361509498018922

    🔢 Interprétation des coefficients : 
    Coefficient distance_gare : -428.63 Cela signifie qu'à chaque mètre supplémentaire de distance par rapport à une gare, le nombre de vélos comptés diminue de 428,63 vélos (en moyenne, sur l'ensemble des sites de comptage). C'est une grande diminution, mais cette relation est modérée par la faible corrélation observée précédemment. Ce coefficient indique qu'il existe une influence, mais peut-être que d'autres facteurs sont aussi impliqués dans les variations du comptage.
    Coefficient distance_site_touristique : -28.52 Ici, chaque mètre supplémentaire de distance par rapport à un site touristique est associé à une diminution de 28,52 vélos comptés en moyenne. Ce coefficient est plus faible que celui des gares, ce qui confirme la faible corrélation trouvée précédemment. Les sites touristiques semblent avoir moins d'impact sur les vélos comptés par rapport aux gares.

    ⚖️ Conclusions : Les gares semblent avoir une influence plus marquée sur le nombre de vélos comptés, mais avec un impact qui peut être modéré par d'autres facteurs. Les sites touristiques ont une influence beaucoup plus faible, comme suggéré par la faible corrélation et le faible coefficient.
    
    """)

    
 

def clustering():
    st.header("3. Tentative de clustering des données")
    
    algorithms = [
        "a. Algorithme des K-Means",
        "b. Algorithme DBSCAN",
        "d. Algorithme HDBSCAN",
        "e. Conclusions du Machine Learning"
    ]
    
    for algo in algorithms:
        st.subheader(algo)
        st.write(f"Résultats pour {algo}...")
        # Ajoutez ici les résultats et visualisations de chaque algorithme

def conclusions():
    st.header("4. Conclusions")
    
    st.subheader("Bilan du projet")
    st.write("Résumé du bilan...")
    
    st.subheader("Améliorations possibles et perspectives")
    st.write("Suggestions d'améliorations...")
    
    st.subheader("Dynamique de l'équipe projet")
    st.write("Réflexions sur la dynamique d'équipe...")
    
    st.subheader("Synthèse et recommandations pour la Mairie de Paris")
    st.write("Synthèse finale et recommandations...")

if __name__ == "__main__":
    main()
