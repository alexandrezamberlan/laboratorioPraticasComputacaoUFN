

class Aluno:

    def __init__(self, cpf: str, nome: str):
        # Usando a função anterior para garantir que o CPF fique apenas com números
        self.cpf = cpf
        self.nome = nome.upper()

    def __eq__(self, outro: object) -> bool:
        """Define a igualdade baseada estritamente no CPF."""
        if not isinstance(outro, Aluno):
            return False
        return self.cpf == outro.cpf

    def __hash__(self) -> int:
        """Permite o uso em estruturas como sets e chaves de dicionários."""
        return hash(self.cpf)

    def __lt__(self, outro: "Aluno") -> bool:
        """Define a ordenação padrão baseada no nome (ordem alfabética)."""
        if not isinstance(outro, Aluno):
            return NotImplemented
        return self.nome.lower() < outro.nome.lower()

    def __repr__(self) -> str:
        return f"Aluno(nome='{self.nome}', cpf='{self.cpf}')"