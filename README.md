RSS to Telegram News Bot

This project automates the process of fetching RSS feeds, processing the news data, and sending it to a Telegram channel. The script ensures news is sent only once by maintaining a record in a local SQLite database.

Features

•Fetches news from an RSS feed.
•Cleans and processes news content (removing unwanted characters).
•Converts publication dates to the Jalali calendar.
•Sends news messages (with or without images) to a Telegram channel.
•Avoids duplicate news by storing unique news IDs in a database.

Requirements

	•Python 3.12 or later
	•SQLite for local database storage
	•A .env file containing necessary API keys and configurations

Installation

1.Clone the repository:

	git clone <repository-url>
	cd <repository-name>
        
2.Install required dependencies:
        
	pip install -r requirements.txt

3.Create a .env file and configure the necessary variables:
  
        TELEGRAM_API_KEY=<your_telegram_api_key>
        TELEGRAM_CHAT_ID=<your_telegram_chat_id>
        RSS_URL=<rss_feed_url>

4.Verify the RSS_URL and ensure it points to a valid RSS feed.

File Structure

	•	main.py: Contains the main script logic.
	•	rss.py: Fetches the RSS feed.
	•	telegram.py: Sends messages and images to Telegram.
	•	db.py: Handles database operations (connection, table creation, checking, and inserting).
	•	utils.py: Contains helper functions (e.g., date conversion, generating unique IDs).
	•	settings.py: Stores configurable settings (e.g., RSS_URL).
	•	.env: Stores sensitive configurations (API keys, chat IDs, etc.).

Usage

	1.	Run the main.py to fetch news and send updates to Telegram:
        python main.py

	2.	The main.py will:
	•	Fetch the RSS feed.
	•	Process and format each news entry.
	•	Check if the news already exists in the database.
	•	Send the news to Telegram.
	•	Store the news in the database to prevent duplicates.

Code Overview

Database

The main uses an SQLite database (news.db) to store:
	•	Unique news IDs (uid)
	•	News titles
	•	News descriptions

This ensures duplicate news items are not sent to Telegram.

Error Handling

	•	Logs errors encountered during the process (e.g., failed message sends or database issues).
	•	Skips problematic news entries and continues processing the rest.

Contributing

	1.	Fork the repository.
	2.	Create a new branch for your feature or bugfix.
	3.	Submit a pull request with your changes.

License

This project is licensed under the MIT License. See the LICENSE file for details.

