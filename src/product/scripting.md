
Scripting avec APrint
=====================



Bien que le logiciel permette de réaliser des cartons, certaines fonctionnalités n'ont pas été prévues ou même développées. APrint et APrint Studio intègrent un langage de script permettant de prototyper ou combler des manques dans le programme initial. dans l'activité d'arrangement de carton, il est fréquent de faire des manipulations qui n'ont pas été prévues, le langage de script permet d'ajouter des fonctionnalités facilement sans être développeur.

Plusieurs consoles de script ont été intégrées à des endroits stratégiques du logiciel. Il est ainsi possible de manipuler les instruments, le carton, les exports vidéo, la génération de gamme et tous les objets utilisés dans le logiciel. Il est également possible de créer des fenêtres pour faciliter l'utilisation de ces nouvelles fonctionnalités.

APrint utilise le language groovy comme moteur de scripts. Ce language simple à apprendre a une multitude d'exemple, tutoriels, informations de références sont disponibles sur le site de groovy à cette adresse http://groovy.codehaus.org/ . Ce langage basé sur Java permet d'exploiter tous les objets du logiciel APrint

L'utilisation du langage de script au sein du logiciel est réalisée dans des consoles, ces consoles donnent accès au contexte direct de l'application via des variables prédéfinies qui permettent d'accéder aux objets vivants de l'application.

Il est également possible d'utiliser principalement le langage de script (utilisation de la console Groovy) et d'y ajouter en référence les objets du logiciel APrint.

Plusieures consoles sont disponibles dans le logiciel :

Une console générale, une console carton (quickscript), une console pour la partie instrument (export / import / transformations).


Console générale d'APrint
-------------------------

Située dans le menu Outil, cette console permet d'effectuer des opérations générale non forcement liées à un carton. cette console générale permet entre autres d'automatiser l'import du fichier MIDI, ainsi que toutes les tâches répétitives sur plusieurs objets du logiciel (instrument, cartons).

**La console définit le point d'entrée suivant :** la variable **"services"** est un objet permettant d'effectuer les operations suivantes :

Method

Description

Object **getOwnerForDialog** ()

Récupération de la fenetre globale, utilisée pour les fenetres modales

dR

Repository2 **getRepository** ()

Récupération de l'objet contenant les instruments

void **newVirtualBook** (VirtualBook virtualBook, Instrument instrument)

cree une nouvelle fenetre avec le carton et pour un instrument donné.

void **newVirtualBook** (VirtualBook virtualBook, Instrument instrument, IssueCollection collection)

cree une nouvelle fenetre avec le carton et pour un instrument donné, avec éventuellement un passage des erreurs (issuecollection)
