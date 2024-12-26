# MyMusicFy

MyMusicFy is a Python application that processes and analyzes music metadata from the Music Metadata Zip files to produce interesting statistics about artists, albums, and songs.

## Features

- Retrieve detailed statistics about a specific artist.
- Get genre-based statistics, including popularity and album distribution.
- Analyze explicit song distribution.
- Calculate average tracks per album.

## Dataset

This project uses CSV files from the Music Metadata Zip:
- `albums.csv`
- `artists.csv`
- `releases.csv`
- `songs.csv`
- `tracks.csv`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/mymusicfy.git
   cd mymusicfy
    ```
2. Usage

Create a virtual environment: Run the following command to create a new virtual environment. Replace .venv with the name of your environment.

```cmd
python -m venv .venv
```
If you are using python3, use that instead:

```cmd
python3 -m venv .venv
```
Activate the virtual environment: To activate the environment, run the following command (use the appropriate one depending on whether you're in CMD or PowerShell):

CMD:
```cmd
.venv\Scripts\activate
```
PowerShell:

```powershell
.\.venv\Scripts\Activate
```
After activation, you'll see the virtual environment name (.venv) appear at the start of your prompt.

2. Install dependencies:

```bash
pip install -r requirements.txt
Place the metadata files into the data/ directory.
```
(for testing use requirements_test.txt)

Deactivate the virtual environment: To deactivate the virtual environment when you're done, simply run:

For deactivating

```cmd
deactivate
```

4. Run example
Run the examples in app.py to explore the dataset.

