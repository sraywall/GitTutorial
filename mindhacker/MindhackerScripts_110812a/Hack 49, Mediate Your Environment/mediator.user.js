// ==UserScript==
// @name          Mediator
// @namespace     http://ron.ludism.org/
// @description   Web mediation script from Mindhacker
// @include       *
// ==/UserScript==
// Based on a script from Greasemonkey Hacks by Mark Pilgrim, copyright © 2006 O’Reilly Media, Inc. All rights reserved. Used with permission.

var arReplacements =
{
"LOL": "<laughter>",
"ROTFLMAO": "<laughter>",
"ROTFLMFAO": "<laughter>",
":-D": "<laughter>",
"[HAha]{4,}": "<laughter>"
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
