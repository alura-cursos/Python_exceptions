class LeitorDeArquivo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        print(f'Abrindo arquivo: {self.arquivo}')
    
    def ler_proxima_linha(self):
        print('Lendo linha...')
        raise IOError()
        return 'Linha de arquivo'

    def fechar(self):
        print('Fechando arquivo.')
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, valor, traceback):
        print("fechando arquivo")