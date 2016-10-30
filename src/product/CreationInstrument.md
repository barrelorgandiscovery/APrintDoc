Notes sur l'enregistrement d'instruments dans le logiciel
=========================================================

Novembre 2011

Introduction
------------

Une des forces du logiciel est l'utilisation d'enregistrements d'instruments réels. Le réalisme de la restitution sonore, est très utile pour donner une idée d'un arrangement de morceaux de musique sur un instrument.

Les logiciels APrint et APrint Studio utilisent des échantillons des tuyaux et des hanches et les restituent pour chaque jeu de notes.

Cette technique permet d'avoir une bonne première approche finale, avec un enregistrement simple.

Dans les différents enregistrements que nous avons pu effectuer, nous avons enregistré des tuyaux sur les instruments eux-mêmes (sans démontage). Ceci permet de conserver certains aspects du jeu de l'instrument comme par exemple : certaines harmonies, certains bruits caractéristiques ainsi que la restitution sonore dans l'espace.

Par expérience, nous avons remarqué que l'enregistrement sonore demande certaines précautions sur les méthodes d'échantillonnage, de prise de son, et de choix des sons.

Cet article a pour but de proposer une première approche sur l'enregistrement. Loin d'être exhaustif, il sera enrichit avec les retours d'expériences et des compétences des différents utilisateurs.

Nous proposons ici une démarche sur les quelques enregistrements réalisés.

Dans cette démarche, nous avons essayés de limiter au maximum tous les biais numériques, en essayant de préserver au maximum les caractéristiques sonores de l'instrument.

1 - Etapes d'enregistrement sonores
-----------------------------------

Trois étapes minimum sont nécessaires pour la création d'un nouvel instrument :

-   Définition de la gamme de l'instrument et création d'un carton de gamme
-   Enregistrement des sons de la gamme et des registres
-   Création de l'instrument dans le logiciel et amélioration de la restitution

2 - Définition de la gamme de l'instrument et création du carton de gamme à enregistrer
---------------------------------------------------------------------------------------

Une première étape consiste à créer un carton contenant la gamme de l'instrument. Ce carton de gamme sera ensuite joué par l'instrument et enregistré note à note et registre par registre.

Pour créer le carton de gamme, la définition de l'instrument (fichier de gamme ou fichier .scale) doit être réalisé.Cette définition peut être faite dans le logiciel en utilisant l'éditeur de gamme.

Si l'orgue partage une gamme d'un autre instrument existant ou récupéré, il est possible de reprendre celle-ci sans avoir à la redéfinir. On utilise alors la fonction d'export de l'éditeur d'instrument.

La description de la gamme permet de connaitre les notes à enregistrer ainsi que les différents registres de l'instrument. Les registres sont importants car le carton de gamme doit pouvoir jouer les différents sons des registres pour une meilleure restitution.

Une fois la gamme définie ou récupérer, un scripts permettent de générer un carton de gamme directement. Le script prends en compte un jeu long du tuyau ainsi que des répétitions successives pour voir le comportement sonore dans l'attaque et la fin du jeu.

Les percussions sont également à enregistrer. (la gamme de test prend également en compte les registres et l'enregistrement de ceux ci unitairement).

La définition de la gamme à enregistrer est clef dans le processus, et plusieurs points d'attention sont à considérer :

-   Un enregistrement de quelques secondes doit être prévu pour chaque note. Ce long enregistrement de chaque note, permet d'éviter un travail de boucle sur l'échantillon et introduire un biais numérique.
-   Une répétition de chaque note est également à enregistrer, ceci permet de mieux repérer dans la partie sonore l'attaque et les temps de début et de fin du son par rapport à la commande mécanique.
-   Les percussions sont également à enregistrer

3 - Préparation de l'enregistrement sonore
------------------------------------------

Nous avons procédé ainsi dans nos enregistrements :

### Mettre l'instrument dans un lieu neutre et silencieux

Le lieu doit être au maximum neutre dans le sens où les effets de réverbération doivent être limités (sauf si la restitution doit refléter également cette réverbération naturelle).

Il est souhaitable d'éviter les églises ou des locaux vides, qui comportent des murs renvoyant le son à de multiples reprises. Dans le cas où une réverbération est souhaitée, celle ci peut être ajoutée à postériori par le logiciel.

Les lieux extérieurs peuvent également être utilisés, mais ceux ci posent des problèmes de souffles dans les micros s'il y a du vent. (à cet effet, certains micros sont équipés d'accessoires ou de mousses permettant la prise de son en extérieur).

### Essayez de réduire les sons parasites

Certains sons comme la soufflerie, ou des bruits mécaniques peuvent être enregistrés dans le cas d'instruments simples, par contre, si ces bruits sont enregistrés sur chaque prise de note, lors de la restitution d'un carton, plusieurs notes étant jouées en même temps, ces sons vont se cumuler dans la restitution. Ces effets deviennent gênant sur les gros instruments avec beaucoup de registres.

Il peut être proposé de réduire l'importance des ces bruits si ceux ci sont prépondérants, par exemple en camouflant la soufflerie ou essayant un meilleur micro (pour le bruit d'enregistrement).

Un retour d'expérience serai apprécié sur des conditions différentes de numérisation.

3 - Numérisation des sons
-------------------------

Pour numériser les sons de l'instrument, plusieurs matériels doivent être considérés :

-   Le Microphone
-   L'enregistreur numérique

#### Le Microphone

Le microphone doit être de bonne qualité, plusieurs technologies de micro peuvent être utilisées en fonction du résultat souhaités. (omnidirectionnel, directionnels ... à bobine ou électrostatiques). (http://fr.wikipedia.org/wiki/Microphone)

La position du micro est très importante pour l'enregistrement, celui ci doit être positionné en frontal et à bonne distance de l'instrument, afin de pouvoir capturer les différents tuyaux et leur répartition dans l'espace.

En gardant une "position fixe" du microphone durant l'enregistrement, celan permet de garantir une prise de son uniforme sur l'ensemble des éléments enregistrés.

Pierre Penard sur son site propose un petit montage électronique pour utiliser deux électrets, et qui effectue une moyenne et une balance de prise de son de chaque coté de l'instrument. (http://orgue-de-barbarie.pagesperso-orange.fr/bidouille.htm)

Un micro récent capture également beaucoup mieux les fréquences par rapport à un micro ayant quelques années.

Penser également à la bande passante du micro, en effet certains micros dédiés à la voix vont atténuer les basses, pourtant très importantes dans l'enregistrement d'un orgue de foire.

La prise de son est quelque chose de complexe, et également fonction du niveau de qualité souhaité dans l'enregistrement. Plus il est souhaité une grande fidélité, plus la mise en oeuvre sera délicate.

**En retour d'expérience, lors de l'enregistrement, il est nécessaire que le micro une fois positionné ne soit plus déplacé pour l'ensemble des échantillons. En effet le déplacement du micro en cours de route ne reflètera plus la balance sonore naturelle de l'instrument et des différents les volumes des tuyaux d'origine. Si le micro est déplacé, cela peut donner des résultats hasardeux.**

#### L'enregistreur numérique

Préférer un enregistreur numérique portatif à un ordinateur. En effet l'enregistreur numérique ne fait pas de bruits additionnel (contrairement à la ventilation d'un ordinateur). L'ordinateur, ayant des hautes fréquences parasite également la prise de son, introduisant des frequences non souhaitées dans l'enregistrement.

Utilisez si possible un format d'enregistrement sans perte (WAV, ou brut), les formats d'enregistrement type MP3 par exemple, introduisent des modifications dans l'échantillon et perdent certains signaux (filtrage fréquentiel). Le format MP3 impose egalement un transformation informatique au format WAV pour être utilisé dans le logiciel (limitons les transformations informatique si possible)

Utilisez un échantillonnage à 44Khz de fréquence, cette fréquence d'échantillonnage est celle utilisée par les CD, et présente une bonne qualité audio. Cette vitesse d'échantillonage induit également de de gros volumes de fichiers de sortie, donc prévoyez la place nécessaire sur l'enregistreur numérique.(Dans un soucis d'optimiser la taille des échantillons créés, réalisez un échantillonage en MONO)

En retour d'expérience, enregistrez un minimum de 3 à 4 secondes par note. Cela vous sera utile lors de l'opération de "mapping". Lavitesse moyenne de défilement du carton étant de 6cm/seconde, vous obtiendrez la possibilité de jouer la note sur 18 à 24 cm sans avoir à réaliser de "boucle numérique" sur le son. Cette opération de "boucle" étant assez fastidieuse à réaliser. Procédez par ordre et méthode. Nommez et enregistrez vos échantillons de façon à pouvoir les identifier plus facilement. Créez des répertoires au nom des éléments enregistrés (ex: Accompagnement, Piccolos - contrechant, Trombones-basses, ...) et placez vos échantillons en les nommant, par exemple, comme ceci : "numéros de piste dans la gamme - nom de la note" (ex:"31-LA.wav", "32-SI.wav", "38-FAdiese.wav", ...) Cette méthode vous facilitera l'étape du "mapping".

#### Récupération des échantillons et premiers traitements

Une fois l'enregistrement de la gamme et des différents registres ont été réalisé avec l'enregistreur numérique, les sons doivent être repérés et découpés (dans le gros fichier .WAV d'enregistrement)

**Préservez les attaques des tuyaux dans le découpage, c'est extrêmement important pour le caractère de l'instrument. Chaque instrument est différent et une de ses caractéristique d'écoute est cette phase transitoire du tuyau avant l'instauration du régime permanent**.

Préservez l'attaque des tuyaux (ou anches)

Pour une meilleure restitution vous pouvez également regarder et préserver les inégalités de temps d'attaque des notes , (ex : les basse par exemple mettent plus de temps à réagir que les flutes du chant). Ce delta peut être mesuré dans l'enregistrement de notes courtes à la fin de l'enregistrement de la note longue.

Retour d'expérience : Ne retravaillez pas numériquement les échantillons. La suppression du bruit par analyse de zones non bruitées détériore l'enregistrement. Préférez un bon enregistrement audio avec un bon micro à un retraitement numérique à postériori. Un traitement numérique peut être réalisé, mais en très bonne connaissance du sujet, (les réponses fréquentielles des micros, des fréquences de l'instrument ... etc).

Evitez les réductions ou augmentation de volumes, cela détruit l'équilibrage souhaité de l'instrument par les facteurs d'orgue. On peut abusivement augmenter le volume des basses sur un ordinateur n'ayant pas de bons "hauts parleurs" (speakers) et rendant une bonne restitution, cependant si l'on écoute l'instrument sur de bons speakers le résultat est désastreux.

4 - Construction et répartition des sons sur l'instrument
---------------------------------------------------------

Une fois les sons récupérés et enregistrés, il reste une phase importante dans la construction sonore de l'instrument : le "mapping".

Le "mapping" consiste à attribuer un son à une ou plusieurs notes de l'instrument, quelques guides ci dessous permettront de tirer au mieux de l'échantillonnage réalisé:

-   Mapper les sons dans les mêmes sections de registres, autrement dit : ne prenez pas une note du chant pour la mettre sur une note de l'accompagnement. Connaissez la facture de votre instrument et regardez bien les différents types de tuyaux pour prendre les sons adéquats.
-   Choisissez dans les sons d'une section de registre, un ou plusieurs sons bien enregistrés. Il arrive que certains tuyau ne soient pas bien accordés ou réagissent différemment de leur voisins. Cela peut être souhaitable pour la bonne conformité de restitution.
    Si un tyau est "particulier" et que vous souhaitez garder ce comportement, enregistrez alors les tuyau voisins). Si vous utilisez ce son sur plusieurs tuyaux, vous généralisez alors ce caractère particulier, donc vous changez l'identité de l'instrument.
-   N'associez pas une plage trop grande de notes pour un son, multipliez les sons. En retour d'expérience, ne dépassez pas 3 notes d'écart par rapport à la note du son, plus le son est utilisé sur les notes "lointaine" de la note de base du son, plus le son est déformé par rééchantillonage par le logiciel. Par exemple, pour mapper les notes "do, re, mi, fa, sol, la" nous sélectionnerons l'échantillon RE pour mapper "do, re, mi" et l'échantillon SOL pour "fa, sol, la".
-   Multipliez les échantillons dans la partie haute de l'instrument, en effet les sons aiguës on des fréquences beaucoup plus élevées et c'est sur cette plage que la déformation s'entends malheureusement le plus. C'est dans cette plage que les opération mathématiques opérées sur des échantillons manquant, divergent pas rapport à l'instrument.

Bref, la partie mapping est une partie délicate de la création de l'instrument. Plusieurs essais sont à réaliser, sur des cartons différents. L'écoute unitaire peut ne rien donner, mais sur un carton de musique, on reconnaît mieux l'instrument.

Prévoyez un peu de temps pour cette étape.

En Synthèse
-----------

Parce que l'important, c'est l'instrument,

Soyez propre sur la partie acquisition du son. Essentielle pour un bon instrument échantillonné.

Ne retravaillez pas abusivement numériquement les échantillons

Préservez les caractéristiques des sons (et notamment l'attaque)

Ne pas négliger la partie association de son et mapping.

### Bibliographie / Références

http://fr.wikipedia.org/wiki/Microphone

http://organ.10.forumer.com/a/creating-organ-soundfonts\_post1133.html

Methode de prise de son légère : http://www.fonema.se/blockhead/blockhead.html (anglais)

### Contributeurs / Auteurs du document

Patrice Freydiere (Auteur)

Olivier Dupont (Auteur)

Pierre Dupont (relecture, adaptation)

Pierre Penard (relecture, commentaires)
