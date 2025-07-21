import time
import logging
import subprocess
import psutil


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


def get_cpu_temp():
    try:
        output = subprocess.check_output(['osx-cpu-temp']).decode('utf-8')
        temp = float(output.strip().replace('°C', ''))
        return temp
    except Exception as e:
        logger.warning(f'Exception: {e}')
        return 0.0


def smart_sleep():
    temp = get_cpu_temp()
    cpu = psutil.cpu_percent(interval=0.1)

    sleep_time = 0

    if temp > 65 or cpu > 70:
        sleep_time = 2000
    elif temp > 45 or cpu > 50:
        sleep_time = 20

    if sleep_time > 0:
        time.sleep(sleep_time)
