CREATE TABLE IF NOT EXISTS public.people
(
    people_id character varying(32) COLLATE pg_catalog."default" NOT NULL,
    name character varying(45) COLLATE pg_catalog."default" NOT NULL,
    gender character varying(1) COLLATE pg_catalog."default" NOT NULL,
    contact_number character varying(15) COLLATE pg_catalog."default" NOT NULL,
    address character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT people_pkey PRIMARY KEY (people_id)
)

TABLESPACE pg_default;


CREATE TABLE IF NOT EXISTS public.place
(
    place_id character varying(48) COLLATE pg_catalog."default" NOT NULL,
    place_name character varying(45) COLLATE pg_catalog."default" NOT NULL,
    address character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT place_pkey PRIMARY KEY (place_id)
)

TABLESPACE pg_default;

CREATE TABLE IF NOT EXISTS public.trace
(
    people_id character varying(32) COLLATE pg_catalog."default" NOT NULL,
    place_id character varying(48) COLLATE pg_catalog."default" NOT NULL,
    "time" timestamp without time zone NOT NULL,
    CONSTRAINT trace_pkey PRIMARY KEY (people_id, place_id, "time"),
    CONSTRAINT trace_people_id_fkey FOREIGN KEY (people_id)
        REFERENCES public.people (people_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT trace_place_id_fkey FOREIGN KEY (place_id)
        REFERENCES public.place (place_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;