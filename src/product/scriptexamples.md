Scripts Samples
===============

Exemples de scripts
===================

Lister les instruments présents
-------------------------------

List instruments
----------------

Dans la console générale


       

    def repository = services.repository

    print repository

    def instruments = repository.listInstruments()
    instruments.each { print "" + it.name + "\n" }
       
       
      

lister tous les trous dans la console
-------------------------------------

list all holes in the console
-----------------------------

dans la console carton

in the book console

       
     

    virtualbook.holesCopy.each { 
       println("" + it)
    }

    void
      
      
      

deplacer les trous selectionnés de 10 mm
----------------------------------------

move selected hole by 10 mm
---------------------------

dans la console carton

in the book console

       
     

    import org.barrelorgandiscovery.virtualbook.*

    def c = pianoroll.selectionCopy

    pianoroll.clearSelection()

    c.each { 
        virtualbook.removeHole(it)
        def h = new Hole(it.track, + virtualbook.scale.mmToTime(10) + it.timestamp, it.length)
        virtualbook.addHole(h)
        pianoroll.addToSelection(h)
    }

    void

      
      
      

Sélectionner les basses
-----------------------

Select the bass
---------------

dans la console carton

in the book console

       
     
    pianoroll.clearSelection()
    def holes = virtualbook.holesCopy
    def basses = virtualbook.scale.findNoteDefTrack("BASSE")
    holes.each { 
        if (it.track in basses)
        {
            pianoroll.addToSelection(it)
        }
    }
    void
      
      
      

Rechercher tous les trous supérieur à 20mm pour diviser leur longueur par 2
---------------------------------------------------------------------------

Search all holes greater than 20mm and divide its length by 2
-------------------------------------------------------------

dans la console carton

in the book console

       
      import org.barrelorgandiscovery.virtualbook.*

    pianoroll.clearSelection()

    def list=[]

    virtualbook.holesCopy.each { 
        
        if (virtualbook.scale.timeToMM(it.length) > 20)
        {
            virtualbook.removeHole(it)
            def h = new Hole(it.track, it.timestamp, (long)(it.length / 2))
            virtualbook.addHole(h)
            list.push(h)
        }

    }

    list.each {pianoroll.addToSelection(it)}

      
      
      

Créer une gamme de test pour un instrument
------------------------------------------

Create a test scale for an instrument
-------------------------------------


       
       
    import org.barrelorgandiscovery.scale.*;
    import org.barrelorgandiscovery.virtualbook.*;


    print services

    def r = services.repository

    def instrument = r.getInstrument("52 Touches FROR (Gamme Limonaire)")
    //def instrument = r.getInstrument("50 JazzBand Limonaire")

    if (instrument == null)
        throw new Exception("error, instrument not found")

    print "instrument name :" + instrument.name + "\n"

    def scale = instrument.scale

    def t = scale.tracksDefinition

    print "****************************************************"
    print "List all tracks definitions \n"


    print "getting the reset command keys"

    def resetkeys = []

    for (i in 0..t.length-1)
    {

        if (t[i] instanceof RegisterSetCommandResetDef)
            resetkeys.add(i)

     }


    def registerByPipeStops = [:]

    // pour chaque commande dans la gamme, on memorise les registres influent dessus ...

    for (i in 0..t.length-1)
    {
        def it = t[i]
        if (t[i] instanceof RegisterCommandStartDef)
        {
            print "adding " + it.registerSetName + " to " + t[i]
            if (! (registerByPipeStops[it.registerSetName]))
            {
                registerByPipeStops[it.registerSetName] = []
            }
            registerByPipeStops[it.registerSetName].add(["track" : i, "register":it.registerInRegisterSet])
        }
    }

    print "\n\n\nDone !"

    print registerByPipeStops

    def longueur = 1000000
    def smallNote = 100000

    def registerchangelength = 200000

    // create a new virtual book
    def v = new VirtualBook(scale)
    v.name = "Gamme " + instrument.name
     
     // position in the book
     def start = 100000
     
     // this function add a play note with repeated small note
     def addPlayNote = {int track ->
     
          v.addHole(new Hole(track,start,longueur))
          start += longueur + smallNote
          
          [0,1,2].each {
              v.addHole(new Hole(track,start,smallNote))
              start += 2*smallNote
          }
    }
     
     // this function activate a register
    def addRegisterChange = {int track->
          v.addHole(new Hole(track,start,registerchangelength))
          start += registerchangelength * 2
    }
     
    def addHoles = { rs -> 
         for(i in 0..t.length-1)
         {
             if (t[i] instanceof NoteDef)
             {
                 if (rs != null && t[i].registerSetName != rs )
                 {
                    continue
                 } 
                 addPlayNote(i)
             }
         }
    }
     
    addHoles(null);
     
    registerByPipeStops.each {

        // reset all the registers 

        resetkeys.each {
        
            def track = it
            
            v.addHole(new Hole(track, start, registerchangelength))
        
        }

        start += registerchangelength * 2


         def k = it.key
         it.value.each {
             print "" + k + "\n"
             addRegisterChange(it["track"])
             addHoles(k)
         }
    }
     
    // add the virtual book to aprint
    services.newVirtualBook(v,instrument)

    void
     
      

Ouvrir une fenêtre de sélection de répertoire
---------------------------------------------

Open a Directory Selection Frame
--------------------------------

dans la console carton ou la console générale

In the general console

    import groovy.aprint.tools.*

    new ChooseFolderFrame(action : { f-> print "Hello le répertoire sélectionné est : ${f}" }).show()

