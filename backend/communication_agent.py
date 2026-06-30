class CommunicationScanner:

    def __init__(self):
        self.flagged_words = [
            "fraud",
            "bribe",
            "money laundering",
            "illegal",
            "fake",
            "secret transfer",
            "black money"
        ]

    def scan_message(self, message):

        message = message.lower()

        for word in self.flagged_words:
            if word in message:
                return {
                    "message": message,
                    "status": "Flagged",
                    "reason": word
                }

        return {
            "message": message,
            "status": "Safe",
            "reason": "No suspicious keywords"
        }
