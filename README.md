---

# Google News Scraper and SQLite Storage

## Overview

This Python script allows users to search for news articles related to specific keywords on Google News, process the articles, and save the content into a SQLite database. The code uses the `GoogleNews` library to fetch the news, `requests-html` for parsing the HTML content of the news websites, and `sqlite3` to store the data in a local database.

---

## Key Features

- **Dynamic Keyword Search**

  Users are prompted to enter a keyword to search for news articles on Google News.

- **News Retrieval**

  Articles related to the entered keyword are fetched using the `GoogleNews` library.

- **HTML Parsing**

  The script uses an asynchronous HTML session (`AsyncHTMLSession`) to scrape and parse the content of individual news articles.

- **SQLite Integration**

  The scraped article data (keyword, URL, title, and content) is stored in a SQLite database (`news.db`) for further use.

- **Paragraph Segmentation**

  Each paragraph in the article content is separated by "####" for clear identification.

---

## Prerequisites

Make sure the following Python libraries are installed before running the script:

- `GoogleNews`  
  Install with:

  ```bash
  pip install GoogleNews
  ```

- `requests-html`  
  Install with:

  ```bash
  pip install requests-html
  ```

- `sqlite3` (No installation required—it’s built into Python.)

---

## How to Use the Code

1. **Run the Script**  
   Execute the Python script in your terminal or IDE. When prompted, enter a keyword to search for news articles.

   **Example Input**:  

   ```
   Enter your keyword to search in google news  
   => Technology
   ```

2. **Confirm Your Keyword**  
   After entering the keyword, the script will ask if you'd like to proceed with the input or enter a new keyword.

   **Example Confirmation**:  

   ```
   Do you want to Continue?  
   Enter y to continue or n to enter the keyword again  
   => y
   ```

3. **Data Storage**  
   Once confirmed, the script will fetch news articles, scrape their content, and store the data (keyword, URL, title, and article content) in a SQLite database named `news.db`.

4. **First-Time Setup**  
   If you are running the script for the first time, you need to create the `news` table in your SQLite database. Uncomment the following section in the script under the comment "First-Time Setup":

   ```python
   c.execute("""CREATE TABLE news (
       keyword TEXT,
       url TEXT,
       title TEXT,
       content TEXT
   )""")
   ```

   Then execute your script once to initialize the database schema.

---

## SQLite Database Table Schema

The SQLite database `news.db` contains a single table named `news` which stores the fetched news articles. Below is the table schema:

| Column   | Data Type | Description                              |
|----------|-----------|------------------------------------------|
| keyword  | TEXT      | The keyword used for the search query    |
| url      | TEXT      | The URL of the news article              |
| title    | TEXT      | The title of the news article            |
| content  | TEXT      | The full scraped content of the article  |

---

## Code Workflow

1. **User Input**  
   - Prompts the user to input a keyword to search for news on Google News.  

2. **Search and Fetch Results**  
   - Uses the `GoogleNews` library to fetch articles related to the user's keyword.

3. **Scrape HTML Content**  
   - Creates an asynchronous session and parses the content of each news article.

4. **Save to SQLite Database**  
   - Stores the data (keyword, URL, article title, and content) in a local SQLite database (`news.db`).

5. **Output**  
   - Prints the title and link of each article in the console for transparency.

---

## Notes and Considerations

- **Article Accessibility**  
  Some articles may not allow scraping, or the request might be blocked by the target website. Ensure the website's terms of service allow web scraping.

- **HTTPS URLs**  
  The script assumes `http://` URLs by default, which might result in errors if the links are `https://`. You may need to modify this part in the script:

  ```python
  url="http://"+info['link']
  ```

  Replace it with:

  ```python
  url="https://"+info['link']
  ```

- **Database Setup**  
  Make sure you only run the `CREATE TABLE` block once. Running it again without modifications will raise an error if the table already exists.

---

## Example Output

When the script is executed successfully, it displays the following information in the terminal for each fetched article:

- **Title**: Displays the title of the news article.
- **URL**: Displays the link to the article.

Here’s an example:

```
Google releases new Pixel phones
https://www.example.com/pixel-news
```

Additionally, all this data is stored in the SQLite database (`news.db`).

---

## Potential Enhancements

This script provides a simple way to fetch and store news data. In the future, the following potential improvements can be added:

1. **Error Handling**  
   Add exception handling for network errors, invalid URLs, and database-related issues.

2. **Pagination**  
   Fetch more articles by adding pagination support in the `GoogleNews` request.

3. **Avoid Duplication**  
   Prevent duplicate entries in the SQLite database by using unique constraints or data validation.

4. **Database Updates**  
   Add features to update or delete existing records in the SQLite database.

5. **User Interface**  
   Enhance the user experience by adding a graphical user interface (GUI) or interactive CLI menus.

---

## License

Feel free to use or modify this code for personal or educational purposes. When using it for anything beyond personal use, consider adhering to the terms of use of Google News and the websites you scrape.

---
