Manipuler des fichiers MIDI par script groovy
=============================================

On souhaite parfois effectuer des manipulations de fichiers MIDI pour effectuer différentes opérations (transposition, comptage de notes, voir d'adéquation d'un morceau par rapport à une gamme d'instrument).

Le logiciel propose un ensemble de fonctions facilitant la manipulation des fichiers MIDI en quelques lignes de script (donc accessible par un non développeur). Ces scripts peuvent également être stockés dans la définition de l'instrument pour proposer des imports MIDI spécifiques.

Sommaire
--------

[Introduction](#introduction)

[Lecture d'un fichier Midi](#lecturefichiermidi)

[Filtrage du contenu d'un fichier midi](#filtrage)

[Analyse d'un fichier midi](#analyse)

[Création d'un script d'import MIDI pour un instrument]()

[]()Introduction
----------------

Le logiciel est implémenté en Java. Java propose des objets standards de manipulation de fichiers midi, cependant leur modification n'est pas très aisée du fait de la présence d'"Evènements" pouvant être liés. Par exemple les notes sont décrites par un évènement NoteOn puis un second évènement NoteOff. Les dates ou timestamp de début de notes ne sont pas codés en absolu (c'est à dire par rapport au début du morceau) mais en relatif. Chaque évènement est référencé dans le temps par rapport à l'évènement précédent (tick).

Des objets plus simples ont été mis en place pour permettre une manipulation plus simple des fichiers midi, du filtrage et de l'interprétation des éléments contenus dans le fichier. Des exemples suivent sur l'utilisation de ces objets, avec des exemples de mise en oeuvre.

[]()Lecture d'un fichier MIDI en 5 Lignes
-----------------------------------------

    import groovy.aprint.midi.*

    use (MidiCategory, MidiFileCategory)
    {
        def mf = new File("C:\\Users\\use\\Dropbox\\Midi MM\\LeBateauDeTahiti.mid").load()

    }

Le Résultat de la console affiche la collection d'évènements MIDI lus dans le fichier

[]()Filtrage d'un fichier Midi
------------------------------

Le bout de script suivant lit un fichier midi et filtre les notes du canal numéro 1

    import groovy.aprint.midi.*


    use (MidiCategory, MidiFileCategory)
    {
        def mf = new File("C:\\Users\\use\\Dropbox\\Midi MM\\LeBateauDeTahiti.mid").load()
        
        // filtrage des évènements associé au canal (1), cad 0 si l'on commence la numérotation à 0
        def resultatFiltrage = mf.filterChannel(0)

        // Ecriture dans un fichier midi de sortie
        resultatFiltrage.save(new File("c:\\temp\\test.mid"))

    }

Le résultat est un fichier MDI test.mid ne contenant que les évènements associés au canal 1. La fonction filterChannel filtre les évènements associés au canal concerné.

D'autres fonctions de filtrage sont disponibles :

<table style="width:10%;">
<colgroup>
<col width="0%" />
<col width="10%" />
</colgroup>
<thead>
<tr class="header">
<th>Fonction / Description</th>
<th>Exemple</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>filterMidiTrack</strong><br />

<p>Filtre les évènements MIDI associés à une piste dans le fichier midi</p></td>
<td><pre><code>import groovy.aprint.midi.*


use (MidiCategory, MidiFileCategory)
{
    def mf = new File(&quot;C:\\Users\\use\\Dropbox\\Midi MM\\LeBateauDeTahiti.mid&quot;).load()
    
    // filtrage des évènements associé au canal (1), cad 0 si l&#39;on commence la numérotation à 0
    def resultatFiltrage = mf.filterMidiTrack(0)

    // Ecriture dans un fichier midi de sortie
    resultatFiltrage.save(new File(&quot;c:\\temp\\test.mid&quot;))

}</code></pre></td>
</tr>
<tr class="even">
<td><strong>filter</strong>
<p>filtre générique pour filtrer le contenu avec une fonction utilisateur. Ceci permet de se faire sa propre fonction de filtrage.</p></td>
<td><pre><code>import groovy.aprint.midi.*


use (MidiCategory, MidiFileCategory)
{
    def mf = new File(&quot;C:\\Users\\use\\Dropbox\\Midi MM\\LeBateauDeTahiti.mid&quot;).load()
    
    // filtrage des évènements associé au canal (1), cad 0 si l&#39;on commence la numérotation à 0
    def resultatFiltrage = mf.filter { evt -&gt;
        if (evt.hasProperty(&quot;midiNote&quot;))
        {
            // on ne garde que les notes supérieures à 250ms
            if (evt.length &gt; 250000)
            {
                return true // on la garde
            }
        }
        
        return false
    }

  
   

}</code></pre></td>
</tr>
</tbody>
</table>

[]()Fonctions d'évaluation du fichier midi
------------------------------------------

Il est parfois intéressant de pouvoir évaluer les notes présentes dans le fichier MIDI pour effectuer une comparaison avec la gamme et permettre l'évaluation de transposition.

Des fonctions ont été ajoutées pour cela.

### listDistinctNotes()

Cette fonction permet de lister les notes distinctes d'un fichier midi

    import groovy.aprint.midi.*


    use (MidiCategory, MidiFileCategory)
    {
        def mf = new File("C:\\Users\\use\\Dropbox\\Midi MM\\LeBateauDeTahiti.mid").load()
        
        // filtrage des évènements associé au canal (1), cad 0 si l'on commence la numérotation à 0
       
       def notes = mf.listDistinctNotes()

       notes.each { note ->
           println note
       }
       

    }

Le résultat affiche ceci :

    >> start script execution
    E3
    G3
    A3
    C4
    D4
    E4
    A4
    B4
    C5
    D5
    E5
    F#5
    G5
    A5
    A#5
    B5
    C6
    C#6
    D6
    E6
    F#6
    G6
    A6
    A#6
    B6
    C7
    C#7
    D7
    E7

Ces notes sont les notes rencontrées dans le fichier MIDI

### int\[\] listTracks()

Cette fonction permet de lister les pistes d'un fichier MIDI

    import groovy.aprint.midi.*


    use (MidiCategory, MidiFileCategory)
    {
        def mf = new File("C:\\Users\\use\\Dropbox\\Midi MM\\LeBateauDeTahiti.mid").load()
        
        // filtrage des évènements associé au canal (1), cad 0 si l'on commence la numérotation à 0
       
       def tracks = mf.listTracks()  

       tracks.each { track ->
           println track
       }
       

    }

Le résultat affiché est le suivant :

    >> start script execution
    1
    2
    3
     

     Script executed in  0: 0:846 

Les pistes sont identifiées par rapport à un numéro, c'est le numéro présent dans le fichier MIDI. Le nom de la piste est ensuite contenu dans un évènement associé à la piste.

### countDistinctNotes()

Cette fonction est particulièrement intéressante pour analyser la répartition des notes dans un ensemble de notes. Cette fonction retourne par note, le nombre d'occurence de la note dans le groupe.

    import groovy.aprint.midi.*


    use (MidiCategory, MidiFileCategory)
    {
        def mf = new File("C:\\Users\\use\\Dropbox\\Midi MM\\LeBateauDeTahiti.mid").load()
        
        // filtrage des évènements associé au canal (1), cad 0 si l'on commence la numérotation à 0
       
       def dnotes = mf.countDistinctNotes()

       dnotes.each { note, nombre ->
           println "" + note + " - " + nombre + " fois"
       }
       

    }

Le résultat est le suivant :

    >> start script execution
    E6 - 61 fois
    C5 - 190 fois
    E5 - 69 fois
    C6 - 103 fois
    G5 - 82 fois
    E7 - 29 fois
    G6 - 151 fois
    D7 - 89 fois
    F#5 - 137 fois
    D5 - 336 fois
    A6 - 101 fois
    D6 - 182 fois
    A5 - 84 fois
    F#6 - 114 fois
    C7 - 70 fois
    B6 - 109 fois
    B5 - 93 fois
    A#6 - 5 fois
    A#5 - 1 fois
    D4 - 110 fois
    G3 - 82 fois
    B4 - 165 fois
    E4 - 5 fois
    C#6 - 7 fois
    C#7 - 6 fois
    A3 - 13 fois
    C4 - 20 fois
    E3 - 124 fois
    A4 - 26 fois

Outil de transformation de fichiers MIDI en carton
--------------------------------------------------

Il est possible à partir du fichier midi d'effectuer une transformation en carton, la transformation commence par la lecture du fichier midi, en fonction de la gamme et de la capacité de l'instrument, certaines notes, percussions ou registres sont convertis en trous.

L'association entre les deux peut être réalisé à la main en script, en parcourant les notes du fichier midi et en créant les trous dans le carton virtuel. Une autre façon plus évoluée et décrite ici permet de créer des associations entre les notes midi et les pistes du carton, les trous sont alors créés automatiquement en fonction des temps et des longueurs des notes dans le fichier MIDI.

    // exemple simple de script d'import de fichier midi
    import groovy.aprint.midi.*
    import groovy.aprint.transform.*



    use (MidiCategory, MidiFileCategory, NoteCategory, ScaleCategory)
    {
        def mf = new File("C:\\Users\\use\\Dropbox\\Midi MM\\LeBateauDeTahiti.mid").load()
        
        def ins =  services.repository.getInstrument("27 / 29 Flutes")
        def scale = ins.scale   
        def sh = scale.helper
        def t = mf.transformFor(scale)
       
        // on associe la note "D5" à la piste de la gamme ayant la note D5
        t.map("D5".note, sh.find("D5"))
        
        def result = t.doConvert()

        services.newVirtualBook(result.virtualbook, ins)

    }
