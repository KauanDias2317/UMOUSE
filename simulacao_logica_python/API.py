import sys

# --- Funções que NÃO esperam resposta (Visualização) ---

def setWall(x, y, direction):
    print(f"setWall {x} {y} {direction}")

def clearWall(x, y, direction):
    print(f"clearWall {x} {y} {direction}")

def setColor(x, y, color):
    print(f"setColor {x} {y} {color}")

def clearColor(x, y):
    print(f"clearColor {x} {y}")

def clearAllColor():
    print("clearAllColor")

def setText(x, y, text):
    print(f"setText {x} {y} {text}")

def clearText(x, y):
    print(f"clearText {x} {y}")

def clearAllText():
    print("clearAllText")

def ackReset():
    print("ackReset")

# --- Funções que ESPERAM resposta (Sensores e Movimento) ---

def mouseFace():
    return int(command("mouseFace"))

def mazeWidth():
    return int(command("mazeWidth"))

def mazeHeight():
    return int(command("mazeHeight"))

def wallFront():
    return command("wallFront") == "true"

def wallRight():
    return command("wallRight") == "true"

def wallLeft():
    return command("wallLeft") == "true"

def moveForward(distance=None):
    if distance is not None:
        command(f"moveForward {distance}")
    else:
        command("moveForward")

def moveForwardHalf(distance=None):
    if distance is not None:
        command(f"moveForwardHalf {distance}")
    else:
        command("moveForwardHalf")

def turnRight():
    command("turnRight")

def turnLeft():
    command("turnLeft")

def wasReset():
    return command("wasReset") == "true"

def log(string):
    sys.stderr.write(f"{string}\n")
    sys.stderr.flush()

def command(args):
    line = args + "\n"
    sys.stdout.write(line)
    sys.stdout.flush()
    response = sys.stdin.readline().strip()
    return response

# Se estiver usando Python 3, redefinimos print para garantir flush
def print(line):
    sys.stdout.write(line + "\n")
    sys.stdout.flush()