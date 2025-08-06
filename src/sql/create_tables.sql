CREATE SCHEMA IF NOT EXISTS collections;
CREATE SCHEMA IF NOT EXISTS boosters;

CREATE TABLE collections.pokemon (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  rarity TEXT NOT NULL,
  type TEXT NOT NULL,
  set TEXT NOT NULL,
  quantity INTEGER NOT NULL,
  value FLOAT NOT NULL
);

CREATE TABLE collections.digimon (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  rarity TEXT NOT NULL,
  type TEXT NOT NULL,
  set TEXT NOT NULL,
  quantity INTEGER NOT NULL,
  value FLOAT NOT NULL
);

CREATE TABLE collections.disney_lorcana (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  rarity TEXT NOT NULL,
  type TEXT NOT NULL,
  set TEXT NOT NULL,
  quantity INTEGER NOT NULL,
  value FLOAT NOT NULL
);

CREATE TABLE collections.magic_the_gathering (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  rarity TEXT NOT NULL,
  type TEXT NOT NULL,
  set TEXT NOT NULL,
  quantity INTEGER NOT NULL,
  value FLOAT NOT NULL
);

CREATE TABLE boosters.history (
  id SERIAL PRIMARY KEY,
  game TEXT NOT NULL,
  set TEXT NOT NULL,
  date_added DATE NOT NULL,
  value FLOAT NOT NULL
);