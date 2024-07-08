from socket import *

class Port_Scanner:
    def __init__(self, targethost, targetport):
        self.targethost = targethost
        self.targetport = targetport

    def connsocket(targethost, targetport):
        try:
            connection = socket(AF_INET, SOCK_STREAM)
            connection.connect((targethost, targetport))
            print("[+] port %d/tcp is open " %targetport)
            connection.close()

        except:
            print("[-] port %d/tcp is closed " % targetport)


    def portscanner(targethost, targetports):

        try:
            targetIP = gethostbyname(targethost)
            print("[+] could get targetIP %s" % targetIP)

        except:
            print("[-] could not get targetIP %s" % targethost)


        try:
            targetname = gethostbyaddr(targetIP)
            print("[+] target name %s" %targetname[0])

        except:
            print("[-] could not resolve conflict %s" %targetIP)

        setdefaulttimeout(1)
        for targetport in targetports:
            print("Scanning.. %d", int(targetport), end='\r')
            Port_Scanner.connsocket(targethost, int(targetport))


ports_to_scanner = list(range(1, 3001))

Port_Scanner.portscanner('google.com', ports_to_scanner)

