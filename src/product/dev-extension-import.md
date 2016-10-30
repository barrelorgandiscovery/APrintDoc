
Developpement d'une extension d'import de fichier MIDI
======================================================



Les extensions d'imports Java, permettent d'enrichir les méthodes de conversion d'un fichier MIDI vers un fichier BOOK.

Plusieurs interfaces peuvent être développées pour permettre l'ajout d'une fonction d'import MIDI en fichier BOOK.


Interfaces JAVA à implémenter
-----------------------------

Ce fichier, une fois dans le répertoire du profil utilisateur, est chargé au démarrage de l'application.

L'interface ImportersExtensionPoint ci dessous doit être implémentée :

```java
/**
 * This extension point permit the extension to implement a custom midi Reading
 * transformation
 * 
 * @author Freydiere Patrice
 * 
 */
public interface ImportersExtensionPoint {

  /**
   * Get the MidiImporter associated to an instrument scale
   * 
   * @param destinationscale
   *            the destination scale
   * @return an array list of midi importers
   */
  public ArrayList<AbstractMidiImporter> getExtensionImporterInstance(
  Scale destinationscale);

}
```

L'interface permet à l'extension de déclarer en fonction d'une gamme d'instruments les objets d'import pouvant être utilisés pour la conversion de MIDI vers BOOK.


Implémentation d'un objet d'import MIDI
---------------------------------------

L'implémentation d'un objet d'import MIDI passe par l'implémentation de l'interface AbstractMidiImporter

```java
/**
 * Transposition directe à partir d'un fichier midi ...
 * 
 * @author Freydiere Patrice
 */
public abstract class AbstractMidiImporter extends AbstractTransformation {

public abstract String getDescription();

public abstract MidiConversionResult convert(MidiFile midifile);

}
```


​    

La propriété getDescription retourne le texte indiqué dans la conversion possible. La méthode convert effectue la conversion du fichier midi et retourne un objet resultat. Cet objet resultat contient deux membres :

```java
/**
 * Bag for getting conversion + associated problems
 * 
 * @author use
 * 
 */
public class MidiConversionResult {

/**
 * The result
 */
public VirtualBook virtualbook;

/**
 * The associated problems linked to the conversion
 */
public ArrayList<MidiConversionProblem> issues;

}
```

Le premier membre virtualbook est le carton lui même converti,
le membre issues contient les erreurs potentiellement rencontrée lors de la conversion et permet à l'utilisateur de pouvoir consulter la liste des erreurs à corriger pour une bonne conversion en carton.


Paramétrage de la conversion
----------------------------

Il est parfois demandé lors de la conversion des paramètres supplémentaires, ces paramètres permettent de régler la conversion et proposer différentes alternatives lors de la transformation.

Deux interfaces peuvent être ajoutées à l'implémentation de l'objet AbstractMidiImporter :

-   CustomImporterParameters : celle ci permet à l'extension de saisir de façon libre les paramètres (une méthode est appelée lors de la demande des paramètres de conversion)
-   ImporterParameters : cette méthode permet de ne pas à avoir à implémenter la saisie des paramètres, mais confie au logiciel la saisie des paramètres en fournissant uniquement une description (BeanInfo). les paramètres saisie alors par l'utilisateur sont transmises à l'extension en utilisant la méthode setParameterToUse. L'extension peut alors récupérer et utiliser les paramètres de conversion.

**Définition de l'interface CustomImporterParameters :**

```java
public interface CustomImporterParameters {

	void showCustomImporterParameters() throws Exception;

}
```

**Définition de l'interface ImporterParameters :**

```java
/**
 * Interface defining the parameters associated to an import, if defined, aprint
 * ask for the parameters and inform the importer of the parameters
 * 
 * @author Freydiere Patrice
 * 
 */
public interface ImporterParameters {

/**
 * Get the bean that define the parameters of the importer
 * 
 * @return
 */
public Object getParametersInstanceBean();

/**
 * Set the parameters to use in the import
 * 
 * @param parameters
 */
public void setParametersToUse(Object parameters);

}
```
