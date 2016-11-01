Utilisation de fichiers midi dans APrint
========================================

Lorsque l'on utilise Aprint pour récupérer des fichiers midi, on se pose la question de savoir comment le fichier midi doit être formaté pour être interprété correctement dans la conversion Carton. Cet article a pour vocation d'expliquer comment l'import de fichier midi est réalisé dans Aprint lors d'une conversion en carton.

Dans l'import standard Aprint, les opérations suivantes sont réalisées :

Lecture du fichier midi et décodage du format MIDI
---------------------------------------------------

Le fichier Midi, indépendamment du format 0 ou 1, est lu. Certains fichiers sont diffusés avec des headers MIDI corrompus, des corrections sont apportées afin de pouvoir lire l'ensemble des évènements et des méta messages.

Dans sa gestion interne du tempo, APrint converti en microsecondes les informations temporelles du fichier MIDI (les débuts de notes, longueurs de notes). Ainsi les informations de tempos ne sont gardées qu'à titre indicatif. Ce qui permet également à APrint de sauvegarder un fichier midi avec un unique tempo de sortie.

Décodage des évènements midi
----------------------------

Les évènements Midi sont ensuite lus dans les différents tracks et triés en fonction des "ticks" MIDI pour les avoir dans un ordre chronologique. Les évènements lus gardent une information de track et de canal. Les évènements de début de note/fin de note sont ensuite convertit en "note pleine" avec une date de début (time stamp en microseconde) et une longueur de note. Le fait d'avoir des notes simplifie ensuite la construction du carton virtuel.

Interprétation des notes de la gamme
------------------------------------

Les évènements MIDI étant décodés en note avec un début et une fin, on passe ensuite à l'interprétation des notes midi pour les mettre dans le carton. La question est comment mettre les bonnes notes sur le carton.

Dans le comportement par défaut, APrint regarde dans la gamme des noms des notes midi associées, puis recherche dans le fichier midi si la même note correspond. Si celle ci existe, elle est récupérée puis insérée dans le carton.

Les percussions sont traitées de la même façon. Le Canal 10 contient l'ensemble des percussions. Si une percussion définie dans APrint existe dans le fichier midi, avec le même code, celle ci sera importée dans le carton virtuel.

### Interprétation différente d'un fichier midi

Il arrive que certaines notes existent en double dans la définition du carton, en effet certains instruments de danse ou de foire peuvent avoir la même note midi dans l'accompagnement ou dans le chant. On souhaite également parfois effectuer des changements d'octaves ou d'autres transformations associées lors de l'import de fichiers MIDI.

Cette problématique peut être traitée dans Aprint par un petit script associé à l'instrument qui permettra de définir comment importer plus précisemment le fichier sur le carton.

Plus précisemment, on peut choisir dans le fichier midi de décaler les basses d'une octave artificiellement pour faire la distinction ou prendre un canal différent pour cela ou nommer la piste Midi pour faire correspondre la partie "BASSE" "ACCOMPAGNEMENT" ou "CHANT".

La mise en place de ce script permet de définir comment on importe un fichier midi et plus précisemment, comment on fait la correspondance avec le carton pour le placement des pistes.

*Pour la mise en place de scripts associé à un instrument, voir la rubrique de manipulation de fichiers midi.*
