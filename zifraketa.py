import operator
import string

##Azpiprogramak

def printZerr(m):
    for i in m:
        print(i)

def maiztasunakLortu(mezua,hizHiztegia):
    for i in hizHiztegia.keys():
        maiztasuna = mezua.count(i)
        hizHiztegia[i] = maiztasuna

def ordezkatuHizk(hizkiZ, hizkiB, mezua, hKorresp):
    hKorresp[hizkiZ] = hizkiB
    return mezua.replace(hizkiZ, hizkiB)
         
def guztiaLetraXehez(mezua):
    return (mezua.lower() == mezua)
     
##ProgramNag

jatMezua="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ \nRKCHXKCI AX CJAXDXJAXJRCE  AX RTENX, E \
ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ \nEJEKSZCNHE. \n \n\
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. \nDXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, \
JI REVI AXT RCXTI. DXKNIJCOCREQE TE \nHKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX  DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, \nKXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI \
XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE \nCAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. \nNCJ AZKKZHC SZXAI PEN \
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT \nOKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,  HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK \
TE \nKXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE. \n"
print("Jatorrizko mezua hurrengoa da: \n")
print(jatMezua)

maiztasunak = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0,
                "K": 0, "L": 0, "M": 0, "N": 0, "Ñ": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0,
                "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}

hiztegiBerria = {"A": " ", "B": " ", "C": " ", "D": " ", "E": " ", "F": " ", "G": " ", "H": " ", "I": " ", "J": " ",
                "K": " ", "L": " ", "M": " ", "N": " ", "Ñ": " ", "O": " ", "P": " ", "Q": " ", "R": " ", "S": " ",
                "T": " ", "U": " ", "V": " ", "W": " ", "X": " ", "Y": " ", "Z": " "}

print("Hona hemen hizkien maiztasun taula: \n")
maiztasunakLortu(jatMezua,maiztasunak)
maiztOrdenatua = sorted(maiztasunak.items(), key=operator.itemgetter(1), reverse=True)
printZerr(maiztOrdenatua)

#1. Lehenengo ordezkapenak: 'X': 103 -> 'E'; 'E': 94 -> 'A'
print("#1. Lehenengo ordezkapenak: 'X': 103 -> 'E'; 'E': 94 -> 'A' \n")
jatMezua = ordezkatuHizk(maiztOrdenatua[0][0], "e", jatMezua, hiztegiBerria)
jatMezua = ordezkatuHizk(maiztOrdenatua[1][0], "a", jatMezua, hiztegiBerria)


#2. 2 eta 3 hizkiko hitzei erreparatuz konturatu gaitezteke: A -> d; T -> l
print("#2. 2 eta 3 hizkiko hitzei erreparatuz konturatu gaitezteke: A -> d; T -> l \n")
jatMezua = ordezkatuHizk("A", "d", jatMezua, hiztegiBerria)
jatMezua = ordezkatuHizk("T", "l", jatMezua, hiztegiBerria)

#3. Hemendik aurrera logika bidez ondorioztatu, begizta handiaren bidez
print("#3. Hemendik aurrera logika bidez ondorioztatu, begizta handiaren bidez \n")
while not(guztiaLetraXehez(jatMezua)):
    #Maiztasunak
    print("Hona hemen hizkien maiztasun taula: \n")
    maiztasunakLortu(jatMezua,maiztasunak)
    maiztOrdenatua = sorted(maiztasunak.items(), key=operator.itemgetter(1), reverse = True)
    printZerr(maiztOrdenatua)
    
    #Input
    print("\n")
    print("Momentuko mezua: \n")
    print(jatMezua)
    hKendu = ""
    hGehitu = ""
    while(len(hKendu) != 1):
        hKendu = str(input("Aldatu nahi duzun hizkia sartu: "))
    while(len(hGehitu) != 1):
        hGehitu = str(input("Zein hizki sartu nahi duzu " + hKendu + "-ren lekuan?"))
    
    #Ordezkapena
    print("Ordezkapena: ' " + hKendu + "' -> '" + hGehitu + "'.")
    jatMezua = ordezkatuHizk(hKendu, hGehitu, jatMezua, hiztegiBerria)
    print("Momentuko mezua: \n")
    print(jatMezua)
    print("Hiztegi berria: \n")
    printZerr(sorted(hiztegiBerria.items()))
    
    print("\n -------------------------------------------------------------------- \n")
