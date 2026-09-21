from aluno import Aluno
import csv


class Util:

    @staticmethod
    def limpar_cpf(cpf):
        return "".join(filter(str.isdigit, cpf))

    @staticmethod
    def mostrar_lista(lista):
        for aluno in lista:
            print(aluno)

    @staticmethod
    def carregar_arquivo_em_lista(nome_arquivo: str, lista: list) -> None:
        """Abre um arquivo CSV (nome,cpf), monta objetos Aluno e os adiciona na lista
        evitando duplicados com base no CPF.
        """
        try:
            with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
                # O DictReader mapeia as colunas baseado no cabeçalho do CSV
                leitor = csv.DictReader(arquivo)

                for linha in leitor:
                    # Extrai os dados do CSV (ajuste os nomes das chaves se o cabeçalho for diferente)
                    nome = linha["nome"].strip()
                    cpf = linha["cpf"].strip()
                    cpf = Util.limpar_cpf(cpf)

                    # Instancia o novo aluno
                    novo_aluno = Aluno(cpf=cpf, nome=nome)

                    # Graças ao seu __eq__, o 'in' vai comparar apenas os CPFs na lista
                    if novo_aluno not in lista:
                        lista.append(novo_aluno)

        except FileNotFoundError:
            print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        except KeyError as e:
            print(
                f"Erro: Verifique se o cabeçalho do CSV possui as colunas 'nome' e 'cpf'. Detalhe: {e}"
            )
    