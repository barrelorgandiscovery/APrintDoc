# APrint Studio - 2020 - "Jean Pierre version"

*Patrice Freydiere - Aout 2020*

![](splash-aprint-studio-2019.jpg)

## Introduction

APrint 2020, est une mise à jour technique importante, néanmoins les utilisateurs trouveront de nouvelles fonctionnalités. 





APrint 2020 intègre également de nombreuses améliorations, simplifiant l'utilisation occasionnelle et quotidienne.



## Prise en charge en standard du perçage Laser

Bien que possible depuis quelques années, cette possibilité a été libérée par gérard dabonnot. Cette ci a été donc retravaillée, pour intégrée le noyau d'APrint. 

Le middleware GRBL 1.1 a été ciblée pour cette première intégration (très utilisé), cependant il est possible par développement d'en ajouter d'autres. Plusieures capacités : nouvelle communication machine, ou nouveau "dialect GCODE", permettant de gérer plus finement le GCODE généré. 

#### Export SVG, DXF

Pour ceux qui disposent d'une machine externe, il est possible d'exporter la découpe d'un carton dans un fichier SVG ou DXF pour perçage externe.

@@@

### Pilotage GRBL - Lazer direct

Plusieures nouvelles machines ont été ajoutées dans l'extension de punch. Initialement concu pour les machines à poiçons, cette extension s'est vu reconstruite pour prendre en charge les découpes linéaires de carton, ceci avec la même interface très simple.

L'utilisation reste aussi simple que la perforation, une fois la machine connectée.

La reprise après panne est également disponible, ainsi que les statistiques.

@@



## Amelioration de la numérisation de cartons





## Vers une utilisation reseau

Pour permettre une collaboration plus directe entre les utilisateurs ou en reseau, une amélioration a été réalisée pour supporter d'autres mode de lecture (notamment reseau).

Ainsi lors de la lecture de fichiers, il est possible de cibler maintenant des sites FTP, HTTP, WEBDav, ... etc. Les utilisateurs ayant plusieurs postes, ou souhaitant partager leur fichiers, ne sont plus forcé d'envoyer les éléments par mail. Ils peuvent utiliser en lecture et écriture un site FTP distant ou WebDav. L'authentification est également prise en charge. 

Ceci facilite alors la récupération de nouveau instruments, avec simplement une URL pouvant être mise dans le nouvel explorateur de fichiers.

Pour les utilisateurs qui ne souhaitent pas partager ou mettre des éléments sur le reseau, ceci ne change rien pour eux.



### Nouvel explorateur de fichier

Une nouvel explorateur de fichier permet de simplifier l'utilisation, à la fois pour la prise en charge du mode reseau, et pour aller plus vite dans différents répertoire.

L'explorateur s'est doté de marque pages, permettant de mémoriser rapidement plusieurs emplacement. un double click sur le marque page positionne l'explorateur au bon endoit. Ceci est particulièrement pratique lorsque l'on navigue à plusieurs emplacements.





## Model Editor

De nouvelles améliorations sur le model editor. 



## Aide en ligne

Nouvelle présentation de l'aide en ligne. Cette évolution a été proposée pour permettre des traductions automatiques plus simple dans les différentes langues. 

D'autre part, l'aide en ligne est maintenant modifiable par tous. Pour cela il vous suffit d'avoir un compte Github (plateforme hébergeant le code source), de "forker" le repository APrintDoc. Vous pourrez alors par le web, ou sur le poste faire des modifications directement, et proposer des "pull request" pour que celle ci soit intégrées.

L'aide en ligne est automatiquement publiée sur ()[https://barrelorgandiscovery.github.io/APrintDoc/] après intégration.



## Compatibilité Java 11,12,13,14

Une mise à jour du logiciel a été réalisée pour prendre en charge les nouvelles versions de java. Ceci ne touche pas vraiment les utilisateurs Windows, qui ne verront pas la différence.

En revanche cela simplifie l'utilisation pour les utilisateurs MacOS (forcés de passer sur les dernnières version).



## Et toujours de petites évolutions ...

