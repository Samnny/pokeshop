--
-- PostgreSQL database dump
--

-- Dumped from database version 14.13 (Ubuntu 14.13-1.pgdg22.04+1)
-- Dumped by pg_dump version 16.6 (Ubuntu 16.6-0ubuntu0.24.04.1)

-- Started on 2025-03-03 13:00:36 -03

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 209 (class 1259 OID 25220)
-- Name: cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cliente (
    id integer NOT NULL,
    nome character varying NOT NULL,
    cpf bigint NOT NULL,
    endereco character varying NOT NULL,
    email character varying NOT NULL,
    senha character varying NOT NULL
);


ALTER TABLE public.cliente OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 25225)
-- Name: comentario_poke; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.comentario_poke (
    id integer NOT NULL,
    data date NOT NULL,
    pokemon_id integer NOT NULL,
    cliente_id integer NOT NULL,
    texto character varying
);


ALTER TABLE public.comentario_poke OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 25228)
-- Name: comentario_publicacao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.comentario_publicacao (
    id integer NOT NULL,
    data date NOT NULL,
    cliente_id integer NOT NULL,
    publicacao_id integer NOT NULL,
    texto character varying
);


ALTER TABLE public.comentario_publicacao OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 25231)
-- Name: pokemon; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pokemon (
    id integer NOT NULL,
    nome character varying NOT NULL,
    descricao character varying NOT NULL,
    altura numeric NOT NULL,
    peso numeric NOT NULL,
    preco numeric NOT NULL,
    tipo_1 character varying NOT NULL,
    tipo_2 character varying,
    genero_1 character varying,
    genero_2 character varying,
    avaliacao numeric
);


ALTER TABLE public.pokemon OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 25236)
-- Name: publicacao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.publicacao (
    id integer NOT NULL,
    data date NOT NULL,
    texto character varying,
    foto bytea,
    cliente_id integer NOT NULL
);


ALTER TABLE public.publicacao OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 25241)
-- Name: ter; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ter (
    pokemon_id integer NOT NULL,
    venda_id integer NOT NULL,
    quantidade integer NOT NULL
);


ALTER TABLE public.ter OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 25244)
-- Name: venda; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.venda (
    id integer NOT NULL,
    local_de_entrega character varying NOT NULL,
    data date NOT NULL,
    cliente_id integer NOT NULL
);


ALTER TABLE public.venda OWNER TO postgres;

--
-- TOC entry 3393 (class 0 OID 25220)
-- Dependencies: 209
-- Data for Name: cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.cliente (id, nome, cpf, endereco, email, senha) VALUES (1, 'Dante Lourenço', 16267523039, 'Rua Júlio Barbosa de Carvalho', 'dantelgrk@gmail.com', '123');
INSERT INTO public.cliente (id, nome, cpf, endereco, email, senha) VALUES (2, 'Dafne Freitas', 38213851030, 'Rua Cleber Maia Cabral', 'dafnekrg@gmail.com', '123');
INSERT INTO public.cliente (id, nome, cpf, endereco, email, senha) VALUES (4, 'Agnes Souza', 21948537079, 'Travessa Jacó', 'agnestft@outlook.com', '123');
INSERT INTO public.cliente (id, nome, cpf, endereco, email, senha) VALUES (5, 'Dominic Alencar', 51834527090, 'Avenida Desembargador Adalberto Barros Leal', 'domalenc@protonmail.com', '123');
INSERT INTO public.cliente (id, nome, cpf, endereco, email, senha) VALUES (3, 'Anakin Oliveira', 94344567030, 'Travessa Zoraida Barbosa', 'anakinstw@outlook.com', '123');


--
-- TOC entry 3394 (class 0 OID 25225)
-- Dependencies: 210
-- Data for Name: comentario_poke; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3395 (class 0 OID 25228)
-- Dependencies: 211
-- Data for Name: comentario_publicacao; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3396 (class 0 OID 25231)
-- Dependencies: 212
-- Data for Name: pokemon; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.pokemon (id, nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao) VALUES (1, 'Bulbassauro', 'Uma semente estranha foi plantada nas suas costas quando nasceu. A planta brota e cresce com este Pokémon.', 0.7, 6.9, 300, 'Grama', 'Veneno', 'Macho', NULL, NULL);
INSERT INTO public.pokemon (id, nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao) VALUES (2, 'Ivyssauro', 'Quando o bulbo nas costas cresce, parece perder a capacidade de ficar em pé nas patas traseiras.', 1.0, 13, 600, 'Grama', 'Veneno', 'Macho', NULL, NULL);
INSERT INTO public.pokemon (id, nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao) VALUES (3, 'Venussauro', 'A planta floresce quando está absorvendo energia solar. Ele permanece em movimento para buscar a luz do sol.', 2.0, 100, 900, 'Grama', 'Veneno', 'Macho', NULL, NULL);
INSERT INTO public.pokemon (id, nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao) VALUES (4, 'Charmander', 'Obviamente prefere lugares quentes. Quando chove, diz-se que o vapor jorra da ponta de sua cauda.', 0.6, 8.5, 300, 'fogo', NULL, 'Macho', NULL, NULL);
INSERT INTO public.pokemon (id, nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao) VALUES (5, 'Charmeleon', 'Quando balança sua cauda ardente, a temperatura ao seu redor sobe cada vez mais, atormentando seus oponentes.', 1.1, 19, 600, 'fogo', NULL, 'Macho', NULL, NULL);
INSERT INTO public.pokemon (id, nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao) VALUES (6, 'Charizard', 'Se Charizard ficar realmente irritado, a chama na ponta de sua cauda queima em um tom azul claro.', 1.7, 90.5, 900, 'fogo', 'Voador', 'Macho', NULL, NULL);
INSERT INTO public.pokemon (id, nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao) VALUES (7, 'Squirtle', 'Após o nascimento, suas costas incham e endurecem em uma concha. Ele borrifa uma espuma potente de sua boca.', 0.5, 9, 300, 'Água', NULL, 'Macho', NULL, NULL);
INSERT INTO public.pokemon (id, nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao) VALUES (8, 'Wartortle', 'A cauda longa e peluda de Wartortle é um símbolo de longevidade, então este Pokémon é bastante popular entre as pessoas mais velhas.', 1.0, 22.5, 600, 'Água', NULL, 'Macho', NULL, NULL);
INSERT INTO public.pokemon (id, nome, descricao, altura, peso, preco, tipo_1, tipo_2, genero_1, genero_2, avaliacao) VALUES (9, 'Blastoise', 'Ele aumenta deliberadamente seu peso corporal para que possa suportar o recuo dos jatos de água que dispara.', 1.6, 85.5, 900, 'Água', NULL, 'Macho', NULL, NULL);


--
-- TOC entry 3397 (class 0 OID 25236)
-- Dependencies: 213
-- Data for Name: publicacao; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.publicacao (id, data, texto, foto, cliente_id) VALUES (289426872, '2025-03-02', 'teste', '\x', 1);
INSERT INTO public.publicacao (id, data, texto, foto, cliente_id) VALUES (1482593948, '2025-03-03', 'outro teste', '\x', 1);


--
-- TOC entry 3398 (class 0 OID 25241)
-- Dependencies: 214
-- Data for Name: ter; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.ter (pokemon_id, venda_id, quantidade) VALUES (1, 118201139, 10);
INSERT INTO public.ter (pokemon_id, venda_id, quantidade) VALUES (1, 1705418397, 5);


--
-- TOC entry 3399 (class 0 OID 25244)
-- Dependencies: 215
-- Data for Name: venda; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.venda (id, local_de_entrega, data, cliente_id) VALUES (2, 'Travessa Jacó', '2025-02-02', 4);
INSERT INTO public.venda (id, local_de_entrega, data, cliente_id) VALUES (3, 'Rua Cleber Maia Cabral', '2025-02-02', 2);
INSERT INTO public.venda (id, local_de_entrega, data, cliente_id) VALUES (4, 'Travessa Zoraida Barbosa', '2025-01-01', 3);
INSERT INTO public.venda (id, local_de_entrega, data, cliente_id) VALUES (5, 'Travessa Zoraida Barbosa', '2025-02-18', 3);
INSERT INTO public.venda (id, local_de_entrega, data, cliente_id) VALUES (1, 'Rua Júlio Barbosa de Carvalho', '2025-01-17', 1);
INSERT INTO public.venda (id, local_de_entrega, data, cliente_id) VALUES (118201139, 'rua tal', '2025-02-28', 2);
INSERT INTO public.venda (id, local_de_entrega, data, cliente_id) VALUES (1705418397, 'Teste', '2025-03-03', 1);


--
-- TOC entry 3233 (class 2606 OID 25250)
-- Name: cliente cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (id);


--
-- TOC entry 3235 (class 2606 OID 25252)
-- Name: comentario_poke comentario_poke_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comentario_poke
    ADD CONSTRAINT comentario_poke_pkey PRIMARY KEY (id);


--
-- TOC entry 3237 (class 2606 OID 25254)
-- Name: comentario_publicacao comentario_publicacao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comentario_publicacao
    ADD CONSTRAINT comentario_publicacao_pkey PRIMARY KEY (id);


--
-- TOC entry 3239 (class 2606 OID 25256)
-- Name: pokemon pokemon_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pokemon
    ADD CONSTRAINT pokemon_pkey PRIMARY KEY (id);


--
-- TOC entry 3241 (class 2606 OID 25258)
-- Name: publicacao publicacao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publicacao
    ADD CONSTRAINT publicacao_pkey PRIMARY KEY (id);


--
-- TOC entry 3243 (class 2606 OID 25260)
-- Name: ter ter_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ter
    ADD CONSTRAINT ter_pkey PRIMARY KEY (pokemon_id, venda_id);


--
-- TOC entry 3245 (class 2606 OID 25262)
-- Name: venda venda_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.venda
    ADD CONSTRAINT venda_pkey PRIMARY KEY (id);


--
-- TOC entry 3246 (class 2606 OID 25263)
-- Name: comentario_poke cliente_cliente_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comentario_poke
    ADD CONSTRAINT cliente_cliente_id_fk FOREIGN KEY (cliente_id) REFERENCES public.cliente(id) ON UPDATE CASCADE NOT VALID;


--
-- TOC entry 3250 (class 2606 OID 25268)
-- Name: publicacao cliente_cliente_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publicacao
    ADD CONSTRAINT cliente_cliente_id_fk FOREIGN KEY (cliente_id) REFERENCES public.cliente(id) ON UPDATE CASCADE;


--
-- TOC entry 3248 (class 2606 OID 25273)
-- Name: comentario_publicacao cliente_cliente_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comentario_publicacao
    ADD CONSTRAINT cliente_cliente_id_fk FOREIGN KEY (cliente_id) REFERENCES public.cliente(id) ON UPDATE CASCADE;


--
-- TOC entry 3247 (class 2606 OID 25278)
-- Name: comentario_poke pokemon_pokemon_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comentario_poke
    ADD CONSTRAINT pokemon_pokemon_id_fk FOREIGN KEY (pokemon_id) REFERENCES public.pokemon(id) ON UPDATE CASCADE;


--
-- TOC entry 3251 (class 2606 OID 25283)
-- Name: ter pokemon_pokemon_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ter
    ADD CONSTRAINT pokemon_pokemon_id_fk FOREIGN KEY (pokemon_id) REFERENCES public.pokemon(id) ON UPDATE CASCADE;


--
-- TOC entry 3249 (class 2606 OID 25288)
-- Name: comentario_publicacao publicacao_publicacao_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comentario_publicacao
    ADD CONSTRAINT publicacao_publicacao_id_fk FOREIGN KEY (publicacao_id) REFERENCES public.publicacao(id) ON UPDATE CASCADE NOT VALID;


--
-- TOC entry 3253 (class 2606 OID 25293)
-- Name: venda venda_cliente_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.venda
    ADD CONSTRAINT venda_cliente_id_fk FOREIGN KEY (cliente_id) REFERENCES public.cliente(id) ON UPDATE CASCADE NOT VALID;


--
-- TOC entry 3252 (class 2606 OID 25298)
-- Name: ter venda_venda_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ter
    ADD CONSTRAINT venda_venda_id_fk FOREIGN KEY (venda_id) REFERENCES public.venda(id) ON UPDATE CASCADE;


--
-- TOC entry 3405 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2025-03-03 13:00:36 -03

--
-- PostgreSQL database dump complete
--

