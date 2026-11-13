
class ServicoProdutos:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def cadastrar(self, usuario, dados):
        if usuario.get("perfil") != "admin":
            raise PermissionError("Apenas administradores podem cadastrar produtos.")
        
        nome = dados.get("nome")
        preco = float(dados.get("preco", 0))
        estoque = int(dados.get("estoque", 0))
        estoque_minimo = int(dados.get("estoque_minimo", 0))

        if preco < 0 or estoque < 0:
            raise ValueError("Preço e estoque não podem ser negativos.")

        return self.repositorio.criar(nome, preco, estoque, estoque_minimo)
