from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from transaction_agent import TransactionMonitor
from communication_agent import CommunicationScanner
from agents.regulation_agent import RegulationAgent
from agents.report_agent import ReportAgent
from agents.audit_agent import AuditAgent

app = FastAPI(
    title="Compliance Monitoring System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

transaction_agent = TransactionMonitor()
communication_agent = CommunicationScanner()
regulation_agent = RegulationAgent()
report_agent = ReportAgent()
audit_agent = AuditAgent()

@app.get("/")
def home():
    return {
        "message": "Compliance Monitoring System API Running Successfully"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/regulations")
def regulations():
    return regulation_agent.get_all_regulations()
