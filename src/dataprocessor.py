import statistics as st

class DataProcessor:
    @staticmethod
    def detect_outliers(data):
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

    @staticmethod
    def process_data(data):
        DataProcessor.detect_outliers(data)

        print("Mean:", st.mean(data))
        print("Median:", st.median(data))
        print("Standard Deviation:", st.stdev(data))
        print("Variance:", st.variance(data))
        print("Mode:", st.mode(data))
        print("Quantiles:", st.quantiles(data))
