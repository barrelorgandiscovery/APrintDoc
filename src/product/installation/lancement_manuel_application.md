# Lancement APrint à partir d'un shell

*Patrice Freydiere - Juillet 2020*

APrint Studio peut être lancé en ligne de commande, ceci permet : 

- de pouvoir avoir des informations supplémentaires dans la console en cas de problèmes rencontrés

- de régler finement les versions de java utilisées (dans le cas où il y a plusieurs java installés sur le système)

- de définir son mode de fonctionnement et l'organisation des fichiers aprint sur son disque

  

### Vérification des prérequis

Vérifiez le prérequis : Java 8, (le logiciel fonctionne également sur des versions plus recentes, des travaux sont en cours pour valider le fonctionnement sur les versions actuelles de java). 

Cette version de java est intégrée dans l'installeur windows, cependant pour les autres plateformes (linux, mac), il faudra vous la procurer par ailleurs.

Nous n'avons testé fortement les logiciels **que** pour la version 8 de Java. Si vous utilisez une version plus recente, contactez nous.



Pour vérifier la version installée, à partir d'un shell, lancez la commande :

```
java -version
```

  Le résultat doit afficher, la version 8 de java, comme ci dessous

```
java version "1.8.0_112"
Java(TM) SE Runtime Environment (build 1.8.0_112-b15)
Java HotSpot(TM) 64-Bit Server VM (build 25.112-b15, mixed mode)
```



**Nota :** 

Dans le cas où vous avez une version de java dans un répertoire dédié, et que cette version n'est pas dans le PATH courant du système, vous pouvez positionner les variables d'environnement pour aller chercher cette version en préférentiel, comme suit (dans cet exemple, le chemin de java est /opt/java8):

```
export JAVA_HOME=/opt/java8
export PATH=$JAVA_HOME:$PATH
```

en procedant ainsi, le test ci dessus `java -version` doit fonctionner et retourner alors la bonne version.



## Lancement d'aprint, à partir de java

Pour lancer APrint en ligne de commande, c'est la ligne suivant qui est appelée :

```
java -Xmx4g -server -cp aprint.jar org.barrelorgandiscovery.gui.aprintng.APrintApplicationBootStrap
```

Cette ligne de commande :

- Indique où est le **fichier** aprint.jar , via l'option **-cp**

- l'option **-Xmx4g** indique que l'on "restreint" l'application à 4go de mémoire, si vous en avez plus, vous pouvez augmenter ce paramètre
- **org.barrelorgandiscovery.gui.aprintng.APrintApplicationBootStrap** est le nom de la classe de lancement de l'application
- L'option **-Dmainfolder=$HOME** est facultative et peut être ajoutée, cette option, permet d'indiquer à aprint où mettre les fichiers d'instruments, les scripts .. etc, si cette option n'est pas indiquée, c'est le "home" de l'utilisateur qui est pris. Cette option permet également de pouvoir installer "cote à cote" le logiciel pour tester différentes configuration ou version, sans impacter les autres.



L'application se lance alors, 

Dans le cas d'exception (message d'erreur) dans la console, ceux ci sont généralement explicite, nous pouvons aider à décoder les paramètres.



Pour plus d'informations sur java et les options de lancement, vous pouvez allez sur ce lien : https://docs.oracle.com/javase/8/docs/technotes/tools/windows/java.html