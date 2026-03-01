# Homework 06

This repository contains a Python script for retrieving biological sequence data from NCBI and managing it using a Redis database.

## Scripts Overview

### 1. `get_ncbi_genbank_records.py`

**Input:** NCBI Protein Database (API)  
**Output:** Formatted text file (`genbank_records.txt`)  

This script automates the retrieval of protein data and utilizes a local Redis instance for data persistence. It performs the following:

- Searches NCBI for Arabidopsis thaliana proteins related to gene AT5G10140
- Fetches full GenBank records for the discovered sequences
- Stores record metadata and sequences in Redis as JSON strings
- Generates a text report containing the ID, Name, Description, and Sequence

## Function Descriptions

### 1. `get_records`

**Returns:** Tuple containing a list of SeqRecord objects and a list of GI IDs

This function handles the communication with the NCBI Entrez API. It first searches for the relevant protein IDs and then downloads the full GenBank records, parsing them into BioPython objects.

### 2. `store_and_write_records`

**Parameters:** List of IDs, List of SeqRecords, Output filename  

This function manages the database and file output. It iterates through the records to store them in a local Redis database using the GI ID as the key. It then reads the data back from Redis to ensure the final text file is written in the correct order.

### 3. `main`

**Parameters:** None

The main execution function that sets the configuration for the script. It defines the output file path, coordinates the flow of data between functions, and handles command-line arguments for different logging levels.

---

## Running the Redis Container

This assignment uses Docker Compose to manage the Redis database.

1. **Start the Database:**
   'docker compose up -d'

2. **Verify it is Running:**
   'docker ps'

3. **Stop the Database:**
   'docker compose down'

   