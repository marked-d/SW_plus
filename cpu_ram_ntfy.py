import psutil
import subprocess
import ntfy

cpu_percent = psutil.cpu_percent()
mem = psutil.virtual_memory()
mem_percent = mem.percent

message = f"CPU: {cpu_percent}%\nMemory: {mem_percent}%"

print(message)
ntfy.notify(message, title="CPU and Memory Stats")
subprocess.call(['curl', '-d', message, 'ntfy.sh/p2019170'])
