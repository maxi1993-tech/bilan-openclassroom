#!/usr/bin/env python3
"""Fusionne les sous-sections ### portant le meme nom dans un bloc ##.
Empeche l'empilement d'un '### Etape N' par delta.
usage: python3 _scripts/fusionne-sous-sections.py p06/03-connaissances.md"""
import re, sys, collections

def fusionne(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    h2 = [i for i, l in enumerate(lines) if l.startswith("## ")]
    # Garde-fou 1 : un fichier sans titre de niveau 2 serait vide en sortie.
    if not h2:
        print("ignore, aucun titre ## :", path)
        return
    # Garde-fou 2 : tout ce qui precede le premier ## (titre H1, preambule)
    # doit etre conserve, il etait supprime jusqu'ici.
    tete = lines[:h2[0]]
    out = list(tete)
    for n, s in enumerate(h2):
        e = h2[n+1] if n+1 < len(h2) else len(lines)
        bloc = lines[s:e]; titre = bloc[0]; corps = bloc[1:]
        h3 = [i for i, l in enumerate(corps) if l.startswith("### ")]
        if not h3:
            out += bloc; continue
        pre = corps[:h3[0]]
        g = collections.OrderedDict()
        for m, ss in enumerate(h3):
            ee = h3[m+1] if m+1 < len(h3) else len(corps)
            nom = corps[ss][4:].strip()
            contenu = corps[ss+1:ee]
            if not any(l.strip() for l in contenu):
                continue
            g.setdefault(nom, []).append(contenu)
        out.append(titre); out += pre
        for nom, morceaux in g.items():
            # Les '---' internes separent les entrees, CLAUDE.md les exige :
            # on les garde. Seul le '---' de fin de morceau est retire, il est
            # remis une seule fois a la couture entre deux morceaux fusionnes.
            c = []
            for m in morceaux:
                m = list(m)
                while m and not m[0].strip(): m.pop(0)
                while m and not m[-1].strip(): m.pop()
                if not m: continue
                if m[-1].strip() != "---": m += ["", "---"]
                if c: c.append("")
                c += m
            out += [f"### {nom}", ""] + c + [""]
        if out and out[-1].strip() != "---" and out[-2:] != ["---", ""]:
            out += ["---", ""]
    txt = re.sub(r'\n{3,}', '\n\n', "\n".join(out)).rstrip() + "\n"
    open(path, "w", encoding="utf-8").write(txt)
    print("fusionne:", path)

for p in sys.argv[1:]:
    fusionne(p)
