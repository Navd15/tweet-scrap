## 1.  Install twint (twitter scrapper)
 - `git clone --depth=1 https://github.com/twintproject/twint.git`
 - `cd twint`
 - `pip3 install . -r requirements.txt`

## 2. Install other py packages 
- `pip install -r requirements.txt`
## 3. scrap tweets using twint
- `python scrap.py q=<keyword> since=<yyyy-mm-dd> until=<yyyy-mm-dd>`
## Above script will save csv file in the root dir with filename as `keyword.csv`
