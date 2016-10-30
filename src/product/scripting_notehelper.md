#Travailler en scripting avec les objets "Note"


Lorsque l'on manipule les fichiers MIDI ou lorsque l'on évalue un fichier MIDI pour le mettre en carton, on travaille souvent avec les notes en scripting.

Creer une note à partir d'une chaine de caractère.

```
import groovy.aprint.midi.*
import groovy.aprint.transform.*

use (NoteCategory)
{
    println "D5".note
}
```

Créer un tableau de note (une plage de note) à partir de deux notes

```
import groovy.aprint.midi.*
import groovy.aprint.transform.*

use (NoteCategory)
{       
    println "D5".note.to("D8".note)
}
```

les objets Note peuvent être modifiés avec un ajout de demis tons et moins de demis tons

```
import groovy.aprint.midi.*
import groovy.aprint.transform.*

use (NoteCategory)
{
    println "D5".note + 4 // ajout de 4 demis tons
    println "D5".note + 12 // ajout d'une octave
}
```



>
>   start script execution
>
>   F#5
>
>   [D5, D#5, E5, F5, F#5, G5, G#5, A5, A#5, B5, C6, C#6, D6, D#6, E6, F6, F#6, G6, G#6, A6, A#6, B6, C7, C#7, D7, D#7, E7, F7, F#7, G7, G#7, A7, A#7, B7, C8, C#8, D8]
>
>   Script executed in  0: 0: 85
>
> 