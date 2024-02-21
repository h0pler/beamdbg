import sys
import logmaster as log
import help

version = "0.0.0"
log.printInfo("Beamdbg v" + version)
if len(sys.argv) != 4:
    log.printError(f"Usage: {sys.argv[0]} <code file> <input file> <output file>", 1)

code_file = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]

try:
    log.printInfo(f"Loading code file \033[34m{code_file}\033[0m...")
    with open(code_file, "r") as f:
        code = f.read()
    log.printInfo(f"Code file successfully loaded \033[34m{code_file}\033[0m")
except FileNotFoundError:
    log.printError(f"Code file not found \033[34m{code_file}\033[0m", 2)

try:
    log.printInfo(f"Loading input file \033[32m{input_file}\033[0m...")
    with open(input_file, "r") as f:
        inp = f.read()
    log.printInfo(f"Input file successfully loaded \033[32m{input_file}\033[0m")
except FileNotFoundError:
    log.printError(f"Cannot found input file \033[32m{input_file}\033[0m", 3)

output_fp = open(output_file, "w")

print()
log.printInfo("Starting to debug...")
readable_chars = "><^v+-@:/\\!?|_HSLsgPpun`')(r\n "
for c in code:
    if c not in readable_chars:
        log.printWarning(f"Found unreadable char \033[31m{c}\033[0m in code, it will be ignored.")

prefix = "beamdbg> "
splitted_code = code.split("\n")
height = len(splitted_code)
width = max([len(l) for l in splitted_code])

def show_code(x = None, y = None):
    if x == None and y == None:
        print(code)

log.printInfo(f"Code height: {height}")
log.printInfo(f"Code width: {width}")
log.printInfo("For help, type \"help\".")
while True:
    cmd = input(prefix)
    if cmd == "help":
        print(help.help_msg)
    elif cmd == "b":
        continue
    elif cmd == "ni":
        continue
    elif cmd == "start":
        continue
    else:
        log.printInfo("Unknown command. type \"help\" for help.")