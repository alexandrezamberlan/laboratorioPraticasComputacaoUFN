from util import Util

# 1. Organização dos arquivos em um dicionário para evitar índices manuais (lista_arquivos[1], etc)
MAPEAMENTO_ARQUIVOS = {
    "inscritos": "arquivo_inscritos.csv",
    "terca_manha": "arquivo_presenca_terca_m.csv",
    "terca_noite": "arquivo_presenca_terca_n.csv",  # Adicionado .csv
    "quarta_manha": "arquivo_presenca_quarta_m.csv",  # Adicionado .csv
    "quarta_noite": "arquivo_presenca_quarta_n.csv",  # Adicionado .csv
}

# 2. Inicialização das listas
lista_inscritos = []
lista_terca_manha = []
lista_terca_noite = []
lista_quarta_manha = []
lista_quarta_noite = []

# 3. Carregamento dos dados usando o mapeamento claro
Util.carregar_arquivo_em_lista(
    MAPEAMENTO_ARQUIVOS["inscritos"], lista_inscritos
)
Util.carregar_arquivo_em_lista(
    MAPEAMENTO_ARQUIVOS["terca_manha"], lista_terca_manha
)
Util.carregar_arquivo_em_lista(
    MAPEAMENTO_ARQUIVOS["terca_noite"], lista_terca_noite
)
Util.carregar_arquivo_em_lista(
    MAPEAMENTO_ARQUIVOS["quarta_manha"], lista_quarta_manha
)
Util.carregar_arquivo_em_lista(
    MAPEAMENTO_ARQUIVOS["quarta_noite"], lista_quarta_noite
)

# 4. Ordenação e exibição (Usando o __lt__ que criamos antes)
lista_terca_manha.sort()
Util.mostrar_lista(lista_terca_manha)

# 5. Otimização de Performance: Criar conjuntos (sets) para busca rápida O(1)
# Buscar usando 'in' em listas dentro de um loop pode ser muito lento se houver muitos alunos.
# Como Aluno tem __hash__, podemos transformá-los em sets temporariamente.
sets_presenca = [
    set(lista_terca_manha),
    set(lista_terca_noite),
    set(lista_quarta_manha),
    set(lista_quarta_noite),
]

lista_nao_atestado = []

# 6. Filtragem de alunos com menos de 3 presenças
for inscrito in lista_inscritos:
    # Sum soma 1 para cada True retornado na validação rápida do set
    total_presencas = sum(inscrito in lista_set for lista_set in sets_presenca)

    if total_presencas < 3:
        lista_nao_atestado.append(inscrito)
