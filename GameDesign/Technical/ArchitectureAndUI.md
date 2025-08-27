# 5. Architecture Technique et Interface Utilisateur (UI)

Le jeu utilise une vue isométrique en 2D avec une caméra fixe. L'interface utilisateur est simple et intuitive, avec les informations principales du camp affichées en haut de l'écran et les boutons de menu principaux en bas. Les menus des bâtiments et des personnages sont accessibles de manière contextuelle en cliquant directement sur l'entité, ou via un menu général.

Les contrôles de la caméra sont adaptés au tactile. Le zoom s'effectue en ajustant la propriété orthographicSize de la caméra. Le joueur peut dézoomer pour voir les opportunités à proximité, ou dézoomer encore plus pour voir la carte du secteur ou de la région . Le dézoom se fait via un mouvement de scroll de la souris ou de pincement des doigts . Le déplacement de l'île n'est pas instantané. Un bouton permet de recentrer la vue sur le personnage principal.
