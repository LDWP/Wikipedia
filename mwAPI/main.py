from mwAPI.user_config import SESSION, URL, HEADERS


def fetch_CSRF_token():
    PARAMS = {
        "action": "query",
        "meta": "tokens",
        "format": "json"
    }
    RESPONSE = SESSION.get(url=URL, params=PARAMS, headers=HEADERS)
    DATA = RESPONSE.json()
    return DATA['query']['tokens']['csrftoken']


def edit_page(page_title, text, summary):
    CSRF_TOKEN = fetch_CSRF_token()
    PARAMS = {
        "action": "edit",
        "title": page_title,
        "token": CSRF_TOKEN,
        "summary": summary,
        "format": "json",
        "text": text
    }
    RESPONSE = SESSION.post(url=URL, data=PARAMS, headers=HEADERS)
    return RESPONSE.json()


def delete_page(page_title, reason):
    CSRF_TOKEN = fetch_CSRF_token()
    PARAMS = {
        "action": "delete",
        "title": page_title,
        "token": CSRF_TOKEN,
        "format": "json",
        "reason": reason
    }
    RESPONSE = SESSION.post(url=URL, data=PARAMS, headers=HEADERS)
    return RESPONSE.json()


def move_page(from_title, to_title, reason, noredirect=False, movetalk=True, movesubpages=True):
    CSRF_TOKEN = fetch_CSRF_token()
    PARAMS = {
        "action": "move",
        "format": "json",
        "from": from_title,
        "to": to_title,
        "reason": reason,
        "token": CSRF_TOKEN
    }

    if movetalk:
        PARAMS["movetalk"] = "1"

    if noredirect:
        PARAMS["noredirect"] = "1"

    if movesubpages:
        PARAMS["movesubpages"] = "1"

    RESPONSE = SESSION.post(url=URL, data=PARAMS, headers=HEADERS)
    return RESPONSE.json()


def get_protection_value(level):
    protection_levels = ["all", "autoconfirmed", "editextendedsemiprotected", "sysop"]
    if level in protection_levels:
        return level
    else:
        raise ValueError(f"Protection invalide : {level}. Choix possibles : {', '.join(protection_levels)}")


def protect_page(title, reason, expiry="3 days", edit_protection="autoconfirmed", move_protection="all"):
    try:
        edit_protection = get_protection_value(edit_protection)
        move_protection = get_protection_value(move_protection)
    except ValueError as ve:
        print(f"Erreur de validation des protections : {ve}")
        return None
    CSRF_TOKEN = fetch_CSRF_token()

    PARAMS = {
        "title": title,
        "reason": reason,
        "protections": f"edit={edit_protection}|move={move_protection}",
        # "cascade": cascade,
        "expiry": expiry,
        "token": CSRF_TOKEN,
        "action": "protect"
    }
    RESPONSE = SESSION.post(url=URL, data=PARAMS, headers=HEADERS)
    return RESPONSE.json()


def unprotect_page(title, reason):
    return protect_page(title, reason, edit_protection="all", move_protection="all")
