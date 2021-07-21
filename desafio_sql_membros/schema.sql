DROP TABLE IF EXISTS projeto;

CREATE TABLE projeto (
    id INTEGER,
    nome TEXT PRIMARY KEY,
    descricao TEXT NOT NULL
);

DROP TABLE IF EXISTS membro;

CREATE TABLE membro (
    id INTEGER,
    nome TEXT PRIMARY KEY,
    linguagem TEXT NOT NULL
);

DROP TABLE IF EXISTS modelo;

CREATE TABLE modelo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    area_aplicacao TEXT NOT NULL,
    projeto_nome TEXT,
    FOREIGN KEY (projeto_nome) REFERENCES projeto(nome)
);

DROP TABLE IF EXISTS participacao;

CREATE TABLE participacao (
    projeto_nome TEXT NOT NULL,
    membro_nome TEXT NOT NULL,
    FOREIGN KEY (projeto_nome) REFERENCES projeto(nome),
    FOREIGN KEY (membro_nome) REFERENCES membro(nome)
);


