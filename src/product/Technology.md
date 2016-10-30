Eléments et choix pour la construction du logiciel APrint
=========================================================

Langage et plate-forme de construction du logiciel
--------------------------------------------------

Ce logiciel est construit en utilisant le langage Java et la plate-forme Java pour plusieurs raisons :

-Le langage Java est le plus utilisé dans le monde, des millions de développeurs participent à cette plate-forme et développe dans ce langage.

-Ce langage est spécifié et plusieurs constructeur de logiciels proposent des implémentations (des implémentations open source existent également, permettant d'assurer une pérennité importante des développements réalisés sur cette plate-forme).

-La plate-forme Java est une des plus ouvertes, un logiciel développé en Java peut être exécuté sous Windows, Linux, Mac OS.

Choix dans le design du logiciel
--------------------------------

Le logiciel a été construit en essayant de pouvoir l'utiliser sur le plus grand nombre de plates-formes et sans dépendance avec un matériel spécifique.

Nous avons donc conservé dans les différentes versions du logiciel une indépendance vis-à-vis de certaines cartes son ou librairie spécifiques à un ordinateur. Pour l'instant aucune accélération matérielle n'est utilisée, cela apporte ,certes, peut-être une lenteur sur des ordinateurs les moins récents mais nous permet de voir le proposer à tous.

D'autre part nous avons choisi de construire APrint sans utiliser de plate-forme visuelle.les plates-formes visuelles de type netbean ou eclipse peuvent apporter beaucoup en termes d'ergonomie cependant le cycle de vie de ses projets est très rapide et il est difficile de s'adapter et de suivre les évolutions aussi rapidement. Utilisation d'une telle plate-forme crée également une dépendance importante pour un logiciel qui vivra quelques dizaines d'années. Nous avons opté pour quelque chose de plus rudimentaire et simple.

Orienté objet
-------------

Nous avons opté pour une conception objet, nous permettons de pouvoir décliner certains entrepôts d'instruments ou décliner certains types d'instruments. Cette conception nous permet d'être malléable dans les extensions pouvant être proposée dans le logiciel ou s'adapter à des types d'instruments non prévus initialement.

La partie graphique est également été conçue en composant. Ceci permet la construction d'assistant ou d'écran pouvant réutiliser tout ou partie du logiciel simplement.

Logiciels open source
---------------------

La licence GPL nous a tout de suite convaincu pour ce type de logiciel, cette licence permet de conserver les libertés de l'utilisateur tout en interdisant une quelconque restriction sur ses liberté. pour plus d'informations sur la licence vous pouvez consulter le site Web de la FSF.

Cette licence permet d'adapter ou de corriger le programme librement en fonction de ses besoins.

Plusieurs librairies de développement ont peut-être intégré à ce projet grâce à cette licence.
