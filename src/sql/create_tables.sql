CREATE SCHEMA IF NOT EXISTS collections;
CREATE SCHEMA IF NOT EXISTS boosters;

CREATE TABLE collections.pokemon (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  rarity TEXT NOT NULL,
  type TEXT NOT NULL,
  set TEXT NOT NULL,
  quantity INTEGER NOT NULL,
  value FLOAT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_message TEXT,
  price_history FLOAT[],
  CONSTRAINT unique_pokemon_card_entry UNIQUE (name, rarity, type, set)
);

CREATE TABLE collections.digimon (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  rarity TEXT NOT NULL,
  type TEXT NOT NULL,
  set TEXT NOT NULL,
  quantity INTEGER NOT NULL,
  value FLOAT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_message TEXT,
  price_history FLOAT[],
  CONSTRAINT unique_digimon_card_entry UNIQUE (name, rarity, type, set)
);

CREATE TABLE collections.disney_lorcana (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  rarity TEXT NOT NULL,
  type TEXT NOT NULL,
  set TEXT NOT NULL,
  quantity INTEGER NOT NULL,
  value FLOAT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_message TEXT,
  price_history FLOAT[],
  CONSTRAINT unique_disney_lorcana_card_entry UNIQUE (name, rarity, type, set)
);

CREATE TABLE collections.magic_the_gathering (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  rarity TEXT NOT NULL,
  type TEXT NOT NULL,
  set TEXT NOT NULL,
  quantity INTEGER NOT NULL,
  value FLOAT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_message TEXT,
  price_history FLOAT[],
  CONSTRAINT unique_magic_the_gathering_card_entry UNIQUE (name, rarity, type, set)
);

CREATE TABLE boosters.history (
  id SERIAL PRIMARY KEY,
  game TEXT NOT NULL,
  set TEXT NOT NULL,
  date_added DATE NOT NULL,
  value FLOAT NOT NULL
);

CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = CURRENT_TIMESTAMP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_updated_at
BEFORE UPDATE ON collections.pokemon
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at
BEFORE UPDATE ON collections.digimon
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at
BEFORE UPDATE ON collections.disney_lorcana
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_updated_at
BEFORE UPDATE ON collections.magic_the_gathering
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();