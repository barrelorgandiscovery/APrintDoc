Travailler avec les fichiers midi en scripts
============================================

Introduction
------------

L'Environnement groovy permet de travailler sur le contenu des fichiers midi. Cette manipulation de fichier midi permet de retravailler le contenu des fichiers midi, et de mieux les adapter aux capacités de l'instrument d'orgue de barbarie.

En effet, certains fichiers midi sont utilisés comme "commande" pour piloter des instruments midifiés, par exemple certaines notes ou evenements n'ont rien à voir avec la musique elle même, mais plus sur des commandes ayant été cablées sur des notes de musiques.

La notion de carton virtuel est donc ici pour permettre une description adaptée de la musique avec les notions prises en charge par les instruments d'orgue de barbarie (registres, percussions ... etc ..)

Deux approches sont disponibles avec le logiciel :

-   Transformer le fichier midi en carton virtuel
-   Transformer le fichier midi pour un autre instrument

Nous presenterons dans la suite, la méthode simplifiée, le dernier chapitre précisera comment revenir à une utilisation plus rigoureuse du fichier midi.

### Lire un fichier midi en scripting

un ensemble d'objet permettent de lire et écrire le contenu d'un fichier midi de façon simplifiée, ces outils simplifiées ne donne pas accès à l'ensemble des possibilités du midi mais permettent de couvrir beaucoup de cas d'utilisation

L'objet **MidiFileIO** du package **org.barrelorgandiscovery.virtualbook.transformation.importer** permet d'effectuer des lecture et écriture de fichiers midi

la méthode "**read**" permet la lecture du fichier midi.

    import org.barrelorgandiscovery.virtualbook.transformation.importer.*

    def folder = new File("C:\\Documents and Settings\\pfr\\midi")

    def fichier_original = "A tous les filles.mid"

    def m = MidiFileIO.read(new File(folder, fichier_original))

    -- ou directement avec les noms de répertoires / fichiers --

    def m = MidiFileIO.read(new File("c:\\mes documents\\midi.mid"))

Le script ci dessus retourne dans la variable **m** un objet **MidiFile** contenant la liste des éléments du fichier midi

ci dessous le resultat de la console après éxécution du programme

     
    >> start script execution
     

     Script executed in  0:10:828 

    >>  MidiFile 
    MidiNote piste:0, Channel : 15Timestamp:80645Note Midi:0Longueur:173387
    MidiNote piste:0, Channel : 15Timestamp:673387Note Midi:0Longueur:173387
    MidiNote piste:0, Channel : 15Timestamp:782258Note Midi:4Longueur:153225
    MidiNote piste:0, Channel : 15Timestamp:842741Note Midi:121Longueur:96775
    MidiNote piste:0, Channel : 15Timestamp:875000Note Midi:122Longueur:68548
    MidiNote piste:0, Channel : 15Timestamp:907258Note Midi:116Longueur:96774
    MidiNote piste:0, Channel : 4Timestamp:967742Note Midi:100Longueur:112903
    MidiNote piste:0, Channel : 6Timestamp:967742Note Midi:93Longueur:120967
    MidiNote piste:0, Channel : 6Timestamp:967742Note Midi:88Longueur:125000
    MidiNote piste:0, Channel : 15Timestamp:782258Note Midi:13Longueur:370967
    MidiNote piste:0, Channel : 15Timestamp:782258Note Midi:14Longueur:379032
    MidiNote piste:0, Channel : 15Timestamp:778225Note Midi:12Longueur:383065
    MidiNote piste:0, Channel : 4Timestamp:1088709Note Midi:90Longueur:76613
    MidiNote piste:0, Channel : 15Timestamp:842741Note Midi:6Longueur:322581
    MidiNote piste:0, Channel : 6Timestamp:1169354Note Midi:92Longueur:72581
    MidiNote piste:0, Channel : 4Timestamp:1209677Note Midi:93Longueur:120968
    MidiNote piste:0, Channel : 4Timestamp:1209677Note Midi:98Longueur:125000
    MidiNote piste:0, Channel : 4Timestamp:1209677Note Midi:102Longueur:125000
    MidiNote piste:0, Channel : 1Timestamp:967742Note Midi:38Longueur:463709
    MidiNote piste:0, Channel : 15Timestamp:1391129Note Midi:117Longueur:96774
    ......

L'environnement de script affiche le contenu de l'objet MidiFile retourné

### Manipulation du fichier midi ...

l'objet MidiFile est une collection d'objet **MidiNote** qui peut être manipulée directement.

exemple de parcours de la liste des notes



    m.each { 

        println "Note : " +  it.midiNote + " Channel : " + it.channel + " track : " + it.track + " debut : " + it.timeStamp + " longueur : " + it.length
    }

On parcours ici, l'ensemble des notes, en affichant le code midi, le "channel" de restitution, et le track , le timing de début de la note (timestamp) en microseconde et la longueur de la note en microseconde.

Les propriétés de chaque note peuvent être modifiées comme suit.

    m.each { 

        it.midiNote = it.midiNote + 12    

    }

Ici nous rajoutons une octave à chaque note (une octave est constituée de 12 demis tons)

### Enregistrement du fichier midi

une fois l'objet **MidiFile** modifié, il est possible de l'enregistrer. la méthode "**write\_midi\_0**" de l'objet **MidiFileIO** permet d'enregistrer le resultat dans un fichier midi au format Midi 0

    def m = MidiFileIO.read(new File(folder, fichier_original))

    m.each { 


        it.midiNote = it.midiNote + 12    

    }

    MidiFileIO.write_midi_0(m, new File("c:\\monnouveaufichier.mid"))

Le fichier "**monnouveaufichier.mid**" a ete sauvegardé.

### Outils supplémentaires pour la manipulation des fichiers midi

D'autre outils sont disponibles pour faciliter la manipulation de fichiers midi.

La classe **MidiHelper** permet de faciliter la manipulation des notes

ci dessous un exemple d'utilisation des différentes méthodes :


    import org.barrelorgandiscovery.tools.*

    println "getMidiNote :" + MidiHelper.getMidiNote(34)

    println "midiLibelle :" + MidiHelper.midiLibelle(34)

    println "midiCode " + MidiHelper.midiCode("C#3")

    println "getOctave " + MidiHelper.getOctave(35)


L'execution de ce script retourne :

    >> start script execution
    getMidiNote :A#
    midiLibelle :A#2
    midiCode 37
    getOctave 2
     

     Script executed in  0: 0: 47
    >>  (null) returned from evaluation

### Aller plus loin dans l'utilisation fine Midi à partir de l'API Standard Java

L'environnement java contient un modèle objet associé à l'utilisation des fichier midi, ceci est porté par le package javax.sound.midi des exemples sont disponible dans le javadoc associé à l'API Java
