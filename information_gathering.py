#Use This script to install information gathering tools
#by kaung khant zaw
import os
import sys
print("BY KAUNG KHANT ZAW")
print("**************************************************************************************")
print('''
1. DNSENUM 2. DNSRECON 3. FIERCE 4. LBD 5. ARPING 6. FPING 7. HPING3
8. MASSCAN 9. NMAP 10. MALTEGO 11. THEHARVESTER 12. NETDISCOVER
13. NETMASK 14. SMBMAP 15. SWAKS 16. NBTSCAN 17. SSLDUMP 18. ONESIXTYONE 19. SNMP-CHECK
20. LEGION 21. DEMITRY 22. SSLH 23. SSLSCAN 24. SSLYZE
25. TO INSTALL ALL''')
print ('''0. TO EXIT THE PROGRAM''')
print("**************************************************************************************")
get_option = int(input("kali>>>"))
if get_option == 1:
    os.system('apt install dnsenum')
elif get_option == 2:
    os.system('apt install dnsrecon')
elif get_option == 3:
    os.system('apt install fierce')
elif get_option == 4:
    os.system('apt install lbd')
elif get_option == 5:
    os.system('apt install arping')
elif get_option == 6:
    os.system('apt install fping')
elif get_option == 7:
    os.system('apt install hping3')
elif get_option == 8:
    os.system('apt install masscan')
elif get_option == 9:
    os.system('apt install nmap')
elif get_option == 10:
    os.system('apt install maltego')
elif get_option == 11:
    os.system('apt install theharvester')
elif get_option == 12:
    os.system('apt install netdiscover')
elif get_option == 13:
    os.system('apt install netmask')
elif get_option == 14:
    os.system('apt install smbmap')
elif get_option == 15:
    os.system('apt install swaks')
elif get_option == 16:
    os.system('apt install nbtscan')
elif get_option == 17:
    os.system('apt install ssldump')
elif get_option == 18:
    os.system('apt install onesixtyone')
elif get_option == 19:
    os.system('apt install snmpcheck')
elif get_option == 20:
    os.system('apt install legion')
elif get_option == 21:
    os.system('apt install demitry')
elif get_option == 22:
    os.system('apt install sslh')
elif get_option == 23:
    os.system('apt install sslscan')
elif get_option == 24:
    os.system('apt install sslyze')