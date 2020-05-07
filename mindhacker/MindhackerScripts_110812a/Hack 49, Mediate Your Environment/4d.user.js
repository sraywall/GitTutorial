// ==UserScript==
// @name          4D
// @namespace     http://ron.ludism.org/
// @description   4D website mediation script
// @include       *
// ==/UserScript==
// Based on a script from Greasemonkey Hacks by Mark Pilgrim, copyright © 2006 O’Reilly Media, Inc. All rights reserved. Used with permission.


var arReplacements =
{
"apos": "furthest ana",
"bionian": "2D being",
"bulk": "4D hypervolume",
"delta": "kata",
"flune": "4D hyperplane",
"glome": "4D hypersphere",
"gongyl": "4D ball",
"pentaspace": "5D space",
"planespace": "2D space",
"tetrealm": "4D hyperplane",
"tetrealmic": "4D",
"realmar": "3D",
"realmic": "3D",
"realmspace": "3D space",
"realm": "3D hyperplane",
"skring": "4D spring",
"sphone": "4D cone",
"surcell": "4D hypersurface",
"swock": "4D sheet",
"tesserobject": "4D object",
"tetracube": "tesseract",
"tetral": "4D",
"tetraspace": "4D space",
"tetronian": "4D being",
"trength": "spissitude",
"trionian": "3D being",
"upsilon": "ana",
"wint": "ana",
"zakos": "furthest kata",
"zant": "kata"
};
var arRegex = new Array();
for (var sKey in arReplacements) {
    arRegex[sKey] = new RegExp(sKey, 'g');
}

var snapTextNodes = document.evaluate("//text()[" +
    "not(ancestor::script) and not(ancestor::style)]",
    document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null);
for (var i = snapTextNodes.snapshotLength - 1; i >= 0; i--) {
    var elmTextNode = snapTextNodes.snapshotItem(i);
    var sText = elmTextNode.data;
    for (var sKey in arReplacements) {
        sText = sText.replace(arRegex[sKey], arReplacements[sKey]);
    }
    elmTextNode.data = sText;
}
