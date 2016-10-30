Elements Techniques sur la prise en compte des instruments virtuels
===================================================================

Comment cela fonctionne il dans le logiciel ?
---------------------------------------------

Le logiciel APrint Studio / APrint permet de faire un rendu sonore pour chaque note d'un carton et ceci conditionné par les registres utilisés dans le carton.

Les notes sont donc enregistrées dans un fichier .WAV. et traitées en interne dans un format 16bits / 44khz. Les échantillons de qualité supérieure ou inférieure sont nivellées aux caractéristiques précédente.

Les échantillons peuvent être :

-   attachés à une note précise indépendemment d'un section de basse , accompagnement ou chant (c'est à dire qu'il sont toujours joués sur la note donnée)
-   attachés à une section de registre (basse, accompagnement), indépendamment d'un registre, c'est parfois le cas lorsqu'un jeu est toujours déclenché sur la note
-   attachés à un registre particulier, en effet l'echantillon n'est joué que si le registre est activé.

un échantillon même s'il est enregistré sur une note précise, peut être associé à plusieures notes adjacentes, ceci permet de ne pas multiplier les enregistrements de notes si les échantillons sont très similaires.

Le sequenceur étant logiciel, la limite en nombre d'échantillons est la mémoire de l'ordinateur et sa puissance. Le format utilisé pour les banques de sons est SoundFont (SF2), mais est uniquement utilisé en interne ou reconstruit à la volée à partir de l'éditeur d'instruments.

Depuis la version 2012, le logiciel dépasse la capacité MIDI de 16 canaux, il est maintenant possible d'avoir jusqu'à 63 registres pilotés pour un instrument.

Le fichier .instrumentbundle
----------------------------

Le fichier instrumentbundle resultant de la définition d'un instrument est en réalité un fichier zip contenant les fichiers wav, la définition de la gamme et les propriétés de l'instrument.

Le fichier .soundsample
-----------------------

Le type de fichier soundsample est un fichier permettant de simplifier la réutilisation d'échantillon (.wav) sur lesquels les propriétés d'échantillons sont enregistrés. On a donc dans ce fichier : la note associée à l'enregistrement, les propriétés de bouclage de l'échantillon (dans le cas où l'échantillon n'est pas assez grand et qu'il faut reprendre une partie de l'echantillon pour avoir des notes longues).

Ce type de fichier permet entre autre de pouvoir constituer des banques de sons de tuyaux pouvant être réutilisés d'un instrument à un autre. Par exemple, la redéfinition de l'ensemble d'instrument d'un même facteur , qui a réutiliser la même construction pour les tuyaux (le rendu est donc similaire).

La relation avec le midi en interne
-----------------------------------

Dans le fonctionnement interne, plusieurs "instruments midi" sont définis dans la banque de son interne, pour chaque section de registre (basse, accompagnement, chant , ..) et chaque registre, une banque est créé. Ces instruments sont par la suite mappés sur un canal midi sur lequel un "program change" spécifie l'instrument interne utilisé.

Dans le jeu d'un carton virtuel, et en fonction de la registration, les notes sont envoyées sur les canaux associés.
