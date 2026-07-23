#!/usr/bin/env python3
"""Rejoue les controles de l'audit du 22-07 sur le depot et un projet.

usage: python3 _scripts/verifie.py            # controles depot seuls
       python3 _scripts/verifie.py p06        # depot + projet

Controles depot :
  renvois casses vers des fichiers inexistants
  tirets cadratins et demi-cadratins
  longueur d'ETAT.md, 20 lignes max

Controles projet (pXX) :
  completude ligne a ligne des deux bilans finaux
  sous-sections ### dupliquees dans un meme bloc ##
  derive de structure entre _template/ et pXX/
  part de lignes barrees dans 11-a-verifier.md
  doublons d'entrees, compares sur la paire `francais` . `english`,
  jamais l'anglais seul : `setTimeout` et `git add --patch` portent
  chacun deux notions distinctes, un test sur l'anglais seul les
  signalerait a tort.

Ne modifie aucun fichier. Code retour 1 si au moins un echec.
"""
import os
import re
import sys

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

BLOCS = ["00-cadrage.md", "01-journal.md", "02-bugs.md", "03-connaissances.md",
         "04-choix-techniques.md", "05-bilan.md", "06-git.md", "07-synthese.md",
         "08-soutenance.md", "09-memo.md", "10-point-de-reprise.md",
         "11-a-verifier.md"]

# Fichiers jamais controles : archives brutes et sorties generees.
# Les archives v1 a v7 ne se modifient jamais, inutile de les signaler.
def exclu(chemin):
    rel = os.path.relpath(chemin, BASE).replace("\\", "/")
    if "/_deltas/" in rel or rel.startswith("_deltas/"):
        return True
    if re.search(r'prompt-oc-v[1-7]\.md$', rel):
        return True
    if os.path.basename(rel).startswith("99-"):
        return True
    return False

def fichiers_md():
    out = []
    for racine, dossiers, noms in os.walk(BASE):
        dossiers[:] = [d for d in dossiers if d not in (".git", "node_modules")]
        for n in noms:
            if n.endswith(".md"):
                c = os.path.join(racine, n)
                if not exclu(c):
                    out.append(c)
    return sorted(out)

def lire(chemin):
    with open(chemin, encoding="utf-8") as f:
        return f.read()

def rel(chemin):
    return os.path.relpath(chemin, BASE).replace("\\", "/")

ECHECS = []

def resultat(nom, problemes, info=""):
    if problemes:
        print(f"[ECHEC] {nom} · {len(problemes)} probleme(s)")
        for p in problemes[:40]:
            print("    " + p)
        if len(problemes) > 40:
            print(f"    ... et {len(problemes) - 40} autres")
        ECHECS.append(nom)
    else:
        suffixe = f" · {info}" if info else ""
        print(f"[OK]    {nom}{suffixe}")

# ---------------------------------------------------------------- depot

def controle_renvois():
    """Renvoi casse : un nom de fichier .md/.py/.sh cite en `code` qui
    n'existe nulle part. Ignores : les motifs generiques (pXX, NN, AAAA),
    les contre-exemples ("pas de", "jamais"), les lignes barrees (deja
    resolues) et les fichiers designes comme vivant dans un autre depot
    ("depot du projet")."""
    noms_connus = set()
    for racine, dossiers, noms in os.walk(BASE):
        dossiers[:] = [d for d in dossiers if d != ".git"]
        noms_connus.update(noms)
    motif = re.compile(r'`([\w./ -]+?\.(?:md|py|sh))`')
    problemes = []
    for f in fichiers_md():
        for i, l in enumerate(lire(f).split("\n"), 1):
            if re.search(r'\b[Pp]as de\b|\bjamais\b', l):
                continue
            if l.lstrip().startswith(("~~", "- ~~")) or "dépôt du projet" in l:
                continue
            for tok in motif.findall(l):
                if re.search(r'XX|NN|AAAA|MM-JJ', tok):
                    continue
                if "/" in tok:
                    ok = (os.path.exists(os.path.join(BASE, tok)) or
                          os.path.exists(os.path.join(os.path.dirname(f), tok)))
                else:
                    ok = tok in noms_connus
                if not ok:
                    problemes.append(f"{rel(f)}:{i} → `{tok}` introuvable")
    resultat("Renvois vers des fichiers", problemes)

def controle_cadratins():
    problemes = []
    for f in fichiers_md():
        for i, l in enumerate(lire(f).split("\n"), 1):
            n = l.count("—") + l.count("–")
            if n:
                problemes.append(f"{rel(f)}:{i} · {n} tiret(s)")
    resultat("Tirets cadratins et demi-cadratins", problemes)

def controle_etat():
    chemin = os.path.join(BASE, "ETAT.md")
    if not os.path.exists(chemin):
        resultat("ETAT.md, 20 lignes max", ["ETAT.md absent"])
        return
    lignes = lire(chemin).rstrip("\n").split("\n")
    n = len(lignes)
    problemes = [f"ETAT.md fait {n} lignes"] if n > 20 else []
    resultat("ETAT.md, 20 lignes max", problemes, f"{n} lignes")

# ---------------------------------------------------------------- projet

def sections(texte):
    """Decoupe un bloc en sections ## → liste de (titre, [lignes])."""
    lignes = texte.split("\n")
    idx = [i for i, l in enumerate(lignes) if l.startswith("## ")]
    out = []
    for n, s in enumerate(idx):
        e = idx[n + 1] if n + 1 < len(idx) else len(lignes)
        out.append((lignes[s][3:].strip(), lignes[s + 1:e]))
    return out

def brut(s):
    """Normalise pour la recherche : sans decor markdown, blancs replies."""
    s = s.replace("\\|", "|")
    for ch in "`*|":
        s = s.replace(ch, " ")
    return " ".join(s.split())

def contenu_utile(ligne):
    """Extrait le contenu comparable d'une ligne source, None si la ligne
    n'est que de la structure (vide, ---, separateur de tableau, titre).
    Une etiquette en gras (`- **Cause** ·`) est retiree : la version
    lisible garde la valeur, pas l'etiquette."""
    s = ligne.strip()
    if not s or s == "---" or s.startswith("<!--"):
        return None
    if re.fullmatch(r'[|\s:. -]+', s):
        return None
    if s.startswith("#"):
        return None
    s = re.sub(r'^>\s*', '', s)
    s = re.sub(r'^([-*]|\d+\.)\s*', '', s)
    s = re.sub(r'^\[[ xX~]\]\s*', '', s)
    m = re.match(r'\*\*(.+?)\*\*\s*[·:.]?\s*(.+)', s)
    if m:
        s = m.group(2)
    s = brut(s)
    return s if len(s) >= 4 else None

def controle_completude(P):
    """Aucune ligne des blocs sources ne doit manquer aux deux finaux.
    Exclusions volontaires cote lisible : la section `État Git` de
    06-git.md, et le bloc Formule quand il porte la sentinelle
    `Non applicable`. Les titres sont exclus, le lisible les renomme."""
    dossier = os.path.join(BASE, P)
    final = os.path.join(dossier, "99-bilan-final.md")
    lisible = os.path.join(dossier, "99-bilan-final-lisible.md")
    if not (os.path.exists(final) and os.path.exists(lisible)):
        resultat("Completude des bilans finaux",
                 [f"bilans absents de {P}/, lancer build-final.sh et build-lisible.py"])
        return

    lignes_final = set(l.strip() for l in lire(final).split("\n"))
    meule_lisible = brut(lire(lisible).replace("\n", " "))

    manque_final, manque_lisible = [], []
    for bloc in BLOCS:
        chemin = os.path.join(dossier, bloc)
        if not os.path.exists(chemin):
            continue
        texte = lire(chemin)
        for i, l in enumerate(texte.split("\n"), 1):
            if l.strip() and l.strip() not in lignes_final:
                manque_final.append(f"{P}/{bloc}:{i} · {l.strip()[:70]}")
        for titre, corps in sections(texte):
            if bloc == "06-git.md" and titre == "État Git":
                continue
            if titre.startswith("📐") and "Non applicable" in "\n".join(corps):
                continue
            for l in corps:
                utile = contenu_utile(l)
                if utile and utile not in meule_lisible:
                    manque_lisible.append(f"{P}/{bloc} ({titre}) · {utile[:70]}")
    resultat("Completude de 99-bilan-final.md", manque_final)
    resultat("Completude de 99-bilan-final-lisible.md", manque_lisible)

def controle_h3_dupliques(P):
    problemes = []
    for bloc in BLOCS:
        chemin = os.path.join(BASE, P, bloc)
        if not os.path.exists(chemin):
            continue
        for titre, corps in sections(lire(chemin)):
            vus = {}
            for l in corps:
                if l.startswith("### "):
                    nom = l[4:].strip()
                    vus[nom] = vus.get(nom, 0) + 1
            for nom, n in vus.items():
                if n > 1:
                    problemes.append(f"{P}/{bloc} · ## {titre} · ### {nom} × {n}")
    resultat("Sous-sections ### dupliquees", problemes)

def controle_derive(P):
    """Chaque bloc du projet doit porter les memes sections ## que son
    modele dans _template/. 08-soutenance.md peut etre absent, le
    template le prevoit. Une section en plus est signalee aussi : un
    bloc supplementaire se propose a Max, il ne s'ajoute pas en silence."""
    problemes = []
    for bloc in BLOCS:
        modele = os.path.join(BASE, "_template", bloc)
        projet = os.path.join(BASE, P, bloc)
        if not os.path.exists(modele):
            continue
        if not os.path.exists(projet):
            if bloc != "08-soutenance.md":
                problemes.append(f"{P}/{bloc} absent")
            continue
        t = set(titre for titre, _ in sections(lire(modele)))
        p = set(titre for titre, _ in sections(lire(projet)))
        for titre in sorted(t - p):
            problemes.append(f"{P}/{bloc} · ## {titre} manquant")
        for titre in sorted(p - t):
            problemes.append(f"{P}/{bloc} · ## {titre} en plus du template")
    resultat("Derive entre _template/ et " + P + "/", problemes)

def controle_barrees(P):
    """Une ligne barree doit vivre dans la section Resolu (## ou ###),
    jamais dans l'actif. La part de lignes barrees est une mesure."""
    chemin = os.path.join(BASE, P, "11-a-verifier.md")
    if not os.path.exists(chemin):
        resultat("Lignes barrees de 11-a-verifier.md", [],
                 "fichier absent")
        return
    texte = lire(chemin)
    parts = re.split(r'^#{2,3}\s+Résolu\s*$', texte, flags=re.M)
    actif, resolu = parts[0], parts[1] if len(parts) > 1 else ""

    def entrees(t):
        out = []
        for l in t.split("\n"):
            s = l.strip()
            if not s or s == "---" or s.startswith(("#", ">")):
                continue
            out.append(re.sub(r'^[-*]\s*', '', s))
        return out

    ea, er = entrees(actif), entrees(resolu)
    barrees_actif = [s for s in ea if s.startswith("~~")]
    n_barrees = len(barrees_actif) + len([s for s in er if s.startswith("~~")])
    total = len(ea) + len(er)
    part = f"{n_barrees}/{total} barrees" if total else "vide"
    problemes = [f"{P}/11-a-verifier.md · barree hors ## Résolu : {s[:70]}"
                 for s in barrees_actif]
    resultat("Lignes barrees de 11-a-verifier.md", problemes, part)

def controle_doublons_paires(P):
    """Doublon d'entree : la meme paire `francais` · `english` deux fois
    dans la meme section ## d'un bloc. La comparaison porte sur la paire
    entiere, jamais sur l'anglais seul. Elle se fait par section : une
    paire expliquee dans 🧠 et cataloguee dans 📚 n'est pas un doublon,
    les deux sections ont des roles distincts."""
    problemes = []
    motif = re.compile(r'`([^`]+)`\s*·\s*`([^`]+)`')
    for bloc in BLOCS:
        chemin = os.path.join(BASE, P, bloc)
        if not os.path.exists(chemin):
            continue
        for titre, corps in sections(lire(chemin)):
            vues = {}
            for i, l in enumerate(corps, 1):
                if l.lstrip().startswith("~~"):
                    continue
                for paire in motif.findall(l):
                    vues.setdefault(paire, []).append(i)
            for (fr, en), lignes in vues.items():
                if len(lignes) > 1:
                    problemes.append(
                        f"{P}/{bloc} · ## {titre} · `{fr}` · `{en}` × {len(lignes)}")
    resultat("Doublons de paires francais · english", problemes)

# ---------------------------------------------------------------- main

def main():
    P = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"Depot : {BASE}")
    print()
    print("-- Controles depot --")
    controle_renvois()
    controle_cadratins()
    controle_etat()
    if P:
        if not os.path.isdir(os.path.join(BASE, P)):
            print(f"\nDossier {P}/ introuvable.")
            sys.exit(2)
        print(f"\n-- Controles projet {P} --")
        controle_completude(P)
        controle_h3_dupliques(P)
        controle_derive(P)
        controle_barrees(P)
        controle_doublons_paires(P)
    print()
    if ECHECS:
        print(f"{len(ECHECS)} controle(s) en echec.")
        sys.exit(1)
    print("Tous les controles passent.")

if __name__ == "__main__":
    main()
