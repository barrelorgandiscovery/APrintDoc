Description de la fonction d'Export DXF
=======================================

Patrice Freydiere - 04/01/2014

Introduction
------------

Cette extension permet l'export d'un carton au format DXF pour une perforation avec une machine LASER.

Description de l'export
-----------------------

L'export du carton réalisé exporte le resultat dans un fichier au format DXF.

Le Format DXF est un format CAD permettant la construction de plan industriels, et très utilisés pour es machines à commandes numériques. Ce format est un fichier TEXTE permettant de décrire les traits.

Le fichier DXF est divisé en calques. Les calques permettent de regroupper un ensemble de traits ensemble, le calque peut être affiché ou masqué en fonction des besoins. Ceci permet de pouvoir mettre dans le plan certains éléments ensembles.

L'export propose deux modes de fonctionnement : un export pour les orgues mécaniques et un export pour les orgues pneumatiques. le traitement du carton est différent suivant ces deux cas d'utilisation.

Export Pour les cartons mécaniques
----------------------------------

L'export pour les cartons mécaniques ne modifie pas le carton, le carton est pris tel quel et les trous presents dans le cartons, sont dessinés au format carré dans le fichier DXF. Il n'y a pas de mise en place de ponts ou de réduction de la taille de trous.

Export pour les cartons pneumatiques
------------------------------------

L'export en mode pneumatique effectue des modifications sur le carton, car les instruments pneumatiques utilisent un support papier. Le support papier accepte mal les trous longs, fragilisant le support. Il y a donc dans ce cas une transformation réalisée sur le "carton", pour transformer les trous longs en une serie de trous. La transformation est décrite ci dessous :

![](localizedresources/fr/SchemaTransformationPneumatique.png)

Le trou d'origine du carton est découpé en petit trous séparés par des ponts. La taille des trous et la dimension des ponts est paramétré dans l'export.

Deux cas peuvent se présenter pour l'export des fins de trous, le schema ci dessous montre les deux cas possibles:

![](localizedresources/fr/SchemaTransformationPneumatique_dernier_trou.png)

Un paramètre d'export 'Pas de pont s'il reste' permet la non création d'un pont et d'un trou à la fin si la taille du trou restant est inférieure au paramètre.

Ainsi, si la taille du dernier trou est supérieure au paramètre, on se situe dans le cas 1 du schema ci dessus

Si la taille du dernier trou est inférieure au paramètre, on se situe dans le cas numero 2 du schema ci dessus.

Paramètres de l'export
----------------------

L'export propose les paramètres suivants :

![](localizedresources/fr/PerfoDXFparametres.png)

<table>
<caption>Description des paramètres</caption>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sortie pour orgue mécanique</strong></td>
<td><p>Ce paramètre propose une sortie au format Mécanique ou Pneumatique</p>
<p>Ce paramètre est important car il influe sur le resultat de sortie, et prends d'autres paramètre associés, comme : la taille des trous, la dimension des ponts, et &quot;pas de pont s'il reste ..&quot;.</p>
<p>Taille de trous (pour le cas pneumatique)</p></td>
</tr>
<tr class="even">
<td>Dimension des ponts</td>
<td>Dans le cas de l'export en mode pneumatique, ce paramètre définit la taille des ponts entre les petits trous créés.</td>
</tr>
<tr class="odd">
<td>Pas de pont s'il reste</td>
<td>Dans le cas ou le trou restant est intérieur à la dimension donnée, le trous précédent est agrandi et il n'y a pas de ponts créés.</td>
</tr>
<tr class="even">
<td>Taille page carton</td>
<td>Dans le fichier DXF, des traits sont créés pour permettre la création des plis (coupés à mi-chair). Ces traits sont créés dan le fichier dans un calque dédié.</td>
</tr>
</tbody>
</table>

Résultat de l'export
--------------------

Le résultat de l'export est la création de deux fichiers DXF:

un fichier \_CARTON.DXF contenant les calques et le contenu suivant :

- Le bord du carton (BORDS\_CARTON) : contour uniquement du carton

- Les pliures recto (PLIURES) : pliures reco uniquement espacées de 2 \* la taille de la page du carton

- Les trous (TROUS) : les traits associés aux découpes des trous.

<img src="localizedresources/fr/dxf_resultat_carton.png" height="200" />

Un second fichier \_pliuresverso est egalement créé contenant les pliures verso, espacées de 2 \* la taille de la page du carton et décalé d'une page par rapport aux pliures recto.


