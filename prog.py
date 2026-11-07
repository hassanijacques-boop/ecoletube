# -*- coding: utf-8 -*-
C = {"Français":"#D9462F","Maths":"#23618F","Questionner le monde":"#31825A","Sciences":"#31825A",
     "Histoire":"#9B5320","Géographie":"#1F7A6C","EMC":"#65489B","Anglais":"#B93A73",
     "Arts":"#C98A12","Numérique":"#37496B","EPS":"#5B7C1F"}
E = {"Français":"📖","Maths":"🔢","Questionner le monde":"🌱","Sciences":"🔬","Histoire":"🏛️",
     "Géographie":"🗺️","EMC":"⚖️","Anglais":"🇬🇧","Arts":"🎨","Numérique":"💻","EPS":"🏃"}

def M(n, att, dom): return {"n":n,"e":E[n],"c":C[n],"att":att,"dom":dom}

PROG = {
"CP": {"short":"cycle 2","resume":"La grande année : apprendre à lire, à écrire, à compter. Tout se joue sur la régularité, pas sur la quantité.",
 "matieres":[
  M("Français","Lire seul un texte court et le comprendre ; écrire en cursive ; produire une phrase correcte.",[
    ("Langage oral","écouter, raconter, dire un poème, poser une question"),
    ("Lecture","syllabes, sons, déchiffrage, premiers textes"),
    ("Écriture","cursive, copie, dictée de syllabes et de mots"),
    ("Étude de la langue","la phrase, le nom, le verbe, le vocabulaire")]),
  M("Maths","Compter jusqu'à 99, additionner et soustraire, reconnaître les figures, se repérer dans l'espace.",[
    ("Nombres","0 à 99, dizaines et unités, comparer, ranger"),
    ("Calcul","additions et soustractions, doubles, premiers problèmes"),
    ("Grandeurs et mesures","longueurs, euros, dates et durées"),
    ("Espace et géométrie","se repérer, figures simples, solides"),
    ("Données","lire un tableau à double entrée")]),
  M("Questionner le monde","Se repérer dans le temps et dans l'espace, observer le vivant et la matière.",[
    ("Le temps","jour, semaine, mois, saisons, hier/aujourd'hui/demain"),
    ("L'espace","la classe, l'école, le quartier, le plan"),
    ("Le vivant","animaux, plantes, corps humain, hygiène"),
    ("La matière","les cinq sens, l'eau, les objets")]),
  M("EMC","Respecter les règles de la classe, nommer ses émotions, vivre avec les autres.",[
    ("Vivre ensemble","règles, politesse, respect, différence"),
    ("Soi et les autres","émotions, consentement, sécurité")]),
  M("Anglais","Comprendre et répéter des mots simples : se saluer, nommer les couleurs et les nombres.",[
    ("Oral","écouter, répéter, chanter"),
    ("Vocabulaire","salutations, couleurs, nombres de 1 à 10")]),
  M("Arts","Explorer les couleurs et les matières, chanter ensemble, tenir un rythme.",[
    ("Arts plastiques","traces, couleurs, collage, modelage"),
    ("Musique","comptines, rythme, écoute")]),
 ]},
"CE1": {"short":"cycle 2","resume":"On consolide la lecture et on entre vraiment dans le calcul posé et la production d'écrit.",
 "matieres":[
  M("Français","Lire environ 70 mots par minute, écrire trois ou quatre phrases, conjuguer au présent.",[
    ("Lecture","fluence, compréhension, textes plus longs"),
    ("Écriture","copie soignée, dictée, premiers textes"),
    ("Étude de la langue","nom, verbe, déterminant, phrase négative et interrogative"),
    ("Conjugaison","le présent des verbes en -er")]),
  M("Maths","Nombres jusqu'à 999, tables, addition posée, mesurer et comparer.",[
    ("Nombres","jusqu'à 999, centaines, comparer, ranger"),
    ("Calcul","tables, addition posée avec retenue, début de multiplication"),
    ("Grandeurs et mesures","longueurs (m, cm), lire l'heure"),
    ("Espace et géométrie","vocabulaire géométrique, figures, solides")]),
  M("Questionner le monde","Observer, comparer, décrire : le vivant, la matière, le temps long.",[
    ("Le vivant","dents, alimentation, croissance"),
    ("La matière","l'air, l'eau, les états"),
    ("Le temps et l'espace","frises, plans, paysages")]),
  M("EMC","Comprendre pourquoi il y a des règles, et ce qu'est un règlement.",[
    ("Vivre ensemble","règlement, droits et devoirs, entraide")]),
  M("Anglais","Comprendre des consignes simples et nommer ce qui entoure l'enfant.",[
    ("Oral","se présenter, compter, nommer les couleurs")]),
  M("Arts","Découvrir des œuvres, expérimenter des techniques, chanter.",[
    ("Arts plastiques","dessin, peinture, assemblage"),
    ("Musique","chants, instruments, écoute")]),
 ]},
"CE2": {"short":"cycle 2","resume":"L'année charnière : lecture fluide, production d'écrit autonome, et l'entrée dans l'histoire.",
 "matieres":[
  M("Français","Lire couramment, comprendre l'implicite, rédiger un texte court et le relire.",[
    ("Lecture","fluence, compréhension, lecture de consignes"),
    ("Écriture","rédaction courte, révision de son texte"),
    ("Étude de la langue","sujet-verbe, groupes, types de phrases"),
    ("Conjugaison","présent, imparfait, futur, passé composé"),
    ("Orthographe","accents, pluriel des noms, accords simples")]),
  M("Maths","Nombres jusqu'à 9 999, multiplication posée, fractions simples, géométrie.",[
    ("Nombres","jusqu'à 9 999, comparer, encadrer"),
    ("Calcul","multiplication posée, division simple, calcul mental"),
    ("Fractions","demi, quart, tiers"),
    ("Grandeurs et mesures","longueurs, masses, contenances, durées"),
    ("Espace et géométrie","angle droit, figures, symétrie")]),
  M("Questionner le monde","Matière, vivant, énergie : observer, expérimenter, expliquer.",[
    ("La matière","eau, air, mélanges, états"),
    ("Le vivant","chaînes alimentaires, régimes, cycles"),
    ("L'énergie et les objets","sources d'énergie, objets techniques")]),
  M("Histoire","La Préhistoire et l'apparition de l'écriture.",[
    ("La Préhistoire","premiers hommes, art pariétal, sédentarisation")]),
  M("Géographie","Mon espace proche, la France, les régions.",[
    ("Mon espace","quartier, commune, département, région"),
    ("La France","relief, villes, régions")]),
  M("EMC","Vivre ensemble dans une classe qui débat et qui décide.",[
    ("Vivre ensemble","règlement, conseil, respect, égalité")]),
  M("Anglais","Se présenter, compter jusqu'à 20, nommer les couleurs et la famille.",[
    ("Oral","présentation, nombres, couleurs")]),
  M("Arts","Regarder, décrire, expérimenter.",[
    ("Arts plastiques","couleurs, matières, techniques"),
    ("Musique","instruments, rythme, chant")]),
 ]},
"CM1": {"short":"cycle 3","resume":"On quitte le « lire pour apprendre à lire » : la lecture sert à apprendre. Grammaire, fractions, histoire.",
 "matieres":[
  M("Français","Identifier sujet, verbe et compléments ; conjuguer à trois temps ; écrire un récit de 10 à 15 lignes.",[
    ("Grammaire","sujet, verbe, compléments, groupe nominal, attribut"),
    ("Conjugaison","présent, imparfait, futur"),
    ("Orthographe","accord sujet-verbe, accords dans le groupe nominal"),
    ("Lecture","comprendre un texte narratif ou explicatif"),
    ("Écriture","récit, description, révision de son texte"),
    ("Lexique","synonymes, familles de mots, dictionnaire")]),
  M("Maths","Grands nombres, fractions, décimaux, division, proportionnalité, périmètre.",[
    ("Nombres","grands nombres, fractions, décimaux"),
    ("Calcul","multiplication et division posées, calcul mental"),
    ("Grandeurs et mesures","périmètre, longueurs, angles"),
    ("Espace et géométrie","droites, symétrie, polygones, solides"),
    ("Problèmes","résoudre un problème en plusieurs étapes")]),
  M("Sciences","La matière, le vivant, la Terre, l'énergie : une démarche, pas une leçon à réciter.",[
    ("La matière","états, mélanges, eau"),
    ("Le vivant","digestion, respiration, classification"),
    ("La Terre","volcans, séismes, activité interne"),
    ("L'énergie","circuits électriques")]),
  M("Histoire","De la Préhistoire à la fin du Moyen Âge.",[
    ("La Préhistoire","traces, premiers hommes"),
    ("L'Antiquité","Gaulois, Rome, romanisation"),
    ("Le Moyen Âge","châteaux, Charlemagne, guerre de Cent Ans")]),
  M("Géographie","Se repérer sur la Terre, habiter la France.",[
    ("Se repérer","lignes imaginaires, continents, océans"),
    ("La France","relief, villes, espaces")]),
  M("EMC","La République, ses symboles, la règle commune.",[
    ("La République","symboles, valeurs, laïcité"),
    ("Vivre ensemble","respect, conseil, égalité")]),
  M("Anglais","Se présenter, décrire, comprendre un court dialogue.",[
    ("Oral","se présenter, nombres, corps, couleurs")]),
  M("Arts","Techniques et histoire des arts.",[
    ("Arts plastiques","couleurs, portrait, composition"),
    ("Musique","instruments, rythme, chant")]),
  M("Numérique","Utiliser un ordinateur, chercher, commencer à programmer.",[
    ("Outils","ordinateur, fichiers, recherche"),
    ("Programmation","algorithme, Scratch")]),
 ]},
"CM2": {"short":"cycle 3","resume":"La dernière année du primaire : tout doit tenir debout seuls — lire, écrire, calculer, argumenter.",
 "matieres":[
  M("Français","Lire 120 mots par minute et comprendre, écrire un texte structuré de 15 lignes, maîtriser les accords.",[
    ("Grammaire","phrase complexe, propositions, pronoms, compléments"),
    ("Conjugaison","passé simple, plus-que-parfait, tous les temps"),
    ("Orthographe","accords, homophones, participe passé"),
    ("Lecture","texte littéraire et documentaire, implicite"),
    ("Écriture","lettre, dialogue, récit, révision de son texte"),
    ("Lexique","niveaux de langue, champ lexical, dictionnaire")]),
  M("Maths","Nombres jusqu'au milliard, décimaux, quatre opérations, proportionnalité, aires.",[
    ("Nombres","jusqu'au milliard, fractions, décimaux"),
    ("Calcul","4 opérations posées, calcul mental, proportionnalité, pourcentages, moyenne"),
    ("Grandeurs et mesures","unités et conversions, durées, aires"),
    ("Espace et géométrie","perpendiculaires, parallèles, symétrie, angles, solides, patrons"),
    ("Problèmes","problèmes à plusieurs étapes, justification")]),
  M("Sciences","Expliquer avec une démarche : vivant, Terre, énergie, environnement.",[
    ("Le vivant","reproduction, évolution, classification"),
    ("La Terre","système solaire, risques, climat"),
    ("L'énergie","sources, conversions, économies"),
    ("Environnement","développement durable, déchets, biodiversité"),
    ("Objets techniques","fonctionnement, conception")]),
  M("Histoire","De la Renaissance à l'Europe d'aujourd'hui.",[
    ("Temps modernes","Renaissance, Louis XIV, grandes découvertes"),
    ("Révolution et XIXe","1789, Napoléon, République, industrialisation"),
    ("XXe siècle","guerres mondiales, Shoah, Europe, décolonisation")]),
  M("Géographie","Habiter, se déplacer, communiquer ; la France dans le monde.",[
    ("Habiter","métropoles, espaces de vie"),
    ("Se déplacer","mobilités en France et en Europe"),
    ("Le monde","population, France dans le monde, outre-mer"),
    ("Risques","risques naturels et technologiques")]),
  M("EMC","La République, la démocratie, les droits, le harcèlement.",[
    ("La République","laïcité, symboles, valeurs"),
    ("Démocratie","vote, élections, engagement"),
    ("Droits","droits de l'enfant, égalité, lutte contre le harcèlement")]),
  M("Anglais","Niveau A1 : se présenter, décrire, raconter, comprendre.",[
    ("Oral","se présenter, dialogues, prononciation"),
    ("Vocabulaire","famille, vêtements, animaux, météo, maison, heure")]),
  M("Arts","Analyser une œuvre, produire, interpréter.",[
    ("Arts plastiques","portrait, couleur, composition"),
    ("Histoire des arts","œuvres et courants"),
    ("Musique","familles d'instruments, rythme, chant")]),
  M("Numérique","Chercher, vérifier, protéger, programmer.",[
    ("Internet","fonctionnement, dangers, esprit critique"),
    ("Programmation","algorithmes, Scratch"),
    ("Outils","ordinateur, traitement de texte")]),
 ]},
}

if __name__ == "__main__":
    import json
    json.dump(PROG, open("/workspace/prog.json","w"), ensure_ascii=False, indent=1)
    print("ok", sum(len(v["matieres"]) for v in PROG.values()))
