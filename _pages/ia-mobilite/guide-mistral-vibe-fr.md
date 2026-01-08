---
layout: page
permalink: /ia-mobilite/guide-mistral-vibe/
title: Guide Mistral Vibe - Configuration Complete
description: Guide complet pour configurer Mistral Vibe sur Windows et macOS pour vos projets IA & Mobilité
lang: fr
---

# 🚀 Guide Complet Mistral Vibe pour l'IA & Mobilité

**Configuration optimisée pour Windows et macOS.** Ce guide vous explique comment installer et configurer **Mistral Vibe** pour vos projets de développement, avec un focus particulier sur les applications IA & Mobilité comme "Gare Ton Char".

---

## 🆕 Création de Compte & Configuration de la Clé API

### 1. Créez Votre Compte Mistral AI

**Inscrivez-vous sur la plateforme officielle Mistral AI :**

👉 **[Inscription Mistral AI](https://mistral.ai/)** *(Site officiel)*

**Étapes pour créer votre compte :**
1. Allez sur [https://mistral.ai/](https://mistral.ai/)
2. Cliquez sur "S'inscrire" ou "Commencer"
3. Choisissez votre méthode d'inscription préférée (email, Google, GitHub)
4. Complétez le formulaire d'inscription
5. Vérifiez votre adresse email

**🎉 Offre Spéciale pour Étudiants & Développeurs :**
- Le modèle **Devstral-2** est actuellement **GRATUIT** pour tous les utilisateurs
- Vous pouvez utiliser des capacités d'IA avancées **sans aucun frais**
- Même après les périodes promotionnelles, les modèles plus petits restent gratuits pour un usage de base

### 2. Générez Votre Clé API

**Après vous être connecté :**
1. Accédez à vos **Paramètres de Compte** ou **Tableau de Bord API**
2. Recherchez "Clés API" ou "Paramètres Développeur"
3. Cliquez sur "Générer Nouvelle Clé API"
4. Copiez votre clé API immédiatement (elle ne sera plus affichée)

**⚠️ Notes de Sécurité Importantes :**
- **Ne partagez jamais votre clé API** publiquement
- **Ne la commitez pas** dans les dépôts Git
- Stockez-la en toute sécurité dans des variables d'environnement ou des gestionnaires de secrets
- Mistral AI utilise une **facturation basée sur les tokens** - vous ne payez que pour ce que vous utilisez

### 3. Configurez la Clé API pour Mistral Vibe

**Méthodes de configuration recommandées :**

#### Option A : Variable d'Environnement (Plus Sécurisé)
```bash
# Windows (PowerShell)
$env:MISTRAL_API_KEY="votre-clé-api-ici"

# macOS/Linux (Bash)
export MISTRAL_API_KEY="votre-clé-api-ici"

# Pour la rendre permanente, ajoutez à votre profil shell
# (.bashrc, .zshrc, ou .bash_profile)
echo 'export MISTRAL_API_KEY="votre-clé-api-ici"' >> ~/.zshrc
```

#### Option B : Fichier de Configuration Mistral Vibe
Créez un fichier `.env` à la racine de votre projet :
```env
MISTRAL_API_KEY=votre-clé-api-ici
MISTRAL_MODEL=devstral-2  # Utilisez le modèle gratuit
```

**💡 Astuce Pro :** Ajoutez `.env` à votre fichier `.gitignore` pour éviter les commits accidentels :
```gitignore
# Ajoutez ceci à votre .gitignore
.env
*.env
.env*.local
```

### 4. Vérifiez Votre Configuration

Testez votre configuration de clé API :
```bash
# Vérifiez si la variable d'environnement est définie
echo $MISTRAL_API_KEY  # Doit afficher votre clé (macOS/Linux)
$env:MISTRAL_API_KEY   # Doit afficher votre clé (Windows)

# Testez la connexion Mistral Vibe
mistral-vibe test-api
```

**✅ Informations sur la Facturation :**
- **Promotion actuelle** : Le modèle Devstral-2 est GRATUIT
- **Tarification standard** : Pay-as-you-go pour les modèles avancés
- **Niveau gratuit** : Modèles plus petits disponibles pour une utilisation gratuite
- **Avantages étudiants** : Consultez [Mistral AI Education](https://mistral.ai/education) pour les programmes spéciaux

---

## 📋 Prérequis Communs

### 1. Installer Python

Mistral Vibe nécessite **Python 3.8 ou supérieur** :

#### Windows
```bash
# Vérifier la version
python --version

# Si Python n'est pas installé :
# 1. Téléchargez depuis [python.org](https://www.python.org/downloads/windows/)
# 2. Cochez "Add Python to PATH" pendant l'installation
# 3. Redémarrez votre terminal
```

#### macOS
```bash
# Vérifier la version
python3 --version

# Si Python n'est pas installé (via Homebrew) :
brew install python

# Ou via le site officiel :
# Téléchargez depuis [python.org](https://www.python.org/downloads/mac-osx/)
```

---

## 🛠️ Configuration de l'Environnement

### 1. Créer un Environnement Virtuel

#### Windows
```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement
venv\Scripts\activate
```

#### macOS/Linux
```bash
# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement
source venv/bin/activate
```

✅ **Votre terminal devrait maintenant afficher `(venv)`** indiquant que l'environnement est activé.

---

## 🤖 Utilisation de Mistral Vibe

### 1. Lancer Mistral Vibe

Ouvrez Mistral Vibe dans votre terminal et commencez une nouvelle session.

### 2. Décrire Votre Projet

**Soyez précis** pour obtenir les meilleurs résultats :

**Exemple pour un projet comme "Gare Ton Char"** :
> "Je veux créer une application web pour présenter un projet de stationnement intelligent appelé 'Gare Ton Char'. Le site doit inclure : une page d'accueil avec une vidéo de démonstration, une section expliquant les fonctionnalités IA, un lien vers l'application mobile, et un formulaire de contact pour les partenaires."

**Conseils** :
- Mentionnez les technologies souhaitées (React, Flask, etc.)
- Précisez les fonctionnalités clés
- Indiquez si une intégration avec des API est nécessaire

### 3. Planifier avec Mistral Vibe

Demandez un plan de travail structuré :
> "Génère un plan étape par étape pour ce projet avec les vérifications nécessaires à chaque phase."

Mistral Vibe créera un plan détaillé avec :
- Tâches spécifiques
- Outils recommandés
- Points de vérification

### 4. Exécuter des Commandes Automatiquement

Mistral Vibe peut exécuter des commandes pour vous :

#### Windows
```bash
mistral-vibe run "Crée un dossier 'gare-ton-char' avec les sous-dossiers : src, public, components, assets"
mistral-vibe run "Installe react, react-dom, et axios via npm"
```

#### macOS/Linux
```bash
mistral-vibe run "Crée un dossier 'gare-ton-char' avec les sous-dossiers : src, public, components, assets"
mistral-vibe run "Installe react, react-dom, et axios via npm"
```

### 5. Vérification et Validation

Validez le travail à chaque étape :

```bash
# Vérifier la structure
mistral-vibe check "Vérifie que tous les fichiers nécessaires sont présents"

# Tester le code
mistral-vibe test "Lance les tests unitaires pour les composants React"
```

---

## 🎯 Configuration Spécifique pour l'IA & Mobilité

### Installer les Outils IA

Pour les projets comme "Gare Ton Char" :

```bash
# Installer les dépendances IA
mistral-vibe run "Installe tensorflow scikit-learn pandas numpy matplotlib"

# Configurer l'environnement de données
mistral-vibe run "Crée un dossier 'data' pour les jeux de données de mobilité"

# Installer les outils de visualisation
mistral-vibe run "Installe plotly seaborn geopandas"
```

### Configuration des Terminaux

#### Windows (PowerShell)
```bash
# Personnaliser le terminal
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
Import-Module posh-git
Import-Module oh-my-posh

# Installer les polices recommandées
mistral-vibe run "Installe les polices Cascadia Code et Fira Code"
```

#### macOS (Terminal/iTerm2)
```bash
# Installer les outils de ligne de commande
xcode-select --install

# Installer Homebrew (si non installé)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installer les outils utiles
brew install git wget curl tree htop

# Installer les polices
brew tap homebrew/cask-fonts
brew install --cask font-cascadia-code font-fira-code
```

---

## 💻 Développement avec Assistance IA

Utilisez Mistral Vibe pour :

### 1. Générer du Code
> "Crée un composant React pour afficher une carte interactive des parkings avec Leaflet"

### 2. Intégrer des API
> "Ajoute une intégration avec l'API Google Maps pour la géolocalisation en temps réel"

### 3. Optimiser les Performances
> "Analyse et optimise le code pour les performances sur mobile avec des techniques de lazy loading"

### 4. Gérer les Données
> "Crée un pipeline de traitement pour les données de mobilité urbaine en utilisant Pandas"

---

## 🔧 Dépannage

### Problèmes Courants et Solutions

| Problème | Solution Windows | Solution macOS |
|----------|------------------|----------------|
| `Python not found` | Vérifiez PATH | `brew link python` |
| `venv non activé` | `venv\Scripts\activate` | `source venv/bin/activate` |
| Commandes bloquées | Exécutez en admin | `chmod +x` sur les scripts |
| Erreurs de dépendances | `pip install --upgrade` | `pip3 install --upgrade` |
| Terminal lent | Utilisez PowerShell 7+ | Utilisez iTerm2 |

---

## 📚 Ressources Supplémentaires

- [Documentation officielle Mistral Vibe](#) *(à venir)*
- [Guide avancé pour les projets IA](#) *(à venir)*
- [Exemples de projets étudiants](#) *(à venir)*

---

**Prêt à révolutionner votre développement ?** Avec ce guide, configurez Mistral Vibe sur n'importe quelle plateforme et créez des applications innovantes plus rapidement que jamais ! 🚀