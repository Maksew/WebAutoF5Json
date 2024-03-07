"""Module principal pour démarrer l'application de rafraîchissement de pages web."""

import logging
from controller.refresher_controller import RefresherController
from logging_config import setup_logging


def main():
    """
    Point d'entrée principal de l'application de rafraîchissement de pages web.
    Crée le contrôleur de l'application et démarre le processus de rafraîchissement
    selon les configurations chargées.
    """
    controller = RefresherController()
    controller.start_refreshing_from_config()


if __name__ == '__main__':
    try:
        setup_logging()
        main()
    except Exception as e:
        logging.error("Une erreur inattendue est survenue : %s", e)
        raise
