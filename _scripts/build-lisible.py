#!/usr/bin/env python3
"""Version lisible du bilan -> 99-bilan-final-lisible.md
Reorganise et met en page. Ne reformule aucun mot de Max.
usage: python3 _scripts/build-lisible.py p06"""
import re, os, sys, datetime

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
P = sys.argv[1] if len(sys.argv) > 1 else "p06"
os.chdir(os.path.join(BASE, P))

def sections(path):
    if not os.path.exists(path): return {}
    lines = open(path, encoding="utf-8").read().split("\n")
    idx = [i for i, l in enumerate(lines) if l.startswith("## ")]
    d = {}
    for n, s in enumerate(idx):
        e = idx[n+1] if n+1 < len(idx) else len(lines)
        body = "\n".join(lines[s+1:e]).strip()
        d[lines[s][3:].strip()] = re.sub(r'\n---\s*$', '', body).strip()
    return d

S = {}
for f in ["00-cadrage.md","01-journal.md","02-bugs.md","03-connaissances.md",
          "04-choix-techniques.md","05-bilan.md","06-git.md","07-synthese.md",
          "08-soutenance.md","09-memo.md","10-point-de-reprise.md"]:
    S.update(sections(f))

verif = S.get("🔍 Vérification", "")
faits = len(re.findall(r'- \[x\]', verif, re.I)); total = len(re.findall(r'- \[[ x]\]', verif, re.I))
bugs  = len([l for l in S.get("🐛 Journal de bugs","").split("\n") if l.strip().startswith("- ")])
conn  = len([l for l in S.get("🧠 Nouvelles connaissances","").split("\n") if l.strip().startswith("- ")])
choix = len([l for l in S.get("🔍 Choix techniques","").split("\n") if l.strip().startswith("- ")])
todo  = S.get("✅ Todo","")
tf, tt = len(re.findall(r'- \[x\]', todo, re.I)), len(re.findall(r'- \[[ x]\]', todo, re.I))

def bugs_table(txt):
    out = []
    for l in txt.split("\n"):
        s = l.strip()
        if s.startswith("**") and s.endswith("**"):
            if out: out.append("")
            out += [f"### {s.strip('*')}", "", "| Bug observé | Cause réelle | Correction |", "| --- | --- | --- |"]
        elif s.startswith("- "):
            parts = [p.strip() for p in s[2:].split("→")]
            if len(parts) == 3:
                out.append("| " + " | ".join(p.replace("|", "\\|") for p in parts) + " |")
            else:
                out.append("| " + s[2:].replace("|", "\\|") + " | | |")
    return "\n".join(out)

D = datetime.date.today().isoformat()
p = []; A = p.append
A(f"""# {P.upper()}, bilan de projet

*Version lisible, générée le {D}. Réorganisée pour la lecture, contenu non reformulé.*
*Source : les blocs de `{P}/`. Ne pas éditer ce fichier, éditer les blocs.*

---

## En une page

| | |
| --- | --- |
| **Avancement todo** | {tf} / {tt} tâches |
| **Vérifications** | {faits} / {total} validées |
| **Bugs résolus et documentés** | {bugs} |
| **Connaissances acquises** | {conn} |
| **Décisions techniques justifiées** | {choix} |

---

## 1. Mission et périmètre
""")
A(S.get("🎯 Mission",""))
A("\n### Contraintes techniques\n"); A(S.get("🔧 Specs techniques",""))
A("\n### Ce qu'il fallait maîtriser\n"); A(S.get("🧗 Ce qu'il va falloir maîtriser sur ce projet",""))
A("\n---\n\n## 2. Décisions techniques\n")
A("> Format `décision → pourquoi`. C'est ce sur quoi le jury interroge en premier.\n")
A(S.get("🔍 Choix techniques",""))
f = S.get("📐 Formule et méthode de calcul","")
if f.strip() and "Non applicable" not in f:
    A("\n### Formule / méthode de calcul\n"); A(f)
A("\n---\n\n## 3. Ce que j'ai appris\n"); A(S.get("🧠 Nouvelles connaissances",""))
A("\n---\n\n## 4. Bugs, cause et correction\n")
A("> Lecture en trois temps : ce que j'ai vu, ce qui le causait vraiment, ce que j'ai changé.\n")
A(bugs_table(S.get("🐛 Journal de bugs","")))
A("\n---\n\n## 5. Mes explications\n")
A("> Rédigé avec mes mots, sans le code sous les yeux. Non reformulé.\n")
A("\n### Pseudocode\n"); A(S.get("🧩 Pseudocode",""))
A("\n### Explication ligne par ligne\n"); A(S.get("🗣️ Explication ligne par ligne",""))
A("\n---\n\n## 6. Ce que je maîtrise, ce qui reste\n"); A(S.get("🧭 Bilan technique (synthèse)",""))
A("\n### Théorie croisée mais non pratiquée\n"); A(S.get("📚 Théorie non pratiquée",""))
A("\n### Bilan pour la session mentor\n"); A(S.get("📋 Bilan, préparation session mentor",""))
A("\n---\n\n## 7. Questions pour le mentor\n"); A(S.get("❓ Questions pour le mentor",""))
A("\n---\n\n## 8. Tips et lexique\n"); A(S.get("💡 Tips","")); A("\n### Lexique\n"); A(S.get("📖 Lexique",""))
A("\n---\n\n## 9. Annexes\n")
A("\n### Todo détaillée\n"); A(todo)
A("\n### Vérifications\n"); A(verif)
A("\n### Validation outils\n"); A(S.get("📊 Validation outils",""))
A("\n### Commits\n"); A(S.get("Commit",""))
if S.get("🎤 Préparation soutenance","").strip():
    A("\n### Préparation soutenance\n"); A(S.get("🎤 Préparation soutenance",""))
A("\n### Point de reprise\n"); A(S.get("📝 Point de reprise",""))

open("99-bilan-final-lisible.md","w",encoding="utf-8").write("\n".join(p).rstrip()+"\n")
print("genere", P + "/99-bilan-final-lisible.md")
