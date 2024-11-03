from colorama import Fore, Style, init
import os,yaml

# colorama config setting
init(autoreset=True)

# parsing techniques YAML file
script_path = os.path.dirname(os.path.abspath(__file__))
with open(f"{script_path}/../cs_templates/injection_techniques.yml","r") as f:
        injection_list = yaml.safe_load(f)