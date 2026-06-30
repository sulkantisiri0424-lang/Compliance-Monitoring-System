class RegulationAgent:

    def __init__(self):
        self.regulations = [
            {
                "id": 1,
                "title": "AML Rules",
                "status": "Active"
            },
            {
                "id": 2,
                "title": "KYC Guidelines",
                "status": "Active"
            },
            {
                "id": 3,
                "title": "Data Privacy Policy",
                "status": "Updated"
            }
        ]

    def get_all_regulations(self):
        return self.regulations

    def add_regulation(self, title, status):
        regulation = {
            "id": len(self.regulations) + 1,
            "title": title,
            "status": status
        }
        self.regulations.append(regulation)
        return regulation
