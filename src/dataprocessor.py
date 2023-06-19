import statistics as st
import math as m
import matplotlib.pyplot as plt
import numpy as np


class DataProcessor:
    def detect_outliers(self, data):
        Q1 = st.quantiles(data)[0]
        Q3 = st.quantiles(data)[2]
        A = Q3 - Q1
        i = 0
        count_outlier_moderado = 0
        count_outlier_extremo = 0
        count_total_outliers = 0
        while i < len(data):
            value = data[i]
            if value < Q1 - 1.5 * A or value > Q3 + 1.5 * A:
                # print(value, " - Outlier Moderado")
                count_outlier_moderado += 1
                count_total_outliers += 1
            if value < Q1 - 3 * A or value > Q3 + 3 * A:
                # print(value, " - Outlier Extremo")
                count_outlier_extremo += 1
                count_total_outliers += 1
            i += 1
        print("Total de Outliers Moderados: ", count_outlier_moderado)
        print("Total de Outliers Extremos: ", count_outlier_extremo)
        print("Total de Outliers: ", count_total_outliers)

    def getMean(self, data):
        return st.mean(data)
    
    def getMedian(self, data):
        return st.median(data)
    
    def getMode(self, data):
        return st.mode(data)
    
    def getStDev(self, data):
        return st.stdev(data)
    
    def getMin(self, data):
        return min(data)
    
    def getMax(self, data):
        return max(data)
    
    def getLen(self, data):
        print("Quantidade de dados:", len(data))
        return len(data)

    def processAndRemoveOutliers(self, data):
        self.detect_outliers(data)
        self.removeOutlierExtremo(data)

    def getNumClasses(self, n):
        log = m.log10(n)
        k = 1 + 3.3 * log
        # print("Valor de k: ", k)
        # print("Valor de k aproximado: ", round(k))
        return round(k)

    def getClassLength(self, dados):
        tamanho_classe = round((max(dados) - min(dados)) /
                               self.getNumClasses(len(dados)), 1)
        return tamanho_classe

    def removeOutlierExtremo(self, dados):
        print("Buscando outliers extremos...")
        Q1 = st.quantiles(dados)[0]
        Q3 = st.quantiles(dados)[2]
        A = Q3 - Q1
        i = 0
        dadosRemovidos = []
        while i < len(dados):
            valor = dados[i]
            if valor < Q1 - 3 * A or valor > Q3 + 3 * A:
                # print(valor, " - Outlier Extremo")
                dadosRemovidos.append(valor)
                dados.remove(valor)
            i = i + 1
        print("Dados removidos: ", dadosRemovidos)
        return dados

    def printInfoDados(self, dados):
        print("DADOS INFORMADOS")

        ordered = sorted(dados)
        # print("Dados ordenados:", ordered)
        print("Numero de classes:", self.getNumClasses(len(dados)))
        print("Tamanho de cada classe:", (max(dados) -
              min(dados)) / self.getNumClasses(len(dados)))
        print("Quantidade de dados:", len(dados))
        print("Media:", st.mean(dados))
        print("Moda:", st.mode(dados))
        print("Mediana:", st.median(dados))
        print("Maximo:", max(dados))
        print("Minimo:", min(dados))
        print("Quartis:", st.quantiles(dados))
        print("Variancia:", st.variance(dados))
        print("Amplitude Interquartil:", max(dados) - min(dados))
        print("Desvio Padrao:", st.stdev(dados))
        print("Coeficiente de Variacao:",
              (st.stdev(dados) / st.variance(dados)) * 100)
        print("Coeficiente de Assimetria:", (st.quantiles(
            dados)[2]) / (st.median(dados) ** (3 / 2)))

        plt.hist(dados, bins=self.getNumClasses(len(dados)))
        plt.title("Histograma")
        plt.show()
        plt.boxplot(dados)
        plt.title("Boxplot")
        plt.show()

    
    def getStFunction(self, x, mu, sigma):
        return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))

    def plotFunction(self, data):
        x = np.linspace(self.getMin(data), self.getMax(data))
        mu = self.getMean(data)
        sigma = self.getStDev(data)
        y = self.getStFunction(x, mu, sigma)
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Normal Function')
        plt.grid(True)
        plt.show()

    def get_unique_values(self, data):
        unique_values = {}
        for value in data:
            unique_values[value] = True
        return list(unique_values.keys())
