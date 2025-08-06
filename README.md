# card_management

## Overview

A web application to manage your Trading Card Game (TCG) collection, supporting Magic the Gathering, Pokemon, Disney Lorcana, and Digimon. The app uses a PostgreSQL database to store your collection data and fetches card prices using the [JUSTTCG API](https://justtcg.com/).

---

## Database Setup

### 1. Configure the Database

You can use the provided GUI script to configure your PostgreSQL database credentials and create the `creds` pickle file.

**Run the configuration GUI:**
```sh
python src/utils/db_config_gui.py
```
This script will prompt you for:
- Database name
- User
- Password
- Host
- Port

It will save your credentials to `src/data/creds/database.pkl`.

---

### 2. Create the Tables

After configuring your credentials, create the necessary tables in your PostgreSQL database using the provided `create_tables.sql` script:

```sh
psql -U your_user -d your_database -f create_tables.sql
```

Replace `your_user` and `your_database` with your PostgreSQL username and database name.

---

## JUSTTCG API Setup

This app uses the [JUSTTCG API](https://justtcg.com/) to fetch card prices.  
**You must obtain an API key from JUSTTCG and save it as a pickle file:**

1. Register and get your API key from [JUSTTCG](https://justtcg.com/).
2. Save your API key in a pickle file at `src/utils/justtcg.pkl`:
    ```python
    import pickle
    with open("src/utils/justtcg.pkl", "wb") as f:
        pickle.dump("YOUR_API_KEY_HERE", f)
    ```
3. Replace `"YOUR_API_KEY_HERE"` with your actual API key.

---

## Running the App

1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Start the Flask app:**
    ```sh
    python src/main.py
    ```

3. **Open your browser and go to:**
    ```
    http://127.0.0.1:5000/
    ```

---

## Features

- Dashboard with total value and card count
- Stats by TCG
- Add booster packs via a user-friendly modal
- PostgreSQL backend for robust data storage
- Card price fetching via JUSTTCG API

---

## Notes

- Make sure your PostgreSQL server is running and accessible.
- The app expects the database tables to match the CSV column structure.
- You must have a valid JUSTTCG API key for price fetching.

---

