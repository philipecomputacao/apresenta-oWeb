create database cabrueira;
#default character set utf8;
#default collate utf8_general_ci;

use cabrueira;

create table aluno(
	id int primary key auto_increment,	
	nome varchar(40) not null,
	sexo enum('m', 'f') not null,
	telefone varchar(40) not null,
	email varchar (50) unique,
	data_nascimento date not null,
	data_matricula date not null,
	turma_fk int,
    desconto int,
	foreign key(turma_fk)
	references turma(id_turma)
	
);


create table pagamento(
	id int primary key auto_increment,	
	valor float(10,2) not null,
	data_pagamento date not null,
	id_aluno_fk int,
	foreign key(id_aluno_fk)
	references aluno(id_aluno)
);


create table turma(
	id int primary key auto_increment,	
	dia varchar(20) not null,
	horário varchar(10) not null,
	localidade varchar(20) not null
);


create table aula(
	id int primary key auto_increment,	
	dia date not null,
	turma_fk int,
	foreign key(turma_fk)
	references turma(id_turma)
	);

create table aluno_aula(	
	aluno int,
	foreign key(aluno_fk)
	references aluno(id_aluno),
	aula_fk int,
	foreign key(aula_fk)
	references aula(id_aula)
	);