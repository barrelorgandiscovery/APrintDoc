Ce document aborde des concepts élémentaires ainsi que des précautions pour la prise de son amateur, avec pour principe de préserver une bonne qualité à un budget modéré. En suivant la théorie en trame de fond, des trucs et astuces spécifiques sont inclus pour permettre au lecteur de reproduire mon système utilisé lors d'enregistrement de banque de sons sur le site MMD.

La Théorie
----------

L'accoustique de la pièce et la distance du microphone

La chaîne d'enregistrement débute avec la source sonore et son environnement. Une première chose est le son direct, qui dans un sens est un vrai signal. Une autre est l'environnement qui crée des réverbérations mais aussi qui peut ajouter d'autres sons comme les spectateurs ou des bruits divers, désirés ou non. Une première observation est que le niveau du son direct décroit de 6 dB (niveau de pression sonore divisée par deux) à chaque fois que l'on double la distance à la source. Le son, lorsqu'il est émit dans une pièce, rebondit contre toutes les surfaces et parfois crée plus ou moins des champs de sons plus diffus. A chaque rebond, une fraction du son est absorbée, ainsi le son réverbéré s'estombe progressivement. Une caractéristique importante est le temps de réverbération, qui définit le temps pour lequel le son réverbéré est diminué de 60 dB après que la source ait été arrêtée. (d'après W.C. Sabine qui au début de l'accoustique de pièce au MIT dans les années 1900 sollicita une pièce avec un tuyau d'orgue et mesura le temps d'extinction). Les temps de réverbération typiques dans une salle à manger sont de 0.5s, pour un auditorium de 0.5 à 0.8s, pour une salle de concert, 0.8-1.5 secs, pour une église 1.5 secs ou plus. Le temps de réverbération T en secondes peut être estimé en utilisant la formule de Sabine :

T = 55\*V/(cA)

V est le volume de la pièce en M3, c la vitesse du son (343m/s) et A la surface d'absorption en M2.

La surface d'absorpsion est une représentation fictive de la pièce "sans perte" à exception d'un trou, d'une surface A. Toutes les ondes énergétiques sonores rencontrant cette surface sont perdues. En Pratique, A=S\*Alpha où S est l'aire physique de la surface. Alpha a pour valeur 0.02 pour du béton, 0.10 pour du bois et jusqu'à 0.50 pour des rideaux. Le calcul du temps de réverbération pour une pièce à partir des surfaces est connu pour ne pas être très fiable. En pratique, on effectue souvent une mesure du temps de réverbération à partir d'une excitation, C.a.d à partir d'un claquement de main ou un tir. Après cela, connaissant T et V, on peut calculer A à partir de la formule de Sabine.

Une seconde observation est que le niveau de ce champ de réverbération est indépendant de la localisation dans la pièce, les ondes sonores réverbérées voyagent plusieurs fois dans les dimensions de la pièce. A une certaine distance de la source, l'"angle de réverbération", le niveau sonore "direct" est égal au niveau de réverbération. Dans une salle à manger la distance typique est 0.7m, dans une salle de concert 4-8m. Cela peut être calculé à partir de la formule r=sqrt(1/16pi).

Ce "r" est essentiel pour placer un microphone d'enregistrement. Placé plus près de la source que le rayon de réverbération, le son direct sera plus fort. Plus loin les réverbérations domineront, ce qui peut être pris pour de la stéréo, mais sans plus d'intérêts. De toutes façons, les perceptions humaines inclues l'"Effet Haas" (l'effet de précédence, la loi de la première onde). Vous pouvez toujours écouter la direction incidente d'un son (le situer) quand le son direct est plus important de 10dB par rapport à la réverbération. C'est pourquoi l'interprétation sonore du cerveau détecte que le son direct vient plus rapidement que ses réverbérations. En synthèse : la distance du microphone de l'objet contrôle le ratio entre le son direct et les réverbérations et l'enregistrement stéréo en utilisant une distance de microphone de plus de trois fois du rayon de réverbération contient très peu d'informations directionnelles sur la source.

Les résonances de pièce peut être un problème lorsqu'elles sont largement espacées en terme de demi tons aux basses fréquences. Dans une pièce à faibles résonances, certains emplacements peuvent avoir un haut niveau sonore et à d'autres endroits presque pas de sons. Ce comportement diffère entre les notes mais vers les hautes fréquences , les résonances de la pièce deviennent de plus en plus proches et ne peuvent être détectées séparément. La fréquence Schroeder fs = 1900 \*sqrt (T / V), où T est le temps de réverbération en secondes, V est le volume de la pièce en mètres cubes, nous indique la fréquence limite de division au dessus de laquelle les résonances ne sont plus un problème car celles - ci deviennent suffisamment proches les unes des autres. Dans une salle à manger fs est typiquement au dessus de 100Hz, dans une salle de concert : 20 Hz. Les personnes de la HiFi devraient savoir qu'il est sans espoir d'avoir une réponse de basse uniforme dans une petite pièce, sauf si celle ci est fortement amortie avec des meubles rembourrés ou d'autres moyens afin de faire baisser le facteur T. Il y a une raison pour qu'une pièce d'écoute soit d'un volume suffisant, sinon vous êtes liés à des problemes avec la distribution des sons de basses.

Un autre problème peut survenir lorsque la pièce a de grandes surfaces parallèles peu amorties. Alors le champ de réverbération peut avoir de fortes composantes non diffuses, avec des pics de résonances périodiques et des échos fluctuants, de telle sorte que vous pouvez "écouter la salle" dans l'enregistreent comme un confinement déplaisant et "teinté".

Normalement on ne remarque pas cet effet en étant soit même dans la pièce, parce que notre système de perception s'adapte et le compense (il calibre sa compensation par rapport aux bruits, mouvements et paroles). Cette compensation n'apparait pas avec un système d'enregistrement.

Microphones
-----------

Un microphone a toujours un diaphragme léger et petit qui suit le mouvement du son reçu. Ce mouvement est converti en un signal électrique, disponible dans le fil de connection du microphone. Dans le champ des types de conversion mécanique/électrique, un microphone peut être "Electrostatique" (condensateur et electrets) ou "electrodynamic", sans mentionner les autres types ésotériques ou utilisant de vieux principes, maintenant rarement utilisés.

-   Les microphones Electrostatiques ont toujours besoin d'une alimentation électrique utilisée dans amplificateur Haute / Basse impédance, les condenseurs nécessitent une polarisation utilisant un haut voltage. Cette alimentation peut être prise d'une batterie à l'intérieur ou à proximité de la capsule, ne pas oublier de l'éteindre après usage. Les systèmes professionnels sont fréquemment alimenté par une alimentation 'phantom' utilisant typiquement 48V à partir d'une table de mixage ou d'un préamplificateur, utilisant le même câble que le microphone. Les microphones électrostatiques ont une réponse fréquentielle plate, couvrant toute la plage de fréquences audio.
-   Les microphones dynamiques génèrent leur sorties par induction dans un conducteur, se déplaçant par le son, dans un champ magnétique. Ils n'ont pas besoin d'alimentation complémentaires mais ont toujours une plage de fréquences limitée, typiquement entre 50Hz et 15Khz. Même les microphones de bonne qualité dérivent considérablement d'une réponse fréquentielle plate.

Dans une perspective d'enregistrement des propriétés directionelles, un critère discriminant est également la pression et le gradient de pression des microphones, combiné avec d'autres caractéristiques.

Dans un microphone à pression, le son atteint seulement une face du diaphragme. Il mesure la pression sonore instantanée locale, qui est indépendant de la direction du son car la capsule est petite à comparer avec la longueur d'onde. Ce type est omnidirectionnel et parfois appelé "boule"

Dans un microphone à gradient de pression, le son atteint les deux faces du diaphragme et mesure la différence de pression. Ceci est proportionnel à la vélocité des particules d'air dans l'onde sonore, ceci est caractérisé par la "vélocité" ou vitesse du microphone. Ceci caractérise la directionnalité du microphone. Donc une sensibilité devant ou derrière mais pas sur les côtés, le type est parfois appelé 'fighre of eight'.

Ces deux principes peuvent être combinés dans des microphones avec plusieurs propriétés directionnelles. Par exemple la somme de chacun effectuera un rendu "cardioide", avec une sensibilité nominale en face des hémisphères mais avec une perte dans le contrôle de la réponse fréquentielle.

La plupart des microphones fonctionnent bien à des niveaux sonores jusqu'à 130 dB. Au delà, les membranes sollicitées peuvent entrer dans des déplacement non linéraires, lié à leur fixation ou taper sur l'électrode, il y aura alors des distorsions d'intermodulation. Un microphone de mesure typique mesure jusqu'à 20 dB de plus mais d'un autre coté a une sensibilité plus basse et un niveau de bruit plus haut.

Enregistrement stéréo

L'objectif d'un enregistrement stéréo est de communiquer une image à celui qui écoute, en transmettant une sensation de distance et de direction de la source sonore. Cela effectue un rendu plus clair, les sources différentes de sons sont séparables et sont beaucoup moins embrouillées les unes par rapport aux autres. Normalement on souhaiterait également contrôler le niveau de réverbération pour créer l'ambiance. Cet aspect est réalisé en sélectionnant la distance entre les microphones et la source.

Un des plus vieux types de microphone est dans un sens le meilleur, pour ne pas le nommer, une tête articifielle avec une paire de microphones à pression où sont situés les canaux auditifs. La tête bêtement interfère avec le champ de sons de façon "correcte", les signaux des microphones proposent une vraie représentation de ce que l'on entendrait soi-même avec respectivement l'oreille gauche et droite. L'effet d'ombrage de la tête ainsi que les différences de temps inter aural sont automatiquement pris en compte. N'importe comment, pour une écoute optimale et réaliste il faut également le reproduire en conséquence. En utilisant des écouteurs, ainsi les deux canaux stéréo sont gardés séparés. Cette façon est la restitution la plus proche et la plus approchante d'une écoute enregistrée à un emplacement donné. L'annexe ci dessous décrit les essais sur une tête artificielle.

Pour un enregistrement stéréo en utilisant des moyens classiques, est l'utilisation d'un système XY où deux microphones directionels sont placés au même endroit, ce que l'on peut avoir avec un microphone stéréo conventionnel.

Actuellement, pour les enregistrements professionnels, le plus souvent le système AB est utilisé, deux microphones distancés de 20cm à 2m, omnidirectionnels et de préférence cardioides. Ce systeme n'est pas compatible avec le Mono, lorsque les deux signaux sont ajoutés, il y a des interférences "dips" dans la réponse fréquentielle à cause de la différence de distance des deux microphones.

Les têtes artificielles sont rarement utilisées dans les prises de son commerciales. Une raison est que ces prises de son sont principalement utilisées pour une restitution sur des haut parleurs où les canaux sont mixés. Une autre raison est que lorsque les sources sonores ne sont pas "petites" au comparé de la pièce (par exemple un gros orchestre ou un orgue). Alors il peut être impossible de trouver une place unique où le son est suffisamment bon pour l'enregistrement. Alors l'ingénieur du son peut contrôler les propriétés de chaque resultat stéréo de la piste, avec l'objectif de créer une image accoustique acceptable. Une prise de son commerciale est principalement un produit et pas forcement un son 'naturel'. Historiquement, de tous temps les critères et méthodes appropriées pour effectuer un "vrai" enregistrement, de même que les goût ont toujours été un grand débat.

Un joli effet de stéreo est que les sources de bruits sont souvent localisées ailleurs que la source sonore d'intérêt, l'auditeur peut alors les entendre loin de lui.

Le mixage

Le climat électromagnétique à l'intérieur d'un ordinateur est extrêmement hostile pour les signaux faibles de circuits analogiques, des beeps ou signaux non aléatoires peuvent être injectés. Afin de se prémunir de cela, les signaux en provenance des microphones devraient être amenés dans des câbles blindés et tenus à l'écart des équipements provoquant des sources d'interférences. Dans des circonstances particulières, il peut arriver que la carte son de l'ordinateur ne possède pas d'entrée microphone, à la place il faut utiliser une connectique "line in" pour un signal fort. Même si cela n'est pas absolument nécessaire, il est souhaitable d'insérer une console de mixage entre le microphone et l'ordinateur. Un argument en faveur de la table de mixage est qu'elle propose la préamplification nécessaire et l'alimentation associée nécessaire aux microphones. Il est également beaucoup plus facile de paramétrer l'acquisition avec de bons vieux boutons et de tout faire à la souris de l'ordinateur. Il est souhaitable de laisser uniquement à l'ordinateur les ordres de jeu, d'enregistrement et de gestion des fichiers.

Une Chaine professionnelle d'aquisition utilisant des convertisseurs analogiques numériques de 24 ou 48 bits juste après le Microphone serait trop coûteuse pour un amateur.

Les mélangeurs (ou mixer) disposent d'une sortie casque avec un volume séparé pour le contrôle de l'aquisition. L'utilisation d'écouteurs fermés qui "déconnectent" du son ambiant. Lors de l'enregistrement il est préférable de ne plus entendre le son ambiant mais le son enregistré, qui provient bien de l'enregistrement. Le meilleur est de pouvoir s'isoler dans une pièce séparée de la salle d'enregistrement.

Les enregistreurs

Les enregistrements analogiques (par exemple : cassettes ) ne sont actuellement plus du tout compétitif face à un PC moderne, pour le prix et la qualité d'enregistrement. Une bonne option pour une meilleure transportabilité est d'utiliser un lecteur Digital DAT mais c'est une alternative assez coûteuse (1000 $), cependant ces appareils sont en proie à des problèmes de défaillance et de compatibilité avec d'autres lecteurs. Un enregistreur minidisk est une solution plus économique (300 $), mais à cause de son encodage de données incluant des compressions, il y a quelques pertes mineures dans la qualité du son et le média utilisé est pour l'instant en question vis à vis de sa pérénité pour l'archivage. La plage de fréquences d'un ordinateur et son bruit théorique (96dB) (signal / bruit) surpassent clairement les enregistreurs analogiques. Les ordinateurs Apple Macintosh sont historiquement les premiers dans le domaine du son et très utilisé dans la profession, mais les ordinateurs IBM PC Windows ont essentiellement pris.

Un système de base illustré ci dessous, où les blocks en bas montre les composants clef d'enregistrement d'un ordinateur PC.

Le format CD stereo 44.1 Khz et en 16bits est un standard de facto pour un bon enregistrement. C'est le format du moment pour l'enregistrement et utilise de la mémoire, à hauteur de 180Kb/s ou 11 Mb/minute pour la restitution. Un premier prérequis est un disque dur suffisamment rapide et un gros disque dur, ce qui n'est plus un probleme de nos jours.

Une interface Analogique / Numérique est utilisée dans les cartes son de l'ordinateur. Le rapport Signal / Bruit est typiquement autour de 75dB et meilleur que les enregistreurs analogiques.

Le logiciel central utilisé est un Editeur, avec différentes fonctions. Premièrement, pour piloter l'enregistrement et stocker le résultat :

Fournit un bouton Enregistrement (Record), Play (jouer), et Stop.

Contrôler l'enregistrement et le format de stockage, la vitesse d'échantillonage et la profondeur d'encodage (8/16/24/48 bits)

Définir le nom du fichier

En second lieu, pour les post-traitements après que l'enregistrement ait été réalisé :

Couper et Trancher les début et fins

Appliquer des "effets" comme l'égalisation, filtrage de bruits, etc ...

Convertir un enregistrement dans un autre format comme le MP3

Dernièrement le PC doit avoir un graveur pour la création de CD. Ainsi vous pouvez graver des fichiers WAV 44.1kHz, 16 bits stéréo en un CD audio standard. Les graveurs sont souvent fournis avec un logiciel d'édition. Il faut être au courant des capacités du graveur pour utiliser des CD-RW reinscriptibles, très pratiques pour des stockages intermédiaires.

Exemples d'équipements

Ceci est une énumération simple de mon équipement actuel.

Les Pièces

Un salon bien feutré peut être utilisé mais peut être que vous n'apprécierez pas la couleur "feutré" dénuée de réverbérations. Une petite pièce peu amortie est généralement catastrophique, ceci accentue les réverbérations de la pièce, ce qui colorera l'enregistrement et donne une impression de confinement.

Mes meilleurs résultats d'enregistrement de mon orgue dans une petite pièce est l'entrée de mon hall d'immeuble. La pièce n'est pas plus grande d'une salle à manquer et peu amortie mais est augmentée d'un petit escalier ouvert, ce qui fonctionne bien avec la réverbération de la pièce. Un truc et astuce est de mettre un épais matelas contre le mur derrière le microphone. C'est une solution contre les interférences de réverbération de l'arrière.

Avec une source sonore importante dans une petite pièce, comme par exemple certains orgues, la distance de rayon de réverbération est difficile à tenir en pratique.
