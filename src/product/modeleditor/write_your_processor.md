# Ecrire son processeur

*Patrice Freydiere - 2018*

Il peut manquer des fonctionnalités dans le model editor, ceci n'est pas un probleme. Le scripting permet d'étendre ses capacités en intégrant la brique manquante.

Cette extensibilité nécessite quelques compétences en informatique, 



## Le processeur Script



Situé dans la palette:

![](scriptprocessor.png)



Le processeur script, est un processeur prenant en configuration le petit programme définissant :

- les paramètres d'entrée et de sortie
- la fonction a executer dans le modèle



Ci dessous un exemple de programme définissant un processeur :



```groovy
import org.barrelorgandiscovery.model.steps.scripts.*;
import org.barrelorgandiscovery.model.*;
import org.barrelorgandiscovery.virtualbook.*
import org.barrelorgandiscovery.xml.*

import java.io.File;

class T extends ModelGroovyScript {
   
   def console
   
   ModelParameter[] configureParameters() {
       [ newParameter(true,"fichier book",newJavaType(File.class)), 
         newParameter(false,"book",newJavaType(VirtualBook.class))]
   }

   Map execute(Map m) {
       console.println("hello :")
       console.println(m)
       return [book:VirtualBookXmlIO.read(m["fichier book"]).virtualBook]
   }

}
new T(console:out)
```

L'exemple ci dessus montre comment lire un fichier .book en utilisant les fonctions d'APrint Studio. 

## Fonctionnement

Le script retourne à sa sortie (dernière ligne), une classe définissant le processeur, 

deux méthodes sont à implémenter :

- configureParameters : cette fonction retourne la liste des paramètres qui sont configurés en entrée et en sortie
- execute : cette fonction est appelée lors de l'execution du processeur



