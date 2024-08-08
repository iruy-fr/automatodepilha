class NPDA:
    def __init__(self):
        # Inicializa a pilha como vazia e define o estado inicial como 'q0'
        self.pilha = []
        self.estado = 'q0'

    def transicao(self, simbolo):
        # Se estiver no estado 'q0'
        if self.estado == 'q0':
            if simbolo == 'a':
                # Se o símbolo for 'a', empilha 'A' e muda para o estado 'q1'
                self.pilha.append('A')
                self.estado = 'q1'
            elif simbolo == 'b':
                # Se o símbolo for 'b' sem ter encontrado 'a' antes, a entrada é inválida
                return False
        # Se estiver no estado 'q1'
        elif self.estado == 'q1':
            if simbolo == 'a':
                # Se o símbolo for 'a', empilha mais um 'A'
                self.pilha.append('A')
            elif simbolo == 'b':
                # Se o símbolo for 'b', verifica se há um 'A' correspondente na pilha
                if self.pilha and self.pilha[-1] == 'A':
                    self.pilha.pop()
                    self.estado = 'q2'
                else:
                    # Se a pilha não tiver um 'A' para emparelhar, a entrada é inválida
                    return False
        # Se estiver no estado 'q2'
        elif self.estado == 'q2':
            if simbolo == 'b':
                # Se o símbolo for 'b', verifica se há um 'A' correspondente na pilha
                if self.pilha and self.pilha[-1] == 'A':
                    self.pilha.pop()
                else:
                    # Se a pilha não tiver um 'A' para emparelhar, a entrada é inválida
                    return False
            else:
                # Se o símbolo for inválido no estado 'q2'
                return False
        return True

    def processar_entrada(self, cadeia):
        # Reinicia o estado para 'q0' e inicializa a pilha com o símbolo de base '$'
        self.estado = 'q0'
        self.pilha = ['$']  # Inicializa a pilha com o símbolo de base

        # Processa cada símbolo na cadeia de entrada
        for simbolo in cadeia:
            if not self.transicao(simbolo):
                return False

        # Verificação final (o estado deve ser 'q2' e a pilha deve conter apenas o símbolo de base)
        if self.estado == 'q2' and self.pilha == ['$']:
            return True
        return False

    def verificar_arquivo(caminho_arquivo):
        # Abre o arquivo para leitura
        try:
            with open(f'{caminho_arquivo}', 'r') as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    cadeia = linha.strip()  # Remove espaços em branco no início e no fim da linha
                    if cadeia:  # Ignora linhas vazias
                        resultado = npda.processar_entrada(cadeia)
                        print(f"Cadeia: '{cadeia}' -> {'Aceita' if resultado else 'Rejeitada'}")
        except FileNotFoundError:
            print(f"Arquivo {caminho_arquivo} não encontrado.")
        except Exception as e:
            print(f"Erro ao processar o arquivo: {e}")

def main():
    print("Verificador NPDA para a linguagem da forma a^n b^n")
    while True:
        entrada = input("Digite uma cadeia ou o caminho de um arquivo (ou 'exit' para sair): ").strip()
        if entrada.lower() == 'exit':
            print("Saindo...")
            break
        if not entrada:
            print("A entrada não pode ser vazia.")
            continue

        # Verifica se é um caminho de arquivo
        if entrada.endswith('.txt'):
            NPDA.verificar_arquivo(entrada)
        else:
            # Processa a entrada como uma cadeia de caracteres
            resultado = npda.processar_entrada(entrada)
            print(f"Cadeia: '{entrada}' -> {'Aceita' if resultado else 'Rejeitada'}")


if __name__ == "__main__":
    # Cria uma instância do NPDA e inicia o programa principal
    npda = NPDA()
    main()