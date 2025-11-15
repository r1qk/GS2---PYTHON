#backend | salva cadastros no JSON
from pathlib import Path
import json

class LeadRepository:
    def __init__(self):
        self.DATA_DIR = Path(__file__).resolve().parent / "data"#caminho da paste repo
        self.DATA_DIR.mkdir(exist_ok=True) #cria a pasta ?
        self.DB_PATH = self.DATA_DIR / "leads.json" # cria o json bd

    def _load(self):
        if not self.DB_PATH.exists():
            return []
        try:
            return json.loads(self.DB_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
        
    def _save(self, leads):
        self.DB_PATH.write_text(json.dumps(leads, ensure_ascii = False, indent = 2), encoding="utf-8")
    
    def create_lead(self, lead_dict):
        leads_loaded = self._load()
        leads_loaded.append(lead_dict)
        self._save(leads_loaded)

    def read_leads(self):
        return self._load()
    
    
