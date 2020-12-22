# Utilisation de l'éditeur d'instruments


# Fonctionnement du logiciel et fichiers utilisés


### Le fichier .instrumentbundle

Le fichier instrumentbundle résultant de la définition d'un instrument est en réalité un fichier zip contenant les fichiers wav, la définition de la gamme et les propriétés de l'instrument.

### Le fichier .soundsample

Le type de fichier soundsample est un fichier permettant de simplifier la réutilisation d'échantillons (.wav) sur lesquels les propriétés d'échantillons sont enregistrés. On a donc dans ce fichier : la note associée à l'enregistrement, les propriétés de bouclage de l'échantillon (dans le cas où l'échantillon n'est pas assez grand et qu'il faut reprendre une partie de l'échantillon pour avoir des notes longues).

Ce type de fichier permet entre autres de pouvoir constituer des banques de sons de tuyaux pouvant être réutilisés d'un instrument à un autre. Par exemple, la redéfinition de l'ensemble d'instruments d'un même facteur, qui a réutilisé la même construction pour les tuyaux (le rendu est donc similaire).


