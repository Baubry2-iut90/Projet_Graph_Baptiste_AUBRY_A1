import networkx as nx
import matplotlib.pyplot as plt
import csv

# Chargement des coordonnées depuis 'villes.csv'
coords = {}
try:
    with open('villes.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            nom = row['city'].strip()
            latitude = float(row['lat'])
            longitude = float(row['lng'])
            coords[nom] = (longitude, latitude)
except FileNotFoundError:
    print("Erreur : Fichier 'villes.csv' introuvable. Assurez-vous qu'il est dans le même dossier.")
    exit()

G = nx.Graph()

# Ajout des routes avec distances (Pondération)
edges = [
    # Île-de-France & Nord
    ("Paris", "Lille", 225), ("Paris", "Rouen", 135), ("Paris", "Reims", 145),
    ("Paris", "Orléans", 130), ("Paris", "Nancy", 380), ("Paris", "Rennes", 350),
    ("Paris", "Dijon", 315), ("Paris", "Le Mans", 210), ("Paris", "Troyes", 180),
    ("Paris", "Amiens", 120), ("Paris", "Chartres", 90),
    ("Lille", "Amiens", 140), ("Lille", "Reims", 200), ("Lille", "Calais", 110),
    ("Lille", "Dunkerque", 80), ("Calais", "Dunkerque", 40), ("Calais", "Boulogne-sur-Mer", 35),
    ("Amiens", "Rouen", 120), ("Amiens", "Saint-Quentin", 80), ("Saint-Quentin", "Reims", 95),
    ("Beauvais", "Paris", 80), ("Beauvais", "Amiens", 65), ("Beauvais", "Rouen", 80),

    # Grand Est
    ("Reims", "Metz", 190), ("Reims", "Troyes", 125), ("Reims", "Charleville-Mézières", 85),
    ("Metz", "Nancy", 60), ("Metz", "Strasbourg", 160), ("Nancy", "Strasbourg", 150),
    ("Strasbourg", "Mulhouse", 115), ("Mulhouse", "Belfort", 45), ("Belfort", "Besançon", 90),
    ("Nancy", "Épinal", 70), ("Épinal", "Belfort", 80), ("Épinal", "Mulhouse", 100),
    ("Besançon", "Dijon", 90), ("Strasbourg", "Dijon", 310), ("Nancy", "Dijon", 200),
    ("Troyes", "Dijon", 190), ("Troyes", "Nancy", 180),

    # Bourgogne-Franche-Comté & Auvergne-Rhône-Alpes
    ("Dijon", "Lyon", 195), ("Dijon", "Chalon-sur-Saône", 70), ("Chalon-sur-Saône", "Lyon", 130),
    ("Lyon", "Grenoble", 110), ("Lyon", "Saint-Étienne", 60), ("Lyon", "Valence", 105),
    ("Lyon", "Annecy", 145), ("Lyon", "Bourg-en-Bresse", 80),
    ("Bourg-en-Bresse", "Annemasse", 90), ("Annemasse", "Annecy", 45),
    ("Grenoble", "Chambéry", 60), ("Chambéry", "Annecy", 50), ("Grenoble", "Valence", 95),
    ("Saint-Étienne", "Clermont-Ferrand", 145), ("Saint-Étienne", "Valence", 125),
    ("Clermont-Ferrand", "Lyon", 165), ("Clermont-Ferrand", "Montluçon", 110),
    ("Montluçon", "Châteauroux", 100),
    ("Nevers", "Montargis", 110), ("Montargis", "Paris", 110),
    ("Clermont-Ferrand", "Nevers", 160),

    # PACA & Occitanie Est
    ("Lyon", "Marseille", 315), ("Valence", "Nîmes", 145),
    ("Nîmes", "Montpellier", 55), ("Nîmes", "Marseille", 125),
    ("Marseille", "Toulon", 65), ("Toulon", "Nice", 150), ("Marseille", "Nice", 200),
    ("Nice", "Cannes", 35), ("Cannes", "Toulon", 120),
    ("Marseille", "Montpellier", 170), ("Montpellier", "Perpignan", 155),
    ("Montpellier", "Toulouse", 240), ("Perpignan", "Toulouse", 205),

    # Occitanie Ouest & Nouvelle-Aquitaine
    ("Toulouse", "Bordeaux", 245), ("Toulouse", "Pau", 195), ("Toulouse", "Agen", 115),
    ("Agen", "Bordeaux", 140), ("Pau", "Bayonne", 115), ("Bayonne", "Bordeaux", 185),
    ("Toulouse", "Bayonne", 300), ("Toulouse", "Limoges", 290),
    ("Bordeaux", "Limoges", 220), ("Bordeaux", "Angoulême", 120), ("Angoulême", "Poitiers", 110),
    ("Poitiers", "Tours", 105), ("Poitiers", "Limoges", 120),
    ("Limoges", "Clermont-Ferrand", 175), ("Limoges", "Châteauroux", 125),
    ("Châteauroux", "Orléans", 130), ("Châteauroux", "Tours", 115),

    # Ouest & Normandie
    ("Bordeaux", "La Rochelle", 190), ("La Rochelle", "Nantes", 140), ("La Rochelle", "Poitiers", 140),
    ("Bordeaux", "Nantes", 350), ("Nantes", "Rennes", 110), ("Nantes", "Angers", 90),
    ("Nantes", "Saint-Nazaire", 65), ("Saint-Nazaire", "Vannes", 115), ("Vannes", "Lorient", 60),
    ("Lorient", "Brest", 135), ("Brest", "Saint-Brieuc", 145), ("Saint-Brieuc", "Rennes", 100),
    ("Rennes", "Brest", 240), ("Rennes", "Le Mans", 160), ("Rennes", "Caen", 185),
    ("Angers", "Le Mans", 95), ("Angers", "Tours", 130), ("Le Mans", "Tours", 100),
    ("Tours", "Orléans", 115), ("Orléans", "Chartres", 75),
    ("Caen", "Rouen", 130), ("Caen", "Le Havre", 95), ("Le Havre", "Rouen", 90),
    ("Rouen", "Évreux", 55), ("Évreux", "Paris", 100), ("Caen", "Alençon", 105), ("Alençon", "Le Mans", 55)
]
G.add_weighted_edges_from(edges)

# ANALYSE AVANCÉE (NOTIONS DU COURS) :
print("\n--- Analyse du Réseau Routier ---")

if nx.is_connected(G):
    longueurs = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))
    excentricites = nx.eccentricity(G, sp=longueurs)
    
    print(f"1. Le réseau est connexe.")
    print(f"2. Diamètre (trajet le plus long) : {nx.diameter(G, e=excentricites)} km")
    print(f"3. Centre du réseau (Ville centrale) : {nx.center(G, e=excentricites)}")

    T = nx.minimum_spanning_tree(G, weight='weight')
    print(f"4. Réseau minimum (Kruskal) : {T.size(weight='weight'):.1f} km pour relier toutes les villes.")

    articulations = list(nx.articulation_points(G))
    print(f"5. Villes stratégiques (points d'articulation) : {articulations}")
else:
    print("Le réseau n'est pas entièrement connecté.")

# Attribue une couleur à chaque nœud pour que deux voisins n'aient pas la même
color_map_dict = nx.coloring.greedy_color(G, strategy="largest_first")
node_colors = [color_map_dict[node] for node in G.nodes()]

# Villes disponibles :
print("\n--- Villes disponibles ---")
print(", ".join(sorted(G.nodes())))
print("--------------------------\n")

# INTERACTION UTILISATEUR :
print("\n--- Calcul d'Itinéraire ---")
def saisir_ville(message):
    while True:
        ville = input(message).strip()
        if ville in G: return ville
        print(f"La ville '{ville}' n'est pas dans la base. Réessayez.")

depart = saisir_ville("Ville de départ : ")
arrivee = saisir_ville("Ville d'arrivée : ")

chemin = nx.shortest_path(G, source=depart, target=arrivee, weight='weight')
dist_totale = nx.shortest_path_length(G, source=depart, target=arrivee, weight='weight')

# VISUALISATION :
fig, ax = plt.subplots(figsize=(12, 10))

# Image de fond (carte de France)
try:
    img = plt.imread("carte_france.png")
    ax.imshow(img, extent=[-5.05, 8.2, 42.1, 51.2], alpha=0.6, aspect='auto')
except:
    print("Note : Image 'carte_france.png' non trouvée, affichage sur fond blanc.")

pos_graphe = {n: coords[n] for n in G.nodes() if n in coords}
edges_visu = [(u, v) for u, v in G.edges() if u in pos_graphe and v in pos_graphe]

# Dessin des routes de fond
nx.draw_networkx_edges(G, pos=pos_graphe, ax=ax, edgelist=edges_visu, edge_color='#bdc3c7', width=1, alpha=0.5)

# Dessin de l'Arbre Couvrant (en bleu pointillé)
edges_tree = [(u, v) for u, v in T.edges() if u in pos_graphe and v in pos_graphe]
nx.draw_networkx_edges(T, pos=pos_graphe, ax=ax, edgelist=edges_tree, edge_color='#3498db', width=1.5, style='--')

# Dessin des nœuds avec les couleurs de la "Coloration"
nx.draw_networkx_nodes(G, pos=pos_graphe, ax=ax, node_size=50, node_color=node_colors, cmap=plt.cm.Set3)

# Mise en évidence du chemin choisi (Rouge)
path_edges = list(zip(chemin, chemin[1:]))
nx.draw_networkx_edges(G, pos=pos_graphe, ax=ax, edgelist=path_edges, edge_color='#e74c3c', width=4)

# Labels
label_pos = {k: (v[0], v[1] + 0.1) for k, v in pos_graphe.items()}
nx.draw_networkx_labels(G, pos=label_pos, ax=ax, font_size=7)

ax.set_title(f"Réseau Routier : {depart} → {arrivee} ({dist_totale} km)\nPointillés bleus = Arbre Couvrant Minimum", fontsize=12, fontweight='bold')
ax.axis('off')


plt.tight_layout()
plt.show()
