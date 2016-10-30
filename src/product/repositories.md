Description de la gestion des instruments et des gammes
-------------------------------------------------------

### Introduction

Le logiciel gère les instruments et les gammes avec un concept d'entrepot (ou repository en anglais). Cet entrepot peut être stocké sous la forme d'un répertoire, ou d'un espace sur le web (pour permettre un échange facile avec les autres utilisateurs). Le logiciel gere alors les instruments ou les gammes sauvegardées comme le définit l'entrepot.

Plusieurs type d'entrepots sont disponibles actuellement

-   Un entrepot "buildin" c'est un entrepot existant en mémoire du logiciel, celui ci ne peut pas être mis à jour
-   Un entrepot de type "zip", qui permet de pouvoir mettre dans un fichier compressé un ensemble de fichier de gamme ou d'instrument
-   Un entrepot de type "folder" ou répertoire (dossier), qui enregistre les différents éléments sous forme de fichier dans un dossier
-   Un entrepot de type "web" qui est sous forme de dossier ou répertoire et qui permet une interaction avec un espace partagé sur internet. ceci permet de récuperer des instruments ou des gammes mis à disposition par les autres utilisateurs.

### Description des différents éléments stockés

Le programme enregistre dans l'entrepot deux types d'information, les gammes et les instruments.

Les instruments peuvent avoir plusieures formes (ceci est liée à la compatibilité avec les anciennes versions du logiciel).

#### Les gammes

Le fichier de gamme est un fichier textuel décrivant les informations qui peuvent être communes entre plusieurs instruments. (capacité de note, contraintes, type de lecture de l'instrument ...) des informations associées comme l'auteur, l'état de la gamme peuvent également être enregistrés.

#### Les instruments

Les instruments peuvent être décrits de deux façon :

-   plusieurs fichiers liés (un fichier de gamme, un fichier de description d'instrument, un fichier de banque de son et un fichier d'image)
-   un seul fichier ".instrumentbundle" contenant tous ces éléments.

Le fichier .instrumentbundle est celui qui est actuellement utilisé en référence dans le logiciel. en effet, celui ci regroupe tous les éléments de description de l'instrument et indépendemment du logiciel.

Ce même fichier est un fichier zip, contenant des fichiers textes, images au format jpg, et sons associés au format WAV.
