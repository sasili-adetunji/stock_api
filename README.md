## Stocks API
A stock broking api what will allow for administrator access, user access. The stockapi will allow for update of stocks. The api allow for query of of stock over a period of time

## Installation

- Download or clone the app to your local machine
- Move into local directory `cd stock_api`
- Ensure docker is running on your machine
- Run `chmod +x ./install.sh`
- Run the script `./install.sh`
- Run `docker-machine ip stockapi-dev` to get the IP Address.

## Endpoints
- Navigate to `IP_ADDRESS:5001/admin/login` to login as an admin access with the creadentials
    ```
    {
        "email": "admin@gmail.com",
        "password": "sasiliyu"
      }
- Grap the auth token returned.
- Naviigate to `IP_ADDRESS:5002/stocks/` using the auth token from above as a Bearer token in the authorization headers with a `POST` request of the format below
    ```
      {

        "stock_name": <STRING>,
        "opening_price": "XX.XX",
        "highest_price": "XX.XX",
        "lowest_price": "XX.XX",
        "closing_price": "XX.XX",
        "date": "YYYY-MM-DD"
      }
- Navigate to `IP_ADDRESS:5002/stocks/` with a  `GET` request to view all stocks
- Filter the stocks by date range `IP_ADDRESS:5002/stocks/?begin_date=YYYY-MM-DD&end_date=YYYY-MM-DD`
## Tests
- Run `chmod +x ./test.sh` to make the test script executable
- RUn `./test.sh dev` to run the test


### Technologies used
The functionality of this api depends on the following technologies.

- Flask
- Docker
- Postgres


## Author
This is done by `Sasiliyu Adetunji`

## License & Copyright
MIT © Sasiliyu Adetunji
Licensed under the MIT License.
