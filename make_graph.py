import matplotlib.pyplot as plt
import os

from datetime import datetime
from bd_request import select_week_graph, select_mont_graph, select_day_graph


def make_graph_week(metal):
    info = select_week_graph(metal)
    x = [datetime.strptime(i[1], "%Y-%m-%d %H:%M").strftime("%d.%m") for i in info]
    y = [i[0] for i in info]

    name_metal = {
        'gold': 'золото',
        'silver': 'серебро'
    }

    plt.figure(figsize=(10, 6))
    plt.xlabel("Дата", fontsize=10)
    plt.ylabel("Цена", fontsize=10)
    plt.title(f"График за неделю: {name_metal[metal]}", fontsize=14, fontweight='bold')
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.plot(x, y, marker='.')

    for i, price in enumerate(y):
        plt.text(i, price, price, ha='center', va='bottom')

    file_path = os.path.join('graphs', "graph.png")
    plt.savefig(file_path, dpi=300)
    plt.close()

    return file_path


def make_graph_month(metal):
    info = select_mont_graph(metal)
    x = [datetime.strptime(i[1], "%Y-%m-%d %H:%M").strftime("%d.%m") for i in info]
    y = [i[0] for i in info]

    name_metal = {
        'gold': 'золото',
        'silver': 'серебро'
    }

    plt.figure(figsize=(10, 6))
    plt.xlabel("Дата", fontsize=10)
    plt.ylabel("Цена", fontsize=10)
    plt.title(f"График за месяц: {name_metal[metal]}", fontsize=14, fontweight='bold')
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.plot(x, y, marker='.')

    for i, price in enumerate(y):
        plt.text(i, price, price, ha='center', va='bottom')

    file_path = os.path.join('graphs', "graph.png")
    plt.savefig(file_path, dpi=300)
    plt.close()

    return file_path


def make_graph_day(metal):
    info = select_day_graph(metal)
    x = [datetime.strptime(i[1], "%Y-%m-%d %H:%M").strftime("%H:%M") for i in info]
    y = [i[0] for i in info]

    name_metal = {
        'gold': 'золото',
        'silver': 'серебро'
    }

    plt.figure(figsize=(10, 6))
    plt.xlabel("Время", fontsize=10)
    plt.ylabel("Цена", fontsize=10)
    plt.title(f"График за день: {name_metal[metal]}", fontsize=14, fontweight='bold')
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.plot(x, y, marker='.')

    for i, price in enumerate(y):
        plt.text(i, price, price, ha='center', va='bottom')

    file_path = os.path.join('graphs', "graph.png")
    plt.savefig(file_path, dpi=300)
    plt.close()

    return file_path


if __name__ == '__main__':
    make_graph_week('silver')
