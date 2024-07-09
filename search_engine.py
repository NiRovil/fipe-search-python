import requests

class Engine():
    def get_brand() -> list:
        req = requests.get('https://parallelum.com.br/fipe/api/v1/carros/marcas')
        return req.json()

    def get_model(brand: str) -> list:
        req = requests.get(f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{brand}/modelos')
        return req.json()

    def get_year(brand: str, model: str) -> list:
        req = requests.get(f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{brand}/modelos/{model}/anos')
        return req.json()

    def get_value(brand: str, model: str, year: str) -> list:
        req = requests.get(f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{brand}/modelos/{model}/anos/{year}')
        return req.json()