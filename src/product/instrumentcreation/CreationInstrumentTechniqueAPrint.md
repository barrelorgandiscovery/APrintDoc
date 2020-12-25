# Eléments techniques sur la prise en compte des instruments virtuels

__ Patrice Freydiere 2020 __

APrint Studio dispose d'un ensemble d'outil permettant de définir ou d'ajuster des définitions d'instruments. Dans ces outils, on retrouve : l'éditeur de gamme, permettant de définir une gamme, avec sa géométrie , l'éditeur d'instrument, permettant d'assembler l'ensemble des éléments constituants d'un instrument, c'est à dire : gamme, définition des sons, définition des contraintes (longueur de trous minimum, .. etc)

Depuis les années 2010, l'ensemble de ces outils intégrés dans l'éditeur d'instrument, regrouppant ces fonctionnalités, comme des outils intégrés et complémentaires permettant la gestion des sons, découpage de sons enregistrés.


## Caractéristiques de définition des instruments

APrint Studio, permet d'intégrer les types d'instruments suivants :

- Orgues de rue
- Orgues de foire
- Orgues de danse
- Boites à musique
- Disques de carton ariston
- Piano mécaniques

Les gammes d'instruments sont définies par une grille régulière définissant l'emplacement des pistes de lecture pneumatique ou mécanique, à partir d'un coté de référence (pour la fabrication, ou visualisation)

Certaines gammes "non régulières" peuvent également être décrites, cependant pour la partie "reconnaissance" et "perforation", des scripts ou des particularités doivent être ajoutées par script.

Chose unique dans le logiciel, est la prise en charge de la définition des registres. Les registres peuvent être définis et utilisés. On retrouve donc :
- la définition des jeux de registres (BASSES, ACCOMPAGNEMENT, CHANT1, CHANT3, CONTRE CHANT)
- la définition des registres associés à ces jeux, ainsi que la commande des sons sur ces registres (activation de certains registres dans certains jeux)

Toutes ces informations sont enregistrées dans un fichier .instrumentbundle, qui est en fait un zip (il est possible de renommer le fichier en zip et d'accéder à ces informations). L'utilisation de ces informations ne nécessitent pas de logiciels specifiques, car enregistré sous forme de "texte", ou "fichier Wav", elles peuvent être réutiliées par ailleurs.


# Prise en charge des sons reels de l'instrument

Le logiciel APrint Studio / APrint permet de faire un rendu sonore pour chaque note d'un carton et ceci conditionné par les registres utilisés dans le carton.

Les notes sont donc enregistrées dans un fichier .WAV. et traitées en interne dans un format 16bits / 44khz. Les échantillons de qualité supérieure ou inférieure sont nivellées aux caractéristiques précédentes.

Les échantillons peuvent être :

-   attachés à une note précise indépendemment d'une section de basse, accompagnement ou chant (c'est à dire qu'il sont toujours joués sur la note donnée)
-   attachés à une section de registre (basse, accompagnement), indépendamment d'un registre, c'est parfois le cas lorsqu'un jeu est toujours déclenché sur la note
-   attachés à un registre particulier, en effet l'échantillon n'est joué que si le registre est activé.

Un échantillon même s'il est enregistré sur une note précise, peut être associé à plusieurs notes adjacentes, ceci permet de ne pas multiplier les enregistrements de notes si les échantillons sont très similaires.

Le séquenceur étant logiciel, la limite en nombre d'échantillons est la mémoire de l'ordinateur et sa puissance. Le format utilisé pour les banques de sons est SoundFont (SF2) mais est uniquement utilisé en interne ou reconstruit à la volée à partir de l'éditeur d'instruments.

Depuis la version 2012, le logiciel dépasse la capacité MIDI de 16 canaux. Il est maintenant possible d'avoir jusqu'à 63 registres pilotés pour un instrument.

# Lien avec la norme midi

Dans le logiciel, ces informations d'instrument, sont "compilée" en norme midi, via l'utilisation de bank de sons. Comme la définition des banks de son sont multiples et variées, le fait de reposer sur une description de l'instrument plus proche de la réalité, permet alors de pouvoir générer les conversions dans les différents formats demandés.

Dans l'implémentation de référence, le format SoundFont est utilisé, et plusieurs "instruments midi" sont définis, pour chaque section de registre (basse, accompagnement, chant , ..). Ces instruments sont par la suite mappés sur un canal midi sur lequel un "program change" spécifie l'instrument interne utilisé.

Dans le jeu d'un carton virtuel et en fonction de la registration, les notes sont envoyées sur les canaux associés.

