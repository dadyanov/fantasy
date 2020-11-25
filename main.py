import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import time

# https://github.com/vaastav/Fantasy-Premier-League
# Поместить папку data в одно окружеине с этим кодом и сказать спасибо разработчику

data_path = 'data'


# Объект дата для получения и работы с данными данных
class Data:
    def __init__(self, name=time.time(), path=data_path):
        self.name = name
        self.path = path
        pass

    # Возвращает список всех директорий данных
    def all_derectories_list(self):
        seasons = list()
        for directory in os.listdir(self.path):
            if directory != '.DS_Store':
                seasons.append(self.path + '/' + directory + '/' + 'gws')
        game_weeks = list()
        for season in seasons:
            for game in os.listdir(season):
                game_weeks.append(season + '/' + game)
        return game_weeks

    # Возвращает список  директорий данных одного сезона
    def season_directories_list(self, season):
        result = list()
        for directory in self.all_derectories_list():
            x = int(directory[5:9])
            if x == season:
                result.append(directory)
        return result

    # Возвращает Data Frame всех данных
    def to_df(self, period=True):
        if period is True:
            directories = self.all_derectories_list()

            df = pd.read_csv(directories[0], encoding='iso-8859-1')
            year = directories[0][5:9]
            if directories[0] == 7:
                gw = directories[0][19:20]
            else:
                gw = directories[0][19:21]
            df['year'] = year
            df['gw'] = gw

            directories.pop(0)
            for directory in directories:
                new_df = pd.read_csv(directory, encoding='iso-8859-1')
                year = directory[5:9]
                if directory == 7:
                    gw = directory[19:20]
                else:
                    gw = directory[19:21]
                new_df['year'] = year
                new_df['gw'] = gw
                df = df.append(new_df)
        elif period is not True:
            directories = self.season_directories_list(period)

            df = pd.read_csv(directories[0], encoding='iso-8859-1')
            year = directories[0][5:9]
            if directories[0] == 7:
                gw = directories[0][19:20]
            else:
                gw = directories[0][19:21]
            df['year'] = year
            df['gw'] = gw

            directories.pop(0)
            for directory in directories:
                new_df = pd.read_csv(directory, encoding='iso-8859-1')
                year = directory[5:9]
                if directory == 7:
                    gw = directory[19:20]
                else:
                    gw = directory[19:21]
                new_df['year'] = year
                new_df['gw'] = gw
                df = df.append(new_df)
        return df

    # Сохраняет DataFrame в csv файл
    @staticmethod
    def progress_save(df, name=time.time()):
        name = str(name) + '.csv'
        df.to_csv('{0}'.format(name))
        return name

    # Читает df из csv
    @staticmethod
    def progress_read(name):
        df = pd.read_csv(name)
        return df


# Объект дата для построения графиков и визуализации данных
# По сути просто набор методов, объединенных в класс для удобства
class Graph:
    def __init__(self, data):
        self.data = data
        pass

    # График распределения данных по категориям и субкатегориям
    def distribution_category(self, category, values, subcategory=None):
        sns.catplot(x="{0}".format(values), y="{0}".format(category),
                    hue="{0}".format(subcategory),
                    data=self.data,
                    orient="h", palette="mako", dodge=True)

        plt.show()
        return plt

