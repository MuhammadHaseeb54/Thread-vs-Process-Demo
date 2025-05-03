import psutil

def get_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    used_memory_mb = memory_info.used // (1024 * 1024)
    return cpu_usage, used_memory_mb
