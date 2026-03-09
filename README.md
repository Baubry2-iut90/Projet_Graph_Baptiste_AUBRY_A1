# Projet_Graph_Baptiste_AUBRY_A1
projet de graph sur les villes de france pour pouvoir connaître les distance (environ) d'un trajet entre 2 villes de France


Analyse et Optimisation du Réseau Routier Français

Ce projet Python utilise la théorie des graphes pour modéliser, analyser et optimiser un réseau de transport reliant les principales villes de France. L'application permet de calculer des itinéraires optimaux tout en analysant la structure et la robustesse du réseau.


Fonctionnalités principales

  Calcul d'itinéraire : Détermination du plus court chemin entre deux villes (algorithme de Dijkstra).

  Optimisation de réseau : Calcul de l'arbre couvrant minimum pour relier toutes les villes au moindre coût.

  Analyse de robustesse : Identification des points d'articulation (villes critiques pour la connectivité).

  Coloration de graphe : Attribution de couleurs aux sommets pour illustrer la séparation des zones adjacentes.

  Visualisation dynamique : Affichage du réseau sur une carte géographique avec superposition des résultats.


Concepts du cours appliqués

Ce projet met en pratique plusieurs notions fondamentales abordées dans le cours :

  Modélisation (Graphe Pondéré) : Le réseau est représenté par un graphe non orienté G=(V,E) où chaque arête possède un poids correspondant à la distance kilométrique réelle (notion de graphe pondéré, p. 3).

  Arbre Couvrant Minimum (Page 165) : Utilisation de la fonction nx.minimum_spanning_tree. Ce concept permet de trouver le sous-graphe qui relie tous les sommets avec le poids total minimal, sans créer de cycles.

  Coloration de Graphe (Pages 169-170) : Implémentation d'un algorithme de coloration pour déterminer le nombre chromatique pratique. Le but est d'affecter une couleur à chaque ville de sorte que deux villes reliées n'aient jamais la même couleur.

  Connectivité et Excentricité :

  Diamètre : La plus longue des "plus courtes distances" entre deux villes du réseau.

  Centre : Identification de la ville ayant l'excentricité minimale (la ville la mieux située pour desservir l'ensemble du territoire).

  Points d'articulation : Identification des nœuds critiques. Si l'une de ces villes est retirée, le réseau se divise en plusieurs parties isolées (perte de la connexité).


Aperçu du résultat :
<img width="1198" height="1048" alt="aperçu_projet_graph" src="https://github.com/user-attachments/assets/6f5cce2f-9cbf-4a44-bbbb-4608bf77ad73" />
<img width="1076" height="330" alt="aperçu_console_projet_graph" src="https://github.com/user-attachments/assets/709e88fc-8e66-4ef9-9ba8-bd20f6b836bb" />


