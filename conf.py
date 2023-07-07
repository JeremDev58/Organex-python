
from cryptography.fernet import Fernet
import os
import json
import sys
LIST_ICONS = ["back", "home", "plus", "valid"]
DEFAULT_COLOR = {
    "light": {
        "element": [],
        "font" : [],
        "icons": os.path.join(os.getcwd(), "theme/icons/light")
    },
    "dark": {
        "element": [],
        "font" : [],
        "icons": os.path.join(os.getcwd(), "theme/icons/light")
        }
}
DEFAULT_FONT = {
    "size": {
        'h1': '40dp', 
        'h2': '30dp', 
        'normal': '20dp', 
        'sub': '10dp'
    }
}
KEY_APP = b'YneL-tf43OC_FWc5FOjuwX5LPQy57XyfNzX3UGJP7Ps='

def _check_path():
    try:
        if not os.path.isdir(os.path.join(os.getcwd(), "theme")):
            os.mkdir(os.path.join(os.getcwd(), "theme"))
        if not os.path.isfile(os.path.join(os.getcwd(), "theme/conf.json")):
            with open(os.path.join(os.getcwd(), "theme/conf.json"), 'w') as f:
                json.dump({"last_theme": "light"}, f)
        if not os.path.isdir(os.path.join(os.getcwd(), "theme/icons")):
            raise
        else:
            if not os.path.isdir(os.path.join(os.getcwd(), "theme/icons/light")):
                raise
            else:
                for icon in LIST_ICONS:
                    if not os.path.isdir(os.path.join(os.getcwd(), "theme/icons/light/{0}.{1}".format(icon, "png"))):
                        raise
            if not os.path.isdir(os.path.join(os.getcwd(), "theme/icons/dark")):
                raise
            else:
                for icon in LIST_ICONS:
                    if not os.path.isdir(os.path.join(os.getcwd(), "theme/icons/dark/{0}.{1}".format(icon, "png"))):
                        raise
    except:
        sys.exit(1)

def _conf_key():
    try:
        if os.path.isfile(os.path.join(os.getcwd(), "secure")):
            with open('secure', 'rb') as f:
                return Fernet(KEY_APP).decrypt(f.read())
        else:
            _clear_key()
            with open('secure', 'wb') as f:
                f.write(Fernet(KEY_APP).encrypt(Fernet.generate_key()))
            with open('secure', 'rb') as f:
                return Fernet(KEY_APP).decrypt(f.read())
    except:
        sys.exit(1)

def _clear_key():
    remove_dir = os.path.join(os.getcwd(), "tasks")
    try:
        if os.path.isdir(remove_dir):
            for root, dirs, files in os.walk(remove_dir):
                for file in files:
                    os.remove(os.path.join(remove_dir, file))
        else:
            os.mkdir(os.path.join(os.getcwd(), "tasks"))
    except:
        sys.exit(1)

def _conf_theme():
    _check_path()
    kw_theme = {}
    try:
        with open(os.path.join(os.getcwd(), "theme/conf.json"), 'r') as f:
                last_theme = json.load(f)
        last_theme_value = last_theme.get("last_theme", "null")
    except:
        last_theme_value = "light"
    finally:
        if last_theme_value in ["light", "dark", "null"]:
            if last_theme_value == "dark":
                kw_theme.update(DEFAULT_COLOR.get("dark"))
            else:
                kw_theme.update(DEFAULT_COLOR.get("light"))
        else:
            try:
                 with open(os.path.join(os.getcwd(), "theme/{0}.json".format(last_theme)), 'r') as f:
                        kw_theme.update(json.load(f))
            except:
                kw_theme.update(DEFAULT_COLOR.get("light"))
    if len(kw_theme) == 0:
        kw_theme = DEFAULT_COLOR.get("light")
    kw_theme.update(DEFAULT_FONT)
    return kw_theme

class Configure():
    list_names: list() = []
    def __init__(self) -> None:
        self._key_crypt = _conf_key()
        self.theme_app = _conf_theme()

    def _encrypt_task(self, task: object):
        pass

    def _decrypt_tasks():
        pass

    def _encrypt_planner(self, planner: object):
        pass

    
   