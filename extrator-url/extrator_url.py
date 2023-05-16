import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não e Valida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return  url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_paramentro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_paramentro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

valor_dolar = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "real" and moeda_destino == "dolar":
    valor_em_real = int(quantidade) * valor_dolar
    print("O valor de conversão de real em dolar e igual a R$ {:.2f}".format(valor_em_real))
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_em_dolar = int(quantidade) / valor_dolar
    print("O valor de conversão de dolar em reais e igual a $ {:.2f} ".format(valor_em_dolar))
else:
    print("Conversão indisponivel")

#extrator_url_2 = ExtratorURL(url)
#print("O tamanaho da URL: ", len(extrator_url))
#print(extrator_url)
#print(extrator_url == extrator_url_2)
#valor_quantidade = extrator_url.get_valor_parametro("quantidade")
#print(valor_quantidade)