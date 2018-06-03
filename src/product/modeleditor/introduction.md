# Introduction au model editor

Le model editor vous permet d'effectuer des traitements sur les cartons ou les fichiers midi. Il rends plus simple l'import d'un fichier midi particuier, ou propose une façon visuelle d'effectuer des traitements sur les cartons (par exemple, changer le carton de gamme).

![](modeleditor.png)



## Les débuts

Le modèle editor repose sur des processeur, proposant des traitements. Chaque processeur effectue un traitement.

![](step.png)



Les processeurs prennent en entrée des paramètres, et fournissent des sorties. Dans l'exemple ci dessus, le processeur prends en entrée un fichier midi et fournit des listes de notes, classées par code midi.

Les boites de traitements (processeurs), sont configurables. L'accès à la configuration du processeur est réalisable par un double click souris. Ce paramétrage permet de spécifier la gamme de l'instrument, ou d'autres paramètres pouvant faire varier les entrées et les sorties.

Ci dessous un exemple de processeur permettant de transformer une succession de notes ou de trous, en un carton d'orgue de barbarie.

![](concentrator_template.png)



![](concentrator.png)

![](concentrator_parameters.png)

Lorsque configuré le processeur affiche les notes de la gamme, pour permettre des connexions en entrée.

![](concentrator_configured.png)



# Premiers pas

Nous allons voir dans cette section, comment réaliser un premier modèle.



![](modeleditor_screen.png)

L'écran propose sur la gauche une palette de processeur et sur la droite la construction du modèle.

La première étape consiste à prendre l'élément "Midi File Reading" et le faire glisser sur la zone du modèle.

![](step1_dragdrop.png)

une fois dans la zone, le processeur propose ses entrées par défaut, il est possible d'observer les paramètres de configuration en double clickant sur le processeur.

![](step2_configure.png)



Ce processeur prends en entrée un fichier midi et propose en sortie une liste d'évènements MIDI (les notes + d'autres informations).

pour alimenter l'entrée en fichier midi, on utiliser le processeur input.

![](input_processor.png)

Ce processeur permet de paramétrer le modèle en spécifiant des paramètres d'entrée ou de sortie. Lorsqu'il est placé dans le modèle, ce processeur propose un type "chaine de caractère" dans sa configuation.  Le changement du type de parmètre en "fichier" permettra de pouvoir sélectionner un fichier, puis de pouvoir connecter les deux éléments.

![](input_parameters.png)



![](step3_file.png)

La connection des deux boites est réalisée en glissé déposé depuis la sortie, comme ci dessous :

![](step4_connect.png)

Les évènements Midi sont alors disponibles pour permettre la conversion en Carton.



La transformation en carton est réalisée en utilisant le processeur "Concentrator", celui ci accepte en entrée des évènements de notes midi, ou des notes de carton.

![](step5_concentrator.png)

Une fois disposé dans le modèle, il est possible par configuration de choisir la gamme de l'instrument, ce qui fait apparaitre l'ensemble des entrées.

![](step6_configure.png)



![](step7_inputs.png)



Encore faut il envoyer les bonnes notes Midi sur la bonne piste, une boite va alors nous intéresser : le Midi Distributor. Cette boite permet de répartir les notes midi et nous permet de connecter les notes midi sur le carton.

![](step8_model.png)

On connecte alors, La sortie du midi à l'entrée du "Midi Distributor". Puis on peut connecter les pistes midi aux pistes du carton.

Pour afficher le resultat, un processeur est ensuite ajouté pour permettre l'affichage du resultat, dans une fenetre de type "carton" dans APrint Studio.

![](step9_open_virtualbook.png)

Un seul paramètre est nécessaire : le nom de l'instrument (que l'on indique comme précédemment dans la configuration, accessible par double click).

![](step10_fin.png)



Le modèle est terminé, et il est possible de l'executer.

![](step10_execute.png)



La console en bas à gauche permet de suivre l'execution et informe sur les possibles erreurs.

![](step10_execute2.png)



Le résultat de la lecture s'affiche dans une nouvelle fenetre.

![](result.png)



Voici comment en quelques click , il est possible de faire une lecture personnalisée d'un fichier midi, pour le convertir correctement en carton.



