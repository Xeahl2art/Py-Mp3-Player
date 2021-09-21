import subprocess

client = subprocess.Popen([
        "ffplay",
        "rtp://127.0.0.1",

    ])
