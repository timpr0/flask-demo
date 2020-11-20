-- Database: Bookstore
-- DROP DATABASE "Bookstore";
CREATE DATABASE "Bookstore"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Table: public.Autors
-- DROP TABLE public."Autors";
create table public."Autors"
(
    "ID"       bigint generated always as identity (maxvalue 2147483647)
        constraint "Autors_pkey"
            primary key,
    "Name"     text,
    "Lastname" text
);

alter table Authors
    owner to postgres;

-- Table: public.Books
-- DROP TABLE public."Books";
create table "Books"
(
    "ISBN"        bigint not null
        constraint "Books_pkey"
            primary key,
    "Title"       text,
    "Description" text,
    "Author"      bigint not null
        constraint author_fgnk
            references Authors
);

alter table "Books"
    owner to postgres;
