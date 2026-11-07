#!/usr/bin/env python3
import json
vids = json.load(open('/workspace/videos.json'))
for v in vids:
    if v["i"] == "Lxb2-yTMZro": v["t"] = "Le Moyen Âge pour les enfants"

# compactage : clés courtes pour réduire le poids
packed = [{"i":v["i"],"t":v["t"],"c":v["c"],"d":v["d"],"m":v["m"],"th":v["th"],"lv":v["lv"]} for v in vids]

import prog as P
prog = P.PROG

tpl = open('/workspace/ecoletube/template.html', encoding='utf-8').read()
html = tpl.replace("__VIDEOS__", json.dumps(packed, ensure_ascii=False, separators=(",",":")))
html = html.replace("__PROGRAMME__", json.dumps(prog, ensure_ascii=False, separators=(",",":")))
open('/workspace/ecoletube/index.html','w',encoding='utf-8').write(html)
print("index.html", len(html), "octets |", len(packed), "vidéos")
