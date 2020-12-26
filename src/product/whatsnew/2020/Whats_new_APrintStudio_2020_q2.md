# APrint Studio - 2020 - "Gérard et Ludwig"

*Patrice Freydiere - Novembre 2020*

![](splash-aprint-studio-2020-beta.jpg)



<u>Nota</u> : Cette version est actuellement en "test", et disponible uniquement pour **les utilisateurs rapprochés**.  Les fonctionnalités sont gelées.





## Introduction

**APrint 2020**, est une mise à jour importante, avec de nouvelles fonctionnalités clefs. 

- Support des **machines à pilotage Lazer**, intégré, aussi simple à utiliser que la version punch, intégrant
  - Export CAD (DXF et SVG)
  - De multiples paramètres pour les différents cas d'utilisation (plusieures passes, support des pliures, reglage des puissances ... )
- Amélioration de l'ergonomie de **l'explorateur de fichier**.
  - Ajout de bookmark, permettant de naviguer plus facilement dans vos arborescences
- Support simplifié du **scan par webcam** et **Video**
  - Possibilité d'utiliser des vidéos au format mp4, avi, ...
  - Simplification de la reconstruction de carton (1-Click)
  - Visualisation de la gamme de destination .... etc ...

APrint 2020, supporte désormais les **nouvelles versions de java**, son utilisation depuis les plateformes MacOS, Linux, est donc simplifié.

APrint 2020, porte le nom de **"Gérard et Ludwig"**, qui ont apportés énormément de choses à l'initiative Barrel Organ Discovery, et **ont libéré une partie du code écrit pour la perforation lazer** développé pour eux il y a quelques années. Ce code initial a largement été retravaillé pour simplifier l'ensemble des étapes et rentre cela utilisable pour les spécificités des CNC actuelles (GRBL 1.1 lazer).

L'ensemble de ces nouvelles fonctionnalités sont décrites ci dessous, vous pouvez egalement vous référer aux pages de documentation pour plus d'informations.



## Export CAD et prise en charge perforation Laser

Cette évolution fait partie des ajouts majeurs de cette version, propulsé par les tests de Yann et Jean Pierre, ceci a permis de largement simplifier l'utilisation et la mise en oeuvre et ainsi de démarrer en quelques heures. 

Une évolution appliquée, permet maintenant d'introduire de nouveaux types de machine. Ainsi, APrint propose avec les même facilité d'utilisation, de nouveaux types de dialects machine.

### Perforation Laser et Export CAD

![](exportCAD.png)

Bien que possible depuis quelques années.  Cette possibilité a <u>été libérée par Gérard et Ludwig</u>. Initialement développée pour eux, cette extension est maintenant disponible dans le produit.

Néanmoins, des amélioration significatives ont été apportées pour intégrer le noyau logiciel d'APrint.

Le middleware GRBL 1.1 a été ciblée pour cette première intégration (très utilisé), il est possible par développement d'en ajouter d'autres. 



et des améliorations : nouvelle communication machine, nouveau "dialect GCODE", permettant de gérer plus finement le GCODE généré. Et s'adapter en fonction des machines (Krunch, GRBL 1.1).



### Export SVG, DXF

Pour ceux qui disposent d'une machine externe, il est possible d'exporter la découpe d'un carton dans un fichier SVG ou DXF pour perçage externe. Ceci permet de préparer un fichier externe, pour une perforation dans un logiciel de gravage lazer externe.



### Pilotage GRBL 1.1 - Lazer direct

Plusieures nouvelles machines ont été ajoutées dans l'extension de punch. Initialement concu pour les machines à poinçons, cette extension s'est vu reconstruite pour prendre en charge les découpes linéaires de carton, ceci avec les mêmes écrans de pilotages.

L' utilisation reste aussi simple que la perforation, une fois la machine connectée.

La reprise après panne est également disponible, ainsi que les statistiques.



![](l1.png)



![](perfolazer.png)



## Amelioration de la numérisation de cartons

### Nouveau format de fichier bookimage

Cette version 2020 _Q2, apporte un nouveau format de fichier: le fichier **bookimage**. Ce format de fichier permet de stocker une images visuelle de carton, permettant de faire des **retouches interactives** sur une numérisation. 

Ces images sont supperposables sur la vue carton, pour retouche ou numérisation manuelle, ou assistée.



![](bookimage.png)



### Numérisation,à partir de fichiers video mp4

L'utilisation de telephone ou webcam, permet de créer des videos du défilement du carton. Ces video peuvent maintenant être utilisée pour construire une image complète du carton, au format BookImage

![](scan.png)



L'interface de reconstruction a été largement améliorée pour SIMPLIFIER l'utilisation, quelques clicks suffisent pour reconstruire le scan.



![](scan_and_recognition.gif)





## Evolutions sur la simplification d'utilisation



### Vers une utilisation réseau, façilitant le partage et l'échange de fichiers numériques

Pour permettre une collaboration plus directe entre les utilisateurs ou en reseau, et permettre un échange simplifié des création libres, une évolution a été réalisée pour supporter d'autres mode de lecture (notamment reseau).

Ainsi lors de la lecture de fichiers, il est possible de cibler maintenant des sites FTP, HTTP, WEBDav, ... etc. Les utilisateurs ayant plusieurs postes, ou souhaitant partager leur fichiers, ne sont plus forcé d'envoyer les éléments par mail. Ils peuvent utiliser en lecture et écriture un site FTP distant ou HTTP WebDav. L'authentification vers ces connexions réseau est également prise en charge. 

Ceci facilite également la récupération et l'échange de définition d'instruments. En utilisant une URL, le fichier est directement récupéré par APrint et utilisable directement.

Pour les utilisateurs qui ne souhaitent pas partager ou mettre des éléments sur le reseau, ceci ne change rien pour eux.



### Nouvel explorateur de fichier

Une nouvel explorateur de fichier permet de simplifier l'utilisation, et pour aller plus vite dans différents répertoire. 

L'explorateur s'est doté de marque pages, permettant de mémoriser rapidement plusieurs emplacement. un double click sur le marque page positionne l'explorateur au bon endoit. Ceci est particulièrement pratique lorsque l'on navigue à plusieurs emplacements.



### Nouvelle fenetre latérale de description de carton

Les propriétés du carton (métadonnées), sont maintenant accessibles plus facilement avec le panneau latéral. Cette mise en valeur, permet le renseignement des éléments du carton, la génère, les dates associées. Ces informations sont toujours utilisées dans les fonctions d'indexation et de recherche.

La saisie de ces éléments permet d'informer les utilisateurs du carton des éléments de provenance, arrangeur, .. etc



## Model Editor

Le Model editor permet d'automatiser certaines taches de transformation de cartons, et simplifie le passage de fichiers midi ou de transposition. Pour plus d'information sur cet outil, consultez la page de documentation, pour apprendre à l'utiliser et créér vos propres transformations.

Dans cette version des améliorations ont été apportées :

- Sélection visuelles et interactives sur les instruments. Il n'est plus nécessaire désormait de connaitre le nom de l'instrument avec précision, ce choix est réalisé de façon interactive.



## Aide en ligne

Nouvelle présentation de l'aide en ligne. Cette évolution a été proposée pour permettre des traductions automatiques plus simple dans les différentes langues. 

D'autre part, l'aide en ligne est maintenant modifiable par tous. Pour cela il vous suffit d'avoir un compte Github (plateforme hébergeant le code source)

L'aide en ligne est automatiquement publiée sur [https://barrelorgandiscovery.github.io/APrintDoc/](https://barrelorgandiscovery.github.io/APrintDoc/).



Sur chaque Page un icone "crayon", vous permet d'annoter et proposer des corrections pour tous.



## Compatibilité Java 9+, 11,12,13,14

Un travail sur le logiciel a été réalisé pour prendre en charge les nouvelles versions de java. Cette évolution ne touche pas les utilisateurs Windows, qui ne sont par impactés (la version de java est embarquée dans l'installation, et ne dépends pas du système).

En revanche cela simplifie l'utilisation pour les utilisateurs MacOS (forcés de passer sur les dernnières version).



## Des évolutions techniques

### Passage à la version XML book 2016

Cette nouvelle version de xml, (toujours normalisée), intègre, entre autre l'orientation de déplacement du carton. (droite à gauche ou gauche à droite).

Une réorganisation technique permet maintenant de pouvoir avoir un descriptif XML des commandes de perforation. Ceci pour améliorer les éléments techniques de perforation et permettre la sauvegarde de plan de perforation pour une utilisation en production, prépréparée.



## Et toujours des évolutions de qualité logicielle

- Fix sur la partie sonore, un bug remonté par **Yann Baraffe** a permit d'améliorer l'écoute lorsque l'instrument a beaucoup de registres. Les soundbank SF2 générée dupliquaient les définitions de mapping, provoquant de multiple jeux dans les logiciels. Ceci a été corrigé.



## Breaking Changes - Changements impactants

- Cette version intègre une nouvelle version de la reconnaissance de carton, les modèles de reconnaissance créé avec l'ancienne version ne seront pas compatible avec celle ci. Il sera donc nécessaire de les reconstruire. Pour simplifier, une version associée de Fiji est disponible maintenant dans l'installation d'aprint.