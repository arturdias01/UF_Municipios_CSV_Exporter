import requests
import csv
import shutil
import os



class Uf_requests: 
    def __init__(self, uf):  # Método construtor
        self.uf = uf
        self.link = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{self.uf.upper()}/municipios"
        self.data = requests.get(self.link).json()
        self.lista_municipios = []
        self.csv_files = os.path.dirname(os.path.abspath(__file__))
        self.csv_files_path = os.path.join(self.csv_files, 'csv_files')


    def print_municipios(self):  # Usar apenas para realizar testes
        for municipio in self.data:
            print(municipio['id'], municipio['nome'])
            self.lista_municipios.append([municipio['id'], municipio['nome']])


    def get_municipios(self):  # Para obter lista de municípios
        for municipio in self.data:
            self.lista_municipios.append([municipio['id'], municipio['nome']])  
        return self.lista_municipios

    
    def escrever_csv(self):  # Para criar o arquivo CSV e escrever os dados. 
        with open(f'ListaCidades{self.uf.upper()}.csv', mode='w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv, delimiter=',') 
            for municipio in self.lista_municipios:
                escritor.writerow(municipio)

        shutil.move(f'ListaCidades{self.uf.upper()}.csv', 'csv_files')  # Move o arquivo para a pasta csv_files     
        print(f'\nO arquivo foi movido para a pasta csv_files.\n')
              