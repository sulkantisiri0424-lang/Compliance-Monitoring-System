class ReportAgent:

    def generate_report(self, transaction, status):

        report = {
            "transaction": transaction,
            "status": status,
            "generated_by": "Compliance Monitoring System"
        }

        return report
