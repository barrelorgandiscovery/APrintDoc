Description de la gestion des instruments et des gammes
-------------------------------------------------------

### Introduction

Le logiciel gère les instruments et les gammes avec un concept d'entrepôt (ou repository en anglais). Cet entrepôt peut être stocké sous la forme d'un répertoire ou d'un espace sur le web (pour permettre un échange facile avec les autres utilisateurs). Le logiciel gère alors les instruments ou les gammes sauvegardées comme le définit l'entrepôt.

Plusieurs types d'entrepôts sont disponibles actuellement

-   Un entrepôt "buildin" c'est un entrepôt existant en mémoire du logiciel, celui ci ne peut pas être mis à jour
-   Un entrepôt de type "zip", qui permet de mettre dans un fichier compressé un ensemble de fichier de gamme ou d'instruments
-   Un entrepôt de type "folder" ou répertoire (dossier), qui enregistre les différents éléments sous forme de fichier dans un dossier
-   Un entrepôt de type "web" qui est sous forme de dossier ou répertoire et qui permet une interaction avec un espace partagé sur internet. Ceci permet de récupérer des instruments ou des gammes mis à disposition par les autres utilisateurs.

### Description des différents éléments stockés

Le programme enregistre dans l'entrepôt deux types d'informations, les gammes et les instruments.

Les instruments peuvent avoir plusieurs formes (ceci est liée à la compatibilité avec les anciennes versions du logiciel).

#### Les gammes

Le fichier de gamme est un fichier textuel décrivant les informations qui peuvent être communes à plusieurs instruments. (capacité de note, contraintes, type de lecture de l'instrument ...) des informations associées comme l'auteur, l'état de la gamme peuvent également être enregistrées.

#### Les instruments

Les instruments peuvent être décrits de deux façons :

-   plusieurs fichiers liés (un fichier de gamme, un fichier de description d'instrument, un fichier de banque de sons et un fichier d'images)
-   un seul fichier ".instrumentbundle" contenant tous ces éléments.

Le fichier .instrumentbundle est celui qui est actuellement utilisé en référence dans le logiciel. En effet, celui ci regroupe tous les éléments de description de l'instrument et indépendemment du logiciel.

Ce même fichier est un fichier zip, contenant des fichiers textes, images au format jpg, et sons associés au format WAV.
