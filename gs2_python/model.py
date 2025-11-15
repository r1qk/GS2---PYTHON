#Como vai ser salvo no Json
class Lead:
    def __init__(self, name, logic, creativity, collaboration, adaptability, recommendation):
        self.name = name
        self.logic = logic
        self.creativity = creativity
        self.collaboration = collaboration
        self.adaptability = adaptability
        self.recommendation = recommendation

    def model_leads(self):
        return {
            "name": self.name,
            "logic": self.logic,
            "creativity": self.creativity,
            "collaboration": self.collaboration,
            "adaptability": self.adaptability,
            "recommendation": self.recommendation
        }