DROP TABLE IF EXISTS projeto;

CREATE TABLE projeto (
    id INTEGER ,
    nome TEXT PRIMARY KEY,
    membros TEXT NOT NULL
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
