# Analyse-des-Cin-mas
# Analyse des Cinémas en Île-de-France

Ce projet vise à analyser l'impact des infrastructures cinématographiques (nombre d'écrans et de fauteuils) sur la fréquentation des cinémas en Île-de-France. L'objectif final est de déterminer si l'ajout d'écrans ou de fauteuils influe significativement sur les entrées annuelles et de construire un modèle prédictif. Ce travail a été réalisé avec Flask, car je n'avais pas encore reçu les cours Python préalables, ayant été absent lors des deux premiers cours.

## Structure du projet

- `app.py` : Le script principal contenant la logique d'analyse des données et le backend Flask.
- `templates/index.html` : Le fichier HTML pour afficher les résultats.
- `static/styles.css` : Feuille de style pour une mise en page claire et attrayante.
- `data/cinemas.csv` : Le fichier de données contenant les informations des cinémas.

## Déroulement des étapes

### Exercice 1 : Nettoyage et Exploration des Données

- **Nettoyage** :
  - Les données manquantes ont été supprimées pour garantir l'intégrité de l'analyse.
  - Un commentaire dans le code explique pourquoi ces valeurs ont été exclues.

- **Exploration** :
  - Les premières lignes du dataset sont affichées pour un aperçu des données.
  - Les statistiques descriptives des colonnes `fauteuils`, `ecrans`, et `entrees_annuelles` sont présentées.

### Exercice 2 : Analyse des Entrées Moyennes par Fauteuil

- Calcul des entrées moyennes par fauteuil pour chaque commune en 2022.
- Identification des 3 communes ayant les meilleurs et pires résultats.
- Un graphique à barres représentant les entrées moyennes par fauteuil pour les 10 communes principales est affiché.

### Exercice 3 : Corrélations et Visualisations

- Les données ont été filtrées pour conserver uniquement l'année 2022.
- Calcul des corrélations entre :
  - Le nombre d'écrans et les entrées annuelles.
  - Le nombre de fauteuils et les entrées annuelles.
- Deux nuages de points avec des régressions linéaires superposées sont présentés.
- **Conclusion** : Le nombre d'écrans a un impact légèrement plus important que le nombre de fauteuils sur les entrées annuelles.

### Exercice 4 : Modélisation Prédictive

- Les données de 2018 à 2021 ont été utilisées pour entraîner un modèle de régression linéaire.
- Division des données :
  - 80% pour l'entraînement.
  - 20% pour les tests.
- **Évaluation du modèle** :
  - Coefficient de détermination (R²) : 0.63
  - Erreur Moyenne Absolue (MAE) : 56,468
- Le modèle prédit les entrées pour 2022 et compare les résultats prédits aux valeurs réelles.

### Exercice 5 : Recommandation pour une Commune Fictive

- Pour une commune fictive de 20 000 habitants avec 2 écrans et 120 fauteuils, le modèle prédit 14 817 entrées annuelles.
- **Recommandation** : Augmenter le nombre d'écrans semble être une stratégie plus efficace en raison de sa corrélation plus élevée avec les entrées annuelles.

## Installation et Exécution

1. Clonez le dépôt :
   ```bash
   git clone <URL_du_depot>
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Lancez l'application Flask :
   ```bash
   python app.py
   ```

4. Ouvrez votre navigateur et accédez à :
   [http://127.0.0.1:5001](http://127.0.0.1:5001)

## Conclusion

Ce projet m'a permis d'appliquer les bases de la data science et de l'apprentissage machine. Bien que je n'aie pas assisté aux premiers cours, j'ai réussi à compléter cet exercice grâce à Flask et aux connaissances acquises en autodidacte. Je suis prêt à approfondir mes compétences dans ces domaines.

