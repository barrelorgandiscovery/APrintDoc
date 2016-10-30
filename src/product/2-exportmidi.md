
Réaliser des exports MIDI pour les instruments automatisés
==========================================================



APrint Studio permet l'export des fichiers de carton, en fichiers MIDI adaptés à l'utilisation par des outils automatiques. Que ce puisse être des perforatrices ou des instruments MIDIfiés.

Il est frequent que les fichiers MIDI issus de l'arrangement ne correspondent pas aux attentes en termes opérationnels.

Un bouton d'export MIDI dans la vue carton permet d'exporter le carton en fichier MIDI. ce bouton effectue les opérations suivantes :

-   Export au format MIDI 0, les pistes sont fusionnées pour n'avoir plus qu'un seul Track. ce format est beaucoup plus facile à lire pour les cartes spécialisées
-   Fusion des trous ou des notes supperposées
-   Homogénéisation du tempo: en effet un seul tempo est utilisé en début de fichier MIDI. Les autres tempo sont alors enlevés pour éliminer leur interprétation par un lecteur de carte MIDI.

Cette fonction est également très utilisées pour les perforatrices automatiques prenant en entrée des fichiers MIDI.
