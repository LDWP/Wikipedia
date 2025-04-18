from mwAPI.login import post_request_login
from mwAPI.main import *
import time

post_request_login("Pseudonyme")

with open("pages.txt", "r", encoding='utf-8') as file:
    pages = [page.strip() for page in file.readlines()]

for page in pages:
    """Exemple pour suppression
    reason = "G6 - Page vide ou blanchie"
    delete_page(page, reason)
    print(f"La page {page} a été supprimée.")
    """

    """Exemple pour protection
    reason = "Modèle très utilisé"
    protect_page(page, reason, expiry="3 days", edit_protection="autoconfirmed", move_protection="autoconfirmed") #SP
    protect_page(page, reason, expiry="3 days", edit_protection="editextendedsemiprotected", 
    move_protection="editextendedsemiprotected") #SPE
    protect_page(page, reason, expiry="3 days", edit_protection="sysop", move_protection="sysop") #Admin
    """

    """Exemple de déprotection
    reason="Tentative de déprotection"
    unprotect_page(page, reason)
    """
    time.sleep(3)