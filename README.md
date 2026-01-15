# 🏥 MediSense - Plateforme de Gestion Médicale Intelligente

**MediSense** est une solution complète de gestion médicale conçue pour optimiser l'interaction entre les professionnels de santé, le personnel administratif et les patients. En intégrant l'intelligence artificielle (Gemini AI), MediSense va au-delà d'un simple outil de gestion pour devenir un véritable assistant de santé.

---

## 🌟 Vision du Projet
MediSense vise à moderniser le parcours de soin en offrant :
- **Efficacité Opérationnelle** : Gestion fluide des rendez-vous et des dossiers patients.
- **Support Intelligent** : Assistance médicale par IA pour l'analyse des symptômes.
- **Accessibilité** : Interfaces dédiées et intuitives pour chaque rôle utilisateur (Médecin, Patient, Assistant).

---

## 🛠 Technologies Utilisées

### Backend
- **Framework** : Django 3.0.5 (Python)
- **Base de données** : SQLite (par défaut)
- **Authentification** : Système de rôles personnalisés basé sur `AbstractUser`.

### Frontend
- **Interface** : Templates Django avec HTML5, CSS3 haute performance.
- **Dynamisme** : JavaScript Vanilla pour une expérience utilisateur fluide.

### Intelligence Artificielle
- **Moteur** : Google Gemini AI (`gemini-2.0-flash`).
- **Fonctionnalité** : Chat interactif pour l'orientation médicale et la recherche clinique.

---

## ✨ Fonctionnalités Principales

### 1. 📋 Gestion des Patients
- Visualisation globale des patients avec indicateurs de santé dynamiques.
- Filtrage avancé par groupe sanguin, ville ou statut de santé (Stable, Bon, Critique).

### 2. 📅 Système de Rendez-vous
- Planification complète avec gestion des statuts (En attente, Confirmé, Terminé, Annulé).
- Calcul automatique de la durée et de l'heure de fin des consultations.

### 3. 🤖 Assistant Médical IA (Chat)
- Discussion en temps réel avec un "docteur virtuel" empathique.
- Localisation des cliniques et médecins partenaires au Maroc via Google Maps.

### 4. 📊 Tableaux de Bord Dynamiques
- Statistiques en temps réel sur les admissions.
- Graphiques de répartition par âge et par état de santé.

---

## ⚙️ Installation et Configuration

1. **Cloner le projet**
   ```bash
   git clone <URL_DU_DEPOT>
   cd MediSense
   ```

2. **Installer les dépendances**
   ```bash
   pip install django google-generativeai markdown
   ```

3. **Configurer l'API Gemini**
   Ajoutez votre clé API dans `medisenese/settings.py` :
   ```python
   GEMINI_API_KEY = "VOTRE_CLE_API"
   ```

4. **Lancer les migrations**
   ```bash
   python manage.py migrate
   ```

5. **Démarrer le serveur**
   ```bash
   python manage.py run_server
   ```

---

## 🏗 Architecture et Rôles
- **Médecins** : Accès complet aux dossiers patients et gestion du calendrier.
- **Assistants** : Support administratif et accueil des patients.
- **Patients** : Prise de rendez-vous et accès à l'assistant IA.

---

## 📂 Structure du Projet

L'organisation des fichiers suit l'architecture standard de Django, structurée comme suit :

### 📁 Racine du Projet
- **`manage.py`** : L'outil en ligne de commande de Django pour la gestion du projet (serveur, migrations, etc.).
- **`db.sqlite3`** : La base de données locale par défaut.
- **`README.md`** : Documentation principale du projet.

---

### 📁 `medisenese/` (Configuration)
Dossier de configuration globale du projet :
- **`settings.py`** : Configuration principale (Database, Apps, API Keys Gemini, etc.).
- **`urls.py`** : Déclaration des routes principales et routage vers les applications.
- **`wsgi.py` / `asgi.py`** : Points d'entrée pour le déploiement sur les serveurs web.

---

### 📁 `account/` (Application Principale)
Contient toute la logique métier liée aux utilisateurs et aux fonctionnalités médicales :
- **`models.py`** : Définition des entités `User`, `Profile` et `Schedule` (Rendez-vous).
- **`views.py`** : Logique de traitement des requêtes (Authentification, Dashboard, gestion des RDV, Chat IA).
- **`urls.py`** : Définition des routes spécifiques à l'application `account`.
- **`forms.py`** : Formulaires personnalisés pour l'inscription, le profil et la prise de rendez-vous.

---

### 📁 `templates/` (Interface Utilisateur)
Regroupe tous les fichiers HTML organisés par rôle :
- **`doctors/`**, **`patients/`**, **`assistants/`** : Pages spécifiques à chaque type d'utilisateur.
- **`chat.html`** : Interface de l'assistant intelligent Gemini.
- **`dashboard.html`** : Tableau de bord principal.
- **`partials/`** : Composants réutilisables (Navbar, Sidebar).

---

### 📁 `static/` (Ressources Statiques)
Contient les fichiers CSS, images et scripts JavaScript pour styliser l'application.

---

## 👤 Auteurs
Projet développé dans le cadre du cursus **5IIR** par **Yassir Benjima**.
