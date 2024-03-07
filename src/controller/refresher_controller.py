"""
Module contenant la classe RefresherController.

Ce module définit le contrôleur principal de l'application
de rafraîchissement automatique de pages web.
Il gère l'interaction entre la vue utilisateur et le modèle de rafraîchissement des pages,
fournissant les méthodes pour démarrer et arrêter le rafraîchissement des pages web.
"""
import json
import logging


from model.page_refresher import PageRefresher

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class RefresherController:
    def __init__(self, config_path='config/config.json'):
        self.config_path = config_path
        self.page_refresher = None
        self.config = None

    def load_config(self):
        with open(self.config_path, 'r') as config_file:
            self.config = json.load(config_file)

    def start_refreshing_from_config(self):
        if not self.config:
            self.load_config()
        self.page_refresher = PageRefresher()
        self.page_refresher.start_refreshing(self.config['urls'], self.config['refresh_time'])

    def stop_refreshing(self):
        if self.page_refresher:
            self.page_refresher.stop_refreshing_async()
