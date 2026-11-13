import sqlite3
import os

CAMINHO = os.environ.get("BIBLIO_DB", "biblio.db")

def conectar():
    conexao = sqlite3.connect(CAMINHO)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criar_tabelas(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            login TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            perfil TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL,
            estoque_minimo INTEGER NOT NULL
        )
    """)
    conexao.commit()
