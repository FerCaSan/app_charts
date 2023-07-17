import matplotlib.pyplot as plt


def generate_bar_char(name,labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title('Population by country')
    plt.savefig(f'./imgs/{name}.png')
    plt.close()
    
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig(f'./imgs/chart_pie.png')
    plt.close()