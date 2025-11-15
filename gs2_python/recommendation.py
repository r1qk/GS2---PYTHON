#Possíveis recomendações
class career:
    def __init__ (self, top1, top2):
        self.top1 = top1
        self.top2 = top2

    def advice (self):
        if self.top1 == "Lógica" and self.top2 == "Criatividade":
            profissao = "Desenvolvedor Full Stack, Cientista de Dados ou Engenheiro de Machine Learning"

        elif self.top1 == "Criatividade" and self.top2 == "Lógica":
            profissao = "Desenvolvedor Full Stack ou Desenvolvedor de Jogos"
        
        elif self.top1 == "Lógica" and self.top2 == "Colaboração":
            profissao = "Analista de Sistemas ou Desenvolvedor Back-end colaborativo"
        
        elif self.top1 == "Colaboração" and self.top2 == "Lógica":
            profissao = "Analista de Negócios ou Scrum Master técnico"
        
        elif self.top1 == "Criatividade" and self.top2 == "Colaboração":
            profissao = "UX/UI Designer ou Front-end Designer"
        
        elif self.top1 == "Colaboração" and self.top2 == "Criatividade":
            profissao = "Product Designer ou UX Researcher"
        
        elif self.top1 == "Colaboração" and self.top2 == "Adaptabilidade":
            profissao = "Scrum Master ou Product Owner"
        
        elif self.top1 == "Adaptabilidade" and self.top2 == "Colaboração":
            profissao = "Gestor de Projetos de TI ou Analista de Processos"
        
        elif self.top1 == "Adaptabilidade" and self.top2 == "Criatividade":
            profissao = "Designer de inovação ou Consultor de Transformação Digital"
        
        elif self.top1 == "Criatividade" and self.top2 == "Adaptabilidade":
            profissao = "UX Researcher ou Arquiteto de Soluções"
        
        elif self.top1 == "Adaptabilidade" and self.top2 == "Lógica":
            profissao = "Suporte Técnico ou DevOps Júnior"
        
        elif self.top1 == "Lógica" and self.top2 == "Adaptabilidade":
            profissao = "Engenheiro de Infraestrutura ou Administrador de Sistemas"
        
        else:
            profissao = "Profissões generalistas de TI (Analista de Sistemas, Técnico de TI)"

        return profissao

        