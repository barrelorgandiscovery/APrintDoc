# Implémentation d'un outil en script

Le scripting ne se limite pas à des transformations sur les cartons, mais peut permettre également de compléter l'écran par de nouveaux outils.

ci dessous est expliqué comment créer un nouvel outil, utilisable dans la fenetre de carton. Cet outil présenté propose un action de "Punch" pour faire des trous calibrés dans le carton.


<video width="600" controls="true" muted="true" autoplay="true">
   <source src="../tool_scripting_demo.mp4" type="video/mp4">
</video>

Cet outil montre le coup de poinçon donné sur le carton,
Les touches + et - permettent de régler la taille du poinçon


Le code source associé à l'outil

	import org.barrelorgandiscovery.gui.aedit.*
	import org.barrelorgandiscovery.virtualbook.*
	
	import javax.swing.*
	import java.awt.event.*
	import java.awt.*


	// JOptionPane.showMessageDialog(null,"Punch Tool Activated")
	
	class PunchTool extends Tool {
	
	    def pianoroll
	    
	    // position actuelle de la souris
	    // utilisé pour l'affichage du texte
	    Integer currentX
	    Integer currentY
	    
	    // taille du trou pour les coups de poinçons
	    double tailleTrou = 5.0
	    
	    // position courante sur le carton
	    // si null, on est pas dans une position connue sur la matrice du carton
	    def position
	    
	    def void activated() {
	       //  JOptionPane.showMessageDialog(null,"activated " + pianoroll)
	    }
	    
	    def void unactivated() {
	     // JOptionPane.showMessageDialog(null,"unactivated")
	    }
	    
	    def void paintElements(Graphics g) {
		if (position != null) { // on est sur une position dans le carton
		    position.track; // piste matchée
		    position.position; // timestamp, in micros
		    
		    // calcul de la position de la piste en mm
		    def axis = pianoroll.trackToMM(position.track)
		    def debut =  pianoroll.timeToMM(position.position)
		    
		    def scale = pianoroll.virtualBook.scale
		    def hauteurPiste = scale.intertrackHeight
		    g.drawRect(pianoroll.convertCartonToScreenX(debut ), 
			       pianoroll.convertCartonToScreenY(axis - hauteurPiste/2),
				pianoroll.MmToPixel(tailleTrou),
				pianoroll.MmToPixel(hauteurPiste))
		    g.drawString("" + tailleTrou + " mm" , currentX, currentY)
		}    
	    }
	    
	    def void mouseMoved(MouseEvent e) {
		  currentX = e.x
		  currentY = e.y
		  // on question pour savoir sur quelle piste on est
		  // et à quel horodatage dans le carton
		  position = pianoroll.query(e.x, e.y)
		  
		  // on demande le réaffichage pour que le dessin
		  // se fasse
		  pianoroll.repaint()
	    }
	   
	    def void mouseReleased(MouseEvent e) {
		if (position != null) {
		    try {
			// definition de la position du "trou", ou "matière à remettre sur le carton"
			def h = new Hole(position.track, position.position, pianoroll.MMToTime(tailleTrou))
			
			pianoroll.startEventTransaction();
			try {
			    def us = pianoroll.undoStack
			    us.push(new GlobalVirtualBookUndoOperation(pianoroll.virtualBook, "Undo Punch", pianoroll));
			       
			    if (e.button == MouseEvent.BUTTON1) {
				// on a clické sur le bouton gauche, on découpe le carton
				pianoroll.virtualBook.addAndMerge(h)                        
			    } else if (e.button == MouseEvent.BUTTON3) {
				// on a clické sur le bouton droit, on remet de la matière
				pianoroll.virtualBook.cutHoles(h)
			    }
			} finally {
			    pianoroll.endEventTransaction()
			}
			// pianoroll.repaint()
		    } catch(Throwable t) {
			    // en cas d'erreur, on l'affiche
			    JOptionPane.showMessageDialog(null,t.message)
		    }
		} // if position != null
	    }
	    
	    void keyTyped(KeyEvent e) {
		// on a appuyé sur une touche
		// JOptionPane.showMessageDialog(null,e.keyChar)
		if (e.keyChar == '+') {
		    tailleTrou = tailleTrou + 1
		    pianoroll.repaint()
		} else if (e.keyChar == '-') {
		    tailleTrou = tailleTrou -1
		    pianoroll.repaint()
		}
	    }
	}
	
	// création de l'outil
	def p = new PunchTool( pianoroll: pianoroll  );
	// activation de l'outil dans la fenetre
	pianoroll.setCurrentTool(p);



