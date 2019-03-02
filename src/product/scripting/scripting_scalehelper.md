
Travailler en scripting avec le Scale Helper
============================================

Lorsque l'on manipule les fichiers MIDI, que l'on fait des transformations sur les cartons, il est parfois nécessaire de pouvoir travailler sur la définition de la gamme d'un instrument. Le scale helper permet de faire des recherches de notes dans une gamme ou de pistes assez aisément.

Celui ci permet de gagner beaucoup de temps dans les transformations ou transpositions d'un instrument à un autre.

Le scale helper est une category groovy ajoutant la propriété helper aux objet "scale" ou gamme. Ci dessous un exemple de mise en oeuvre :

    import groovy.aprint.transform.*
    import groovy.aprint.midi.*
    
    use (ScaleCategory) {
    
        def ins = services.repository.getInstrument("27 / 29 Flutes")
    
        def scaleHelper = ins.scale.helper
    
    
    }

Que peut-on alors demander au scale helper? Si l'instrument possède une définition de partie Basse / Accompagnement / Chant, il est possible d'avoir les informations suivantes :


Lister les pistes
-----------------

    import groovy.aprint.transform.*
    import groovy.aprint.midi.*
    
    
    use (ScaleCategory) {
    
        def ins = services.repository.getInstrument("52 Limonaire Origine")
    
        def scaleHelper = ins.scale.helper
    
        scaleHelper.tracks.each { println  it.toString() }
    
    }

On récupère la définition de la gamme :

    >> start script execution
    Track no 0 -> PercussionDef - 35 fixed length : 6.0 retard : 6.0
    Track no 1 -> PercussionDef - 35 fixed length : 6.0 retard : 4.0
    Track no 2 -> NoteDef - 89 - CHANT
    Track no 3 -> NoteDef - 88 - CHANT
    Track no 4 -> NoteDef - 86 - CHANT
    Track no 5 -> NoteDef - 85 - CHANT
    Track no 6 -> NoteDef - 84 - CHANT
    Track no 7 -> NoteDef - 83 - CHANT
    Track no 8 -> NoteDef - 82 - CHANT
    Track no 9 -> NoteDef - 81 - CHANT
    Track no 10 -> NoteDef - 80 - CHANT
    Track no 11 -> NoteDef - 79 - CHANT
    Track no 12 -> NoteDef - 78 - CHANT
    Track no 13 -> NoteDef - 77 - CHANT
    Track no 14 -> NoteDef - 76 - CHANT
    Track no 15 -> NoteDef - 75 - CHANT
    Track no 16 -> NoteDef - 74 - CHANT
    Track no 17 -> NoteDef - 73 - CHANT
    Track no 18 -> NoteDef - 72 - CHANT
    Track no 19 -> NoteDef - 71 - CHANT
    Track no 20 -> NoteDef - 70 - CHANT
    Track no 21 -> NoteDef - 69 - CHANT
    Track no 22 -> NoteDef - 68 - CHANT
    Track no 23 -> NoteDef - 67 - CHANT
    Track no 24 -> NoteDef - 66 - ACCOMPAGNEMENT
    Track no 25 -> NoteDef - 65 - ACCOMPAGNEMENT
    Track no 26 -> NoteDef - 64 - ACCOMPAGNEMENT
    Track no 27 -> NoteDef - 63 - ACCOMPAGNEMENT
    Track no 28 -> NoteDef - 62 - ACCOMPAGNEMENT
    Track no 29 -> NoteDef - 61 - ACCOMPAGNEMENT
    Track no 30 -> NoteDef - 60 - ACCOMPAGNEMENT
    Track no 31 -> NoteDef - 59 - ACCOMPAGNEMENT
    Track no 32 -> NoteDef - 58 - ACCOMPAGNEMENT
    Track no 33 -> NoteDef - 57 - ACCOMPAGNEMENT
    Track no 34 -> NoteDef - 55 - ACCOMPAGNEMENT
    Track no 35 -> NoteDef - 53 - BASSE
    Track no 36 -> NoteDef - 52 - BASSE
    Track no 37 -> NoteDef - 50 - BASSE
    Track no 38 -> NoteDef - 48 - BASSE
    Track no 39 -> NoteDef - 59 - BASSE
    Track no 40 -> NoteDef - 58 - BASSE
    Track no 41 -> NoteDef - 57 - BASSE
    Track no 42 -> NoteDef - 55 - BASSE
    Track no 43 -> null
    Track no 44 -> PercussionDef - 40 fixed length : 6.0 retard : 6.0
    Track no 45 -> PercussionDef - 81 fixed length : 4.0 retard : 4.0
    Track no 46 -> null
    Track no 47 -> org.barrelorgandiscovery.scale.RegisterCommandStartDef@fa385
    Track no 48 -> org.barrelorgandiscovery.scale.RegisterSetCommandResetDef@b88448
    Track no 49 -> org.barrelorgandiscovery.scale.RegisterCommandStartDef@1f4ba51
    Track no 50 -> org.barrelorgandiscovery.scale.RegisterCommandStartDef@1f45022
    Track no 51 -> org.barrelorgandiscovery.scale.RegisterCommandStartDef@b8fba5
    
    
     Script executed in  0: 1:  8 

Décrire les notes des sections de registres
------------------------------------------

Dans le cas où l'instrument dispose de section de registres, les informations peuvent être récupérées par section de registres.

    import groovy.aprint.transform.*
    import groovy.aprint.midi.*
    
    
    use (ScaleCategory, NoteCategory) {
    
        def ins = services.repository.getInstrument("52 Limonaire Origine")
    
        def scaleHelper = ins.scale.helper
    
        scaleHelper.bass.notes.each { println it }
    
        println "liste des pistes :"
    
        scaleHelper.bass.tracks.each { println it }
    }
    
    le resultat de la console affiche :

​     


    >> start script execution
    F4
    E4
    D4
    C4
    B4
    A#4
    A4
    G4
    liste des pistes :
    Track no 35 -> NoteDef - 53 - BASSE
    Track no 36 -> NoteDef - 52 - BASSE
    Track no 37 -> NoteDef - 50 - BASSE
    Track no 38 -> NoteDef - 48 - BASSE
    Track no 39 -> NoteDef - 59 - BASSE
    Track no 40 -> NoteDef - 58 - BASSE
    Track no 41 -> NoteDef - 57 - BASSE
    Track no 42 -> NoteDef - 55 - BASSE
    
    
     Script executed in  0: 0:343 

Rechercher une piste associée à une note
----------------------------------------

Il est possible de faire des recherches de notes sur la gamme :

    import groovy.aprint.transform.*
    import groovy.aprint.midi.*
    
    
    use (ScaleCategory, NoteCategory) {
    
        def ins = services.repository.getInstrument("52 Limonaire Origine")
    
        def scaleHelper = ins.scale.helper
    
        scaleHelper.track("C5".note)    
    
    }

Diverses autres variantes sont également disponibles pour effectuer des recherches. La fonction track peut prendre en paramètre la section de registre :

    import groovy.aprint.transform.*
    import groovy.aprint.midi.*
    
    
    use (ScaleCategory, NoteCategory) {
    
        def ins = services.repository.getInstrument("52 Limonaire Origine")
    
        def scaleHelper = ins.scale.helper
    
        // recherche d'un note dans la mélodie
        scaleHelper.track("C6".note, scaleHelper.MELODY) // on aurai pu mettre BASS ou ACCOMPAGNMENT, COUNTER_MELODY
    
    
    }

Le résultat de la console affiche :


    >> start script execution
​     

     Script executed in  0: 0: 63 
    
    >>  Track no 18 -> NoteDef - 72 - CHANT
