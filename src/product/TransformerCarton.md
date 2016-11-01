
Travailler avec les cartons en scripting
========================================


Introduction
------------

Il est fréquent de vouloir effectuer des transformations de fichiers midi / ou de cartons d'un instrument à un autre. Le langage de scripting d'APrint propose un ensemble de fonctions permettant de largement simplifier ces actions, nous présentons ci dessous des exemples d'utilisation de ces fonctions

    Nous considérons dans les exemples ci dessous que les actions sont réalisées dans une console de type "Quickscript", donc associée à un carton et ayant une variable "virtualbook" prédéfinie.

### Jouer avec la gamme d'un carton pour transformation

```
import groovy.aprint.transform.*
import org.barrelorgandiscovery.scale.*
import org.barrelorgandiscovery.tools.MidiHelper

use (NoteCategory, ScaleCategory, HoleCategory)
{
    def h = virtualbook.scale.helper

    println "nom de la gamme :" + virtualbook.scale.name
    println ""

    // jouons avec les notes
    
    Note n = "D3".note    // la note Re 3
    println n  // affiche D3
    println n+1 // affiche D#3
    
    println MidiHelper.localizedMidiLibelle(n.midiCode)  // Ré 3
    
    // on fait une collection de notes
    
    def listeNotes = ((48..62) as List).collect { index ->  new Note(midiCode: index) }
    println listeNotes // [C4, C#4, D4, D#4, E4, F4, F#4, G4, G#4, A4, A#4, B4, C5, C#5, D5]

    // transpose la liste des notes ... 
    println listeNotes.collect { it + 1 } // [C#4, D4, D#4, E4, F4, F#4, G4, G#4, A4, A#4, B4, C5, C#5, D5, D#5]
```

​        


        // liste des pistes du carton 
        println "Liste des pistes de la gamme " + h.tracks.join("\n")
        
     /*
    Resultat ---------------------------------------------------------
     
    Liste des pistes de la gamme Track no 0 -> PercussionDef - 35 fixed length : 6.0 retard : 6.0
    Track no 1 -> PercussionDef - 35 fixed length : 6.0 retard : 6.0
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
    Track no 44 -> PercussionDef - 35 fixed length : 6.0 retard : 6.0
    Track no 45 -> PercussionDef - 81 fixed length : 4.0 retard : 4.0
    Track no 46 -> null
    Track no 47 -> org.barrelorgandiscovery.scale.RegisterCommandStartDef@4c2849
    Track no 48 -> org.barrelorgandiscovery.scale.RegisterSetCommandResetDef@1e8f2a0
    Track no 49 -> org.barrelorgandiscovery.scale.RegisterCommandStartDef@90f19c
    Track no 50 -> org.barrelorgandiscovery.scale.RegisterCommandStartDef@1e67280
    Track no 51 -> org.barrelorgandiscovery.scale.RegisterCommandStartDef@675039
    
    Fin Resultat ---------------------------------------------------------
    */
      
        // liste des registres possibles
        println  ""
        println "Différents Registres : " + h.registerSets.keySet().join("\n")
      
    /*
    Resultat ---------------------------------------------------------
    
    Différents Registres : bass
    accompagnement
    melody
    counterMelody
    melody3
    
    Fin Resultat ---------------------------------------------------------
    */
      
        println ""
        println "Liste des notes des basses : " + h.tracks(h.bass.notes, h.bass.name).join("\n")
      
      /*
       Resultat ---------------------------------------------------------
    
    Liste des notes des basses : Track no 35 -> NoteDef - 53 - BASSE
    Track no 36 -> NoteDef - 52 - BASSE
    Track no 37 -> NoteDef - 50 - BASSE
    Track no 38 -> NoteDef - 48 - BASSE
    Track no 39 -> NoteDef - 59 - BASSE
    Track no 40 -> NoteDef - 58 - BASSE
    Track no 41 -> NoteDef - 57 - BASSE
    Track no 42 -> NoteDef - 55 - BASSE
    
    Fin Resultat ---------------------------------------------------------
    */
      
        println ""
        println "Recherche la piste du Do dans les basses : " + h.trackWithoutOctave("D3".note,h.bass.name)
      
      // Recherche la piste du Do dans les basses : Track no 37 -> NoteDef - 50 - BASSE


​      
        println ""
        println "Liste les pistes de percussion " + h.percussionTracks.join("\n")
        
        /*
         Resultat ---------------------------------------------------------
    
        Liste des pistes de percussion Track no 0 -> PercussionDef - 35 fixed length : 6.0 retard : 6.0
    Track no 1 -> PercussionDef - 35 fixed length : 6.0 retard : 6.0
    Track no 44 -> PercussionDef - 35 fixed length : 6.0 retard : 6.0
    Track no 45 -> PercussionDef - 81 fixed length : 4.0 retard : 4.0
    
    Fin Resultat ---------------------------------------------------------
    */
        
        println ""
        println "Liste des pistes de commande de registres " + h.registerTracks.join("\n")
    /*
     Resultat ---------------------------------------------------------
    
    Liste des pistes de commande de registres Track no 47 -> org.barrelorgandiscovery.scale.RegisterCommandStartDef@4c2849
    Track no 48 -> org.barrelorgandiscovery.scale.RegisterSetCommandResetDef@1e8f2a0
    Track no 49 -> org.barrelorgandiscovery.scale.RegisterCommandStartDef@90f19c
    Track no 50 -> org.barrelorgandiscovery.scale.RegisterCommandStartDef@1e67280
    Track no 51 -> org.barrelorgandiscovery.scale.RegisterCommandStartDef@675039
    
    Fin Resultat ---------------------------------------------------------
    */
    
        /////////////////////////////////////////////////////////////////////////////
    
        // transformation de cartons
        
        def ins  = services.repository.getInstrument("Raffin 27 / 29 t Simplifie")
    
        // création d'un objet TransformHelper (cf documentation Groovy)
        def t = h.transformFor(ins.scale)
        def d = ins.scale.helper
        
        // on fait la correspondance entre les basses et les basses trouvées dans le 27/29, en montant d'un demi ton
    
        def pistesnotesbasse = h.tracks(h.bass.notes, h.bass.name) 
        println "Piste des notes de basse origine : " +  pistesnotesbasse.join("\n")
        /*
         Resultat ---------------------------------------------------------
        Piste des notes de basse origine : Track no 35 -> NoteDef - 53 - BASSE
    Track no 36 -> NoteDef - 52 - BASSE
    Track no 37 -> NoteDef - 50 - BASSE
    Track no 38 -> NoteDef - 48 - BASSE
    Track no 39 -> NoteDef - 59 - BASSE
    Track no 40 -> NoteDef - 58 - BASSE
    Track no 41 -> NoteDef - 57 - BASSE
    Track no 42 -> NoteDef - 55 - BASSE
     Fin Resultat ---------------------------------------------------------
    */


        def notesBasseOrigineDontOnAjouteUnTon = h.bass.notes.collect { it + 2 }
        println notesBasseOrigineDontOnAjouteUnTon.join("\n")
        /*
         Resultat ---------------------------------------------------------
        G4
    F#4
    E4
    D4
    C#5
    C5
    B4
    A4
    Fin Resultat ---------------------------------------------------------
    */
        
        def nonTrouvee = t.map( pistesnotesbasse, d.tracks(notesBasseOrigineDontOnAjouteUnTon as Note[] ,null ))
    
        def result = t.transform(virtualbook) // on transform le carton, result contient le carton transformé et la liste des erreurs de transcriptions
        services.newVirtualBook(result.virtualbook, ins); // affiche le carton dont on a 
        
        println " Erreurs de transcription : " + result.untransposedholes.size()
        //  Erreurs de transcription : 3748


        void
    }


