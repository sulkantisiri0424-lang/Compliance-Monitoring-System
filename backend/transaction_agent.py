from models import Transaction

class TransactionMonitor:

    def __init__(self):
        self.threshold = 100000

    def analyze_transaction(self, sender, receiver, amount):

        if amount >= self.threshold:
            status = "Suspicious"
        else:
            status = "Normal"

        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "status": status
        }

        return transaction

    def print_report(self, transaction):

        print("----- Transaction Report -----")
        print("Sender :", transaction["sender"])
        print("Receiver :", transaction["receiver"])
        print("Amount :", transaction["amount"])
        print("Status :", transaction["status"])
