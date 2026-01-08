---
layout: page
permalink: /ia-mobilite/vibe-workshop/
title: Atelier Vibe Coding - Créer avec l'IA
description: Atelier pratique pour découvrir le développement assisté par IA avec Mistral Vibe - Parfait pour les débutants en programmation
title-fr: Atelier Vibe Coding - Créer avec l'IA
lang: fr
page_id: vibe-workshop
---

# 🎨 Atelier Vibe Coding : Votre Premier Projet Web avec l'IA

**Bienvenue dans l'ère du développement assisté par intelligence artificielle !** Cet atelier vous guidera pas à pas pour créer votre premier site web avec l'aide de **Mistral Vibe**, même si vous n'avez **aucune expérience en programmation**.

**🎯 Objectifs de l'atelier :**
- Comprendre comment fonctionnent les assistants IA pour le développement
- Créer un site web fonctionnel pour présenter votre projet
- Apprendre à collaborer efficacement avec Mistral Vibe
- Découvrir les possibilités de l'IA pour l'ingénierie et la mobilité

**📚 Public cible :** Étudiants en ingénierie automobile sans expérience en programmation

---

## 🤖 Comprendre Mistral Vibe et ses Capacités

### **1. Qu'est-ce que Mistral Vibe ?**

Mistral Vibe est un **assistant de développement piloté par IA** qui peut vous aider à :

- **Écrire du code** dans différents langages (HTML, CSS, JavaScript, Python, etc.)
- **Créer des structures de projets** automatiquement
- **Générer des designs web** et des prototypes
- **Analyser des données** et créer des visualisations
- **Automatiser des tâches répétitives** de développement

**💡 Comment ça marche ?** Vous décrivez ce que vous voulez en langage naturel, et Mistral Vibe génère le code correspondant !

### **2. Cas d'utilisation pour votre projet**

**Pour cet atelier, nous allons nous concentrer sur :**

| Domaine | Exemples de tâches | Avantages pour vous |
|---------|-------------------|-------------------|
| **Développement Web** | Créer des pages HTML, ajouter du CSS, JavaScript | Présenter votre projet professionnellement |
| **Prototypage** | Créer des maquettes, tester des idées rapidement | Visualiser vos concepts avant développement |
| **Analyse de données** | Traiter des données de mobilité, créer des graphiques | Analyser des données réelles de transport |
| **Automatisation** | Générer du code répétitif, créer des scripts | Gagner du temps sur les tâches techniques |

**🎓 Pourquoi c'est important pour vous ?**
- **Gagnez du temps** : Concentrez-vous sur vos idées, pas sur la syntaxe
- **Apprenez progressivement** : L'IA vous guide et explique le code
- **Prototypage rapide** : Testez des concepts en quelques minutes
- **Préparation professionnelle** : Ces outils sont utilisés dans l'industrie

---

## 🛠️ Configuration de Votre Environnement

### **1. Suivez le Guide d'Installation**

Avant de commencer, assurez-vous que tout est installé :

👉 **[Guide Mistral Vibe - Configuration Complete](/ia-mobilite/guide-mistral-vibe/)**

**Ce que vous devez avoir :**
- ✅ Python 3.8+ installé
- ✅ Mistral Vibe configuré
- ✅ Votre clé API Mistral AI (gratuite pour les étudiants)
- ✅ Un terminal fonctionnel (PowerShell, Terminal, ou iTerm2)

### **2. Testez Votre Configuration**

Ouvrez un terminal et vérifiez que tout fonctionne :

```bash
# Vérifiez que Mistral Vibe est accessible
mistral-vibe --version

# Vérifiez que votre clé API est configurée
echo $MISTRAL_API_KEY  # macOS/Linux
$env:MISTRAL_API_KEY   # Windows

# Testez la connexion (devrait retourner "OK")
mistral-vibe test-api
```

**⚠️ Si quelque chose ne fonctionne pas :**
1. Revérifiez le guide d'installation
2. Vérifiez que vous avez bien suivi toutes les étapes
3. Demandez de l'aide au professeur

---

## 🧪 Expériences Simples pour Commencer

### **1. Votre Premier Projet avec Vibe**

Créez un dossier pour votre atelier et commencez à explorer :

```bash
# Créez un dossier pour l'atelier
mkdir mon-projet-vibe
cd mon-projet-vibe

# Demandez à Mistral Vibe de créer une structure de base
mistral-vibe run "Créez une structure de projet web avec :
- un dossier 'src' pour le code
- un dossier 'assets' pour les images
- un dossier 'docs' pour la documentation
- un fichier 'index.html' de base
- un fichier 'README.md' pour décrire le projet"
```

**📁 Explorez ce qui a été créé :**
```bash
# Listez les fichiers créés
ls -la

# Ouvrez le fichier HTML créé
# Sur Windows : start index.html
# Sur macOS : open index.html
```

### **2. Modifiez et Améliorez**

Maintenant, demandez à Mistral Vibe d'améliorer votre projet :

```bash
# Ajoutez du contenu au fichier HTML
mistral-vibe run "Dans index.html, ajoutez :
- un titre 'Mon Projet de Mobilité Intelligente'
- un paragraphe décrivant un projet de parking intelligent
- une section 'À propos' avec votre nom
- un pied de page avec la date d'aujourd'hui"

# Créez un fichier CSS pour le style
mistral-vibe run "Créez un fichier 'style.css' dans assets/ avec :
- une police moderne
- des couleurs bleues et blanches
- un design responsive pour mobile
- des animations simples"
```

### **3. Expérimentez avec Différents Types de Contenu**

Essayez ces commandes pour comprendre les capacités :

```bash
# Générez du contenu pour votre projet
mistral-vibe run "Créez un fichier 'projet.md' qui explique :
- les objectifs d'un système de parking intelligent
- les technologies utilisées (IA, capteurs, applications)
- les bénéfices pour les utilisateurs et la ville"

# Créez un script Python simple
mistral-vibe run "Créez un script 'analyse.py' qui :
- lit un fichier de données CSV
- calcule des statistiques basiques
- génère un rapport simple"

# Générez des idées de projet
mistral-vibe run "Donnez-moi 5 idées innovantes pour améliorer la mobilité urbaine en utilisant l'IA"
```

**💡 Conseils pour de meilleures requêtes :**
- Soyez **précis** dans vos demandes
- Donnez des **exemples** quand possible
- Demandez des **explications** si le code n'est pas clair
- N'hésitez pas à **demander des modifications**

---

## 🌐 Projet Principal : Créer Votre Site Web de Projet

### **1. Préparation de Votre Projet**

**Matériel nécessaire :**
- Un document décrivant votre projet (Word, PDF, ou notes)
- Des images ou schémas si disponibles
- Une idée claire de ce que vous voulez présenter

**📝 Planifiez votre site web :**
1. **Page d'accueil** : Présentation générale du projet
2. **Page « À propos »** : Votre équipe et vos objectifs
3. **Page « Technologie »** : Les solutions techniques utilisées
4. **Page « Impact »** : Les bénéfices pour la mobilité
5. **Page « Contact »** : Comment vous joindre

### **2. Méthodologie Pas à Pas**

#### **Étape 1 : Planification (15-30 minutes)**

```bash
# Créez un plan détaillé avec Mistral Vibe
mistral-vibe run "Aidez-moi à planifier un site web pour mon projet de parking intelligent. 
Le site devrait inclure :
- Une page d'accueil avec une bannière et une description
- Une section expliquant la technologie utilisée
- Une galerie d'images ou de schémas
- Une page de contact avec un formulaire
Donnez-moi une structure HTML complète avec des commentaires."
```

**📋 Vérifiez le plan généré :**
- Le code est-il bien organisé ?
- Toutes les sections nécessaires sont-elles présentes ?
- Les commentaires sont-ils clairs ?

#### **Étape 2 : Création de la Structure (30-45 minutes)**

```bash
# Créez la structure HTML de base
mistral-vibe run "Générez le code HTML complet pour mon site web selon le plan. 
Incluez :
- Une navigation entre les pages
- Des espaces réservés pour le contenu
- Un design moderne et professionnel
- Du code bien commenté pour que je puisse le comprendre"

# Créez le fichier CSS correspondant
mistral-vibe run "Générez le CSS pour mon site web avec :
- Un thème bleu et blanc (couleurs de la mobilité)
- Une police professionnelle
- Un design responsive pour mobile
- Des animations subtiles"
```

**🔍 Testez localement :**
```bash
# Ouvrez votre page dans un navigateur
# Sur Windows : start index.html
# Sur macOS : open index.html

# Vérifiez que :
- Le design est cohérent
- La navigation fonctionne
- Le site est lisible sur mobile
```

#### **Étape 3 : Ajout de Contenu (45-60 minutes)**

Maintenant, personnalisez avec votre contenu réel :

```bash
# Ajoutez votre contenu spécifique
mistral-vibe run "Aidez-moi à ajouter du contenu à ma page d'accueil :
- Un titre : 'Gare Ton Char - Solution de Parking Intelligent'
- Un sous-titre : 'Révolutionner le stationnement urbain avec l'IA'
- Un paragraphe expliquant notre projet en 3-4 phrases
- Une liste des fonctionnalités principales"

# Ajoutez des images
mistral-vibe run "Montrez-moi comment ajouter des images à mon site. 
Expliquez comment :
- Créer une galerie d'images
- Ajouter des légendes
- Optimiser les images pour le web"
```

**📸 Pour vos images :**
- Utilisez des schémas de votre projet
- Ajoutez des captures d'écran si disponibles
- Utilisez des images libres de droits (Unsplash, Pexels)

#### **Étape 4 : Améliorations (30-45 minutes)**

Une fois la base terminée, améliorez votre site :

```bash
# Ajoutez un formulaire de contact
mistral-vibe run "Créez un formulaire de contact complet avec :
- Champs pour nom, email, message
- Validation des entrées
- Un bouton d'envoi stylisé
- Protection contre les spams"

# Ajoutez des éléments interactifs
mistral-vibe run "Ajoutez une carte interactive à mon site. 
Utilisez une solution simple comme :
- Une carte Leaflet ou Google Maps
- Marquez l'emplacement de notre projet
- Ajoutez une légende explicative"

# Améliorez le design
mistral-vibe run "Suggérez 3 améliorations de design pour mon site :
1. Une animation d'accueil
2. Des effets au survol
3. Une barre de progression"
```

### **3. Validation et Tests**

**✅ Liste de vérification avant de terminer :**

```bash
# Testez toutes les fonctionnalités
mistral-vibe run "Créez une checklist de test pour mon site web"
```

**Tests à effectuer :**
- [ ] Toutes les pages s'affichent correctement
- [ ] La navigation fonctionne entre les pages
- [ ] Le site est lisible sur mobile (testez avec votre téléphone)
- [ ] Les images s'affichent correctement
- [ ] Les liens fonctionnent
- [ ] Le formulaire de contact est utilisable
- [ ] Le design est cohérent sur toutes les pages

---

## 🤝 Comment Obtenir de l'Aide

### **1. Demander de l'Aide à Mistral Vibe**

**Exemples de bonnes questions :**
```bash
# Si vous ne comprenez pas quelque chose
mistral-vibe run "Expliquez-moi cette partie du code : [collez le code ici]"

# Si quelque chose ne fonctionne pas
mistral-vibe run "Pourquoi mon image ne s'affiche pas ? Voici mon code : [code]"

# Pour des suggestions
mistral-vibe run "Comment puis-je améliorer cette section ? [décrivez la section]"
```

### **2. Demander de l'Aide au Professeur**

**Quand demander de l'aide humaine :**
- Vous êtes bloqué depuis plus de 15 minutes
- Vous ne comprenez pas les explications de Mistral Vibe
- Vous avez besoin de conseils sur la direction de votre projet
- Vous voulez des retours sur votre design

**Comment demander efficacement :**
1. **Décrivez** ce que vous essayez de faire
2. **Montrez** le code ou l'erreur
3. **Expliquez** ce que vous avez déjà essayé
4. **Posez** une question spécifique

---

## 🚀 Pour Aller Plus Loin (Si Vous Avez Fini)

### **1. Expérimentez avec d'autres fonctionnalités**

```bash
# Analyse de données pour la mobilité
mistral-vibe run "Créez un script Python qui :
- Analyse des données de trafic
- Génère des visualisations
- Prédit les tendances de stationnement"

# Intégration avec des APIs
mistral-vibe run "Montrez-moi comment intégrer une API météo à mon site"

# Création d'une application mobile
mistral-vibe run "Générez le code de base pour une application mobile de parking"
```

### **2. Idées de Projets pour l'Ingénierie Automobile**

**Projets que vous pourriez explorer avec Mistral Vibe :**

1. **Système de Prédiction de Parking**
   - Analyse des données historiques
   - Prédiction des places disponibles
   - Intégration avec des capteurs IoT

2. **Optimisation des Trajets**
   - Calcul des itinéraires optimaux
   - Réduction des embouteillages
   - Intégration avec les transports en commun

3. **Gestion Intelligente du Trafic**
   - Analyse des flux de circulation
   - Proposition de solutions en temps réel
   - Simulation de scénarios

4. **Véhicules Autonomes**
   - Simulation de comportements
   - Analyse des données de capteurs
   - Optimisation des algorithmes

### **3. Préparation pour vos Projets Futurs**

Utilisez Mistral Vibe pour :
- **Documenter** vos projets
- **Créer des présentations** professionnelles
- **Analyser des données** complexes
- **Prototyper rapidement** des idées

---

## 📚 Ressources Supplémentaires

- **[Documentation Mistral Vibe](https://mistral.ai/docs)** *(Documentation officielle)*
- **[Exemples de Projets](https://mistral.ai/examples)** *(Inspiration pour vos projets)*
- **[Communauté Mistral AI](https://mistral.ai/community)** *(Pour poser des questions)*

---

**🎉 Félicitations !** Vous avez créé votre premier site web avec l'aide de l'IA. Vous êtes maintenant prêt à utiliser ces outils pour vos projets d'ingénierie et au-delà !

**💡 N'oubliez pas :**
- Sauvegardez votre travail régulièrement
- Expérimentez et amusez-vous
- L'IA est là pour vous aider, pas pour remplacer votre créativité
- Les compétences que vous avez apprises aujourd'hui sont très recherchées dans l'industrie

**Prochaines étapes :**
- Continuez à explorer les capacités de Mistral Vibe
- Appliquez ces techniques à vos projets réels
- Partagez vos créations avec la communauté
- Restez à jour avec les dernières avancées en IA pour la mobilité