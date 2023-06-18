import statistics as st
import math as m
import matplotlib.pyplot as plt


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
                print(value, " - Outlier Moderado")
                count_outlier_moderado += 1
                count_total_outliers += 1
            if value < Q1 - 3 * A or value > Q3 + 3 * A:
                print(value, " - Outlier Extremo")
                count_outlier_extremo += 1
                count_total_outliers += 1
            i += 1
        print("Total de Outliers Moderados: ", count_outlier_moderado)
        print("Total de Outliers Extremos: ", count_outlier_extremo)
        print("Total de Outliers: ", count_total_outliers)

    def process_data(self, data):
        self.detect_outliers(data)
        self.removeOutlierExtremo(data)
        print("Mean:", st.mean(data))
        print("Median:", st.median(data))
        print("Standard Deviation:", st.stdev(data))
        print("Variance:", st.variance(data))
        print("Mode:", st.mode(data))
        print("Quantiles:", st.quantiles(data))

    def getNumClasses(self, n):
        log = m.log10(n)
        k = 1 + 3.3 * log
        print("Valor de k: ", k)
        print("Valor de k aproximado: ", round(k))
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
                print(valor, " - Outlier Extremo")
                dadosRemovidos.append(valor)
                dados.remove(valor)
            i = i + 1
        print("Dados após remoção de outliers extremos: ", dados)
        print("Dados removidos: ", dadosRemovidos)
        return dados

    def printInfoDados(self, dados):
        self.removeOutlierExtremo(dados)

        print("DADOS INFORMADOS")

        ordered = sorted(dados)
        print("Dados ordenados:", ordered)
        print("Numero de classes:", self.getNumClasses(len(dados)))
        print("Tamanho de cada classe:", (max(dados) -
              min(dados)) / self.getNumClasses(len(dados)))
        print("Tamanho", len(dados))
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
        plt.show()
        plt.boxplot(dados)
        plt.show()
