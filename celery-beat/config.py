task_time_limit = 180          # 45 menutes
task_soft_time_limit = 180     # 41.67 menutes
enable_utc = True
# schedules
from datetime import timedelta
beat_schedule = {
    # 'printy': {
    #     'task': 'printy',
    #     'schedule': timedelta(seconds=5),
    #     'args': (8, 2)
    # },
    'printy': {
        'task': 'tasks.printy',
        'schedule': timedelta(seconds=15)
    },

}