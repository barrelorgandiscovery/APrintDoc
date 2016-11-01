
Format de cartons virtuel ou fichiers ".book"
=============================================


Introduction, une utilisation du format midi pervertie
------------------------------------------------------

APrint studio introduit un nouveau format de fichier (fichier book), qui est un format de fichier Texte. Ce nouveau format de fichier permet d'enregistrer sans pertes et en conservant l'ensemble des informations associées à un carton de façon non ambiguë (comme la registration, la définition de l'instrument sur lequel a été créé le carton).

Cette introduction de nouveau format de fichier a été nécessaire pour simplifier l'échange et pouvoir garantir que quelqu'un envoyant un morceau de musique, d'autres personnes puissent l'écouter et retravailler dessus sans pertes d'informations.

En effet, depuis l'utilisation des fichiers midi dans le domaine de l'orgue de barbarie, leur utilisation / échange est rendu difficile pour plusieurs raisons :

-   Le format de fichier midi définit plusieurs façons de définir la registration (tracks différents, utilisation de canaux, commande de registre dans des sysevent spéciaux connus de certains matériels)
-   Des cartes midi ont été utilisées pour l'interfaçage avec un instrument, en détournant certaines notes pour piloter les registres, donc l'écoute d'un tel fichier midi de commande est "bizzare" dans un séquenceur classique, (par expérience, les notes midi peuvent également ne pas être respectées).
-   Les fichiers midi acceptent également l'introduction de notes ne pouvant être jouées par les instruments. Certains instruments ne sont pas chromatiques sur certains jeux.

Même si l'utilisation de fichier midi est extrêmement pratique sur les phases amont du carton, dans l'arrangement, la composition, on arrive à un point lors de la réalisation du carton où beaucoup de questions se posent sur l'implémentation ou la réalisation finale du carton sur l'instrument, en respectant les contraintes de celui ci (et il peut y en avoir beaucoup)

En conclusion, réutiliser un fichier midi pour un échange de musique ou de morceau de musique en format midi peut être simple pour les petits instruments, mais délicat si l'on n'a pas la définition du pilotage de l'instrument et même en ayant ces informations, il n'est pas garanti que ce que l'on écoute reflète ce qui sera correctement joué sur l'instrument.


Description du format de carton .book
-------------------------------------

Le format .book n'est ni plus ni moins que la transcription du carton de façon informatisée. Ce fichier contient les éléments suivants :

-   Un titre
-   Des métadonnées sur le carton
-   Une image associée au carton (pour la page de garde)
-   La définition des pistes du carton (percussion, notes, définition de la registration ...)
-   la liste des trous effectués dans le carton

Ces informations sont sauvegardée dans un fichier au format texte (XML), ce format a été préféré à un format propriétaire car il permet sans logiciel de pouvoir comprendre le contenu du fichier et permettre à des outils d'indexation ou des bibliothèques de développement disponibles sur tous les ordinateurs, de pouvoir l'exploiter.

Passons à la description plus précise du contenu du fichier

### Les métadonnées

Les informations de métadonnées permettent d'avoir des informations générales sur le fichier, pour pouvoir effectuer des recherches.

on retrouve donc le tronc commun :

-   L'auteur de la musique (**Author)**
-   L'arrangeur de la musique pour cet instrument (**Arranger)**
-   Une date de création du morceau (**CreationDate)**
-   Une date de dernière modification (**LastModificationDate)**
-   Un genre pour la musique (**Genre)**
-   L'instrument pour lequel le morceau a été composé (**DesignedInstrumentName)**

Le nom de l'instrument pour lequel la morceau a été composé ne définit pas la description des touches de l'instrument, la section suivante est faite pour cela.

### Définition de la gamme

La section gamme (**Scale)** définit le nombre, la composition et le rôle de chaque piste. La plupart des boites à touches ou mécanisme de lecture (flûte de pan) de la musique par l'instrument est réalisée par une grille régulière à partir d'un talon et avec une dimension en mm pour l'axe de première piste par rapport au talon, puis une dimension en mm d'entrepiste (dimension entre deux axes de pistes (pas)) et puis finalement le nombre de pistes dans le carton.

En fonction des instruments, le talon peut être situé vers l'avant ou l'arrière de l'instrument selon la façon dont la boîte à touches plaque le carton pour mettre la lecture en référence. Certains instruments centrent le carton, il suffit alors de spécifier arbitrairement une orientation de talon (avant ou arrière).

Vient ensuite la description de la signification des pistes. Dans le format book les pistes peuvent être :

-   Des notes (appartenant à un groupe de jeu (arrangement, chant, contre chant ... )
-   Des percussions
-   Des commandes de registres (les automates, jeux fortés, trémolo, jalousies rentrent dans cette catégorie)

Distinctement du carton, la gamme peut avoir un nom, auteur différent de l'instrument ou du carton, dans le cas où la gamme est un standard réutilisé dans plusieurs instruments différents.

La gamme contient également une information de vitesse de défilement du carton (en millimètre par seconde), ceci permet d'effectuer des conversions de "secondes" vers des millimètres.

On retrouve également une information de "type de lecture" , pneumatique / mécanique.

#### Définition d'une piste contenant des notes

La définition d'une piste ayant des notes propose les informations suivantes :

-   La note, utilisant la notation anglosaxone des notes (C, C\#, D,D\#, E, F,F\#, G, G\#, A, A\#, B) suivit de l'octave
-   Le groupe de jeux auquel appartient la note (Chant, basse, contrechant ..)

#### Définition d'une piste contenant des percussions

La définition d'une piste ayant des notes propose les informations suivantes :

-   Un code de percussion
-   des informations de décalage par rapport au jeu (en effet les percussions peuvent fonctionner en pression / dépression, et donc la fin du trou marque, sur certains instruments, le jeu de la percussion).

#### Définition d'une piste contenant des commandes de registration

La définition d'une piste de commande de registration peut avoir différents types :

-   Déclenchement (général ou pour un groupe de jeux)
-   Enclenchement d'un registre sur un groupe de jeux

Chaque définition a des informations sur un éventuel décalage par rapport à la prise en compte des changements de registration

#### Registration

La gamme porte également la description de l'instrument en terme de jeux de tuyaux et de groupes de jeux. Dans cette définition on retrouve, la liste des groupes de jeux présents dans l'instrument (d'ailleurs repris dans la description des notes).

Pour chaque groupe de jeux, les jeux de tuyaux sont décrits, qu'ils soient fixes ou pilotés par registres, ceux ci sont décrits pour permettre d'avoir une vision globale de l'instrument en terme de sonorités. Ces éléments sont codifiés pour permettre une analyse comparative des différents instruments et de transposition / conversion.

### Définition des trous

La description de la gamme étant le plus compliqué dans ce format de fichier, la définition des trous est beaucoup plus simple, chaque trou est décrit avec une date de début du trou (en millisecondes), une longueur de trou (en millisecondes) et une piste d'appartenance. La conversion entre le timing et le millimétrage sur le carton est réalisée par le biais de la vitesse proposée dans la définition de la gamme.

### 

Conclusion
----------

Loin de décrire toutes les particularités des instruments mécaniques, ce format nous a permis de simplifier grandement l'utilisation et l'échange de morceaux de musique spécialement composés/arrangés pour un instrument mécanique et sans pertes. L'utilisation de la description des gammes généralisées nous a également permis d'effectuer des comparaisons d'instruments et de réaliser des transformations avancées sur certains cartons.

Des scripts et exports simples de réalisation permettent alors d'exporter le contenu de ce fichier vers des fichiers midi, structurés d'une façon particulière (groupes de tuyaux dans un "track" midi distinct etc). Ce format .book est alors utilisé en format "pivot", plutôt que de réaliser des transformations croisées entre des fichiers midi différents, pour chaque nouveau type de fichiers midi, un import/export peut être spécifié.

Le format texte et XML utilisé n'est pas innocent car celui ci permet d'étendre à souhait les informations proposées, sans gêner les logiciels utilisant ce format. Il peut donc être possible d'allonger la liste des informations stockées dans ce format en fonction des besoins, sachant qu'un tronc commun définit ici, permettra l'échange entre les différents intervenants.


