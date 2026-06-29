import time

class SLAManager:

    def __init__(self):

        self.sla_limits = {
            "default": 30  # seconds
        }

    def is_breached(self, start_time: float, task_type="default"):

        limit = self.sla_limits.get(task_type, 30)

        return (time.time() - start_time) > limit