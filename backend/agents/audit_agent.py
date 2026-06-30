class AuditAgent:
    def __init__(self):
        self.logs = []

    def log_event(self, action, status):
        log = {
            "action": action,
            "status": status
        }
        self.logs.append(log)
        return log

    def get_logs(self):
        return self.logs
