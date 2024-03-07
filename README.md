# WebAutoF5Json 🔄

WebAutoF5Json est une application Python 🐍 qui permet de rafraîchir automatiquement des pages web à intervalles définis par l'utilisateur via un fichier json. 

## Fonctionnalités 🌟

- 🔄 Rafraîchissement automatique de pages web selon un intervalle spécifié dans un fichier de configuration JSON.
- 📝 Configuration simple et rapide par modification du fichier `config.json`.
- 🚨 Gestion robuste des erreurs avec des journaux détaillés pour le dépannage.
- 🛠️ Support pour le navigateur Edge grâce à Selenium, avec possibilité d'étendre à d'autres navigateurs.

## Installation 🔧

Assurez-vous que Python et pip sont installés sur votre machine. Clonez ensuite le dépôt et installez les dépendances requises :

```bash
pip install -r requirements.txt
```

Cette commande installera automatiquement toutes les bibliothèques et paquets Python nécessaires au bon fonctionnement de l'application.

## Configuration 📁

Avant de lancer l'application, configurez les URLs et les intervalles de rafraîchissement dans le fichier config.json :

```bash
{
  "urls": ["http://example.com", "http://example.org"],
  "refresh_time": 10
}

```

## Utilisation 🛠️

Pour démarrer l'application, exécutez le script principal :

```bash
python src/main.py
```

## Architecture du projet 🏗️

```
WebAutoF5Json/
│
├── src/
│   ├── main.py                          # Point d'entrée principal
│   ├── controller/                      # Contrôleur principal
│   │   └── refresher_controller.py      # Gestion de la configuration et du rafraîchissement
│   ├── model/                           # Modèle pour rafraîchir les pages
│   │   └── page_refresher.py            # Utilise Selenium pour interagir avec les navigateurs
│   └── logging_config.py                # Configuration personnalisée des logs
│
├── config/
│   └── config.json                      # Fichier de configuration JSON pour l'application
│
├── tests/                               # Tests unitaires et d'intégration
│   └── ...                              # Fichiers de test
│
├── drivers/                             # Pilotes WebDriver pour Selenium
│   └── msedgedriver.exe
│
├── docs/                                # Documentation du projet
│   └── documentation.pdf
│
└── venv/                                # Environnement virtuel Python
    └── ...                              # Dépendances installées
```

## Tests 🧪

Des tests unitaires sont fournis pour tester l'intégration entre le contrôleur, le modèle, et l'UI. Pour exécuter les tests, utilisez :

```bash
python -m unittest discover -s tests
```

## Contribution 🤝

Les contributions sont les bienvenues ! Soumettez vos pull requests à la branche principale.

