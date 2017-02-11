Création de fenêtres et d'interfaces Graphiques en Scripting
============================================================

GUI Creation using scripts
==========================

Lorsque l'on crée des scripts, il est plus aisé de proposer des fenêtres pour la saisie des paramètres et proposer aux utilisateurs une aide associée pour accélérer l'utilisation du logiciel.

Cet article montre comment ajouter des fenêtres dans un script APrint / APrint Studio.

Une première fenêtre
====================

Ci dessous un petit exemple d'utilisation de la fonction showFrame pour la création d'une fenêtre à partir d'un script. L'objet SwingBuilder permet la création de composants pouvant être ensuite utilisés dans des scripts. Les composant sont passés à la commande showFrame pour la création de la fenêtre. La fenêtre ici n'affiche qu'un label pour exemple.

    import groovy.aprint.tools.*
    import groovy.swing.*

    def sb = new SwingBuilder()

    def l = sb.label(text:"hello")

    def f = GUIHelper.showFrame(["Premier paramètre":l])
    f.pack()
    f.visible=true

Saisie de deux paramètres dans une fenêtre
==========================================

Ci dessous un second exemple de saisie de deux paramètres sous forme libre et utilisation de ceux ci dans une fonction

    import groovy.aprint.tools.*
    import groovy.swing.*

    def sb = new SwingBuilder()

    def t1 = sb.textField(text:"premier paramètre", columns:30)
    def t2 = sb.textArea(text:"second paramètre", columns:30, rows:20)
    def b = sb.button(label:"ok", actionPerformed : {  print "hello window" + t1.text + "-" + t2.text  })

    def f = GUIHelper.showFrame(["1":t1, "2" : t2], b)
    f.pack()
    f.visible=true

Ce second exemple ajoute un bouton en bas de la fenêtre, permettant d'afficher dans la console un message "hello window" et réutilise la valeur des paramètres ci dessus.


