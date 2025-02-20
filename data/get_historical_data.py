import yfinance as yf
import datetime
import os

def download_forex_data(ticker, start_date, filename='forex_data.csv'):
    try:
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        forex_data = yf.download(ticker, start=start_date, end=today)

        if forex_data.empty:
            raise ValueError(f"No data available for {ticker} in the given date range.")
        
        forex_data.to_csv(filename)
        print(f"Data successfully downloaded and saved as {filename}")
        return forex_data

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    ticker = 'EURUSD=X'
    start_date = '2002-01-01'
    filename = 'EURUSD_data.csv'

    if os.path.exists(filename):
        user_input = input(f"{filename} already exists. Do you want to delete it and download new data? (y/n): ").lower()
        if user_input == 'y':
            os.remove(filename)
            print(f"{filename} deleted.")
        else:
            print("Download aborted.")
            return
    
    download_forex_data(ticker, start_date, filename)

if __name__ == "__main__":
    main()
