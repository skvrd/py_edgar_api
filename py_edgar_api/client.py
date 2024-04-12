from typing import Optional

from requests import Session

from .company import Company

class Client():
    def __init__(self, company_name: str, email: str) -> None:
        self._company_name = company_name
        self._email = email
        self._session = Session()
        self._session.headers.update({
            'User-Agent': f'{self._company_name} (email: {self._email})'
        })

    def get_company(self, ticker: str) -> Optional[Company]:
        response = self._session.get('https://www.sec.gov/files/company_tickers.json')
        response.raise_for_status()
        companies = response.json()
        return next(
            (
                Company(company['cik_str'], company['title'])
                for company in companies.values() 
                if company['ticker'] == ticker
            ), None
        )