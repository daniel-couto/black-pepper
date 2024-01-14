// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table conta {
  id integer [primary key]
  agencia integer
  conta timestamp 
  nome varchar
  instituicao_id integer
}

Table instituicao {
  id integer [primary key]
  nome varchar
}

Ref: conta.instituicao_id > instituicao.id // many-to-one
