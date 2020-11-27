DROP TABLE IF EXISTS vinyls;
DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS labels;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    artist_name VARCHAR(255)
);

CREATE TABLE labels (
    id SERIAL PRIMARY KEY,
    label_name VARCHAR(255)
);

CREATE TABLE vinyls (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist_id SERIAL REFERENCES artist(id) ON DELETE CASCADE,
    genre VARCHAR(255),
    price FLOAT,
    cost_price FLOAT,
    label_id SERIAL REFERENCES label(id) ON DELETE CASCADE,
    release_year INT
);