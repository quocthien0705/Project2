from win32api import GetMonitorInfo, MonitorFromPoint
def get_taskbar_height():
    monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")

    taskbar_height = monitor_area[3] - work_area[3]
    return taskbar_height