
class ProdutoRepositorio:
    def __init__(self, conexao):
        self.conexao = conexao

    def listar(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT id, nome, preco, estoque, estoque_minimo FROM produtos")
        return cursor.fetchall()

    def criar(self, nome, preco, estoque, estoque_minimo):
        cursor = self.conexao.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, preco, estoque, estoque_minimo) VALUES (?, ?, ?, ?)",
            (nome, preco, estoque, estoque_minimo)
        )
        self.conexao.commit()
        return cursor.lastrowid
