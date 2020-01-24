import psutil
import datetime
import time


def cpu_temp():
    return psutil.sensors_temperatures()['cpu-thermal'][0].current


def cpu_percentages():
    return psutil.cpu_percent(percpu=True)


def load_averages():
    return psutil.getloadavg()


def memory_percentage():
    return psutil.virtual_memory().percent


def uptime():
    # import ipdb
    # ipdb.set_trace()
    return datetime.timedelta(seconds=int(time.time() - psutil.boot_time()))
