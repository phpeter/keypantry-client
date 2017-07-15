Users:
	-id: serial
	-username: character varying(55)
	-passwordHash: character varying(255)

Items:
	-id: serial
	-name: character varying(55)
	-userId: int
	-key: int
	-own: boolean

CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username CHARACTER VARYING(55) NOT NULL,
	passwordHash CHARACTER VARYING(255) NOT NULL
)

CREATE TABLE items (
	id SERIAL PRIMARY KEY,
	name CHARACTER VARYING(55),
	userId INT,
	key INT,
	isOwned BOOLEAN
)