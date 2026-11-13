import os
import tempfile
from app import app

def cliente():
    db_fd, app.config["BIBLIO_DB"] = tempfile.mkstemp()
    app.config["TESTING"] = True
    client = app.test_client()
    yield client
    os.close(db_fd)
    os.unlink(app.config["BIBLIO_DB"])

def test_rota_saude():
    with app.test_client() as cliente_teste:
        resposta = cliente_teste.get("/saude")
        assert resposta.status_code == 200
