import matplotlib.pyplot as plt


def generate_bar_char(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title('Population by country')
    plt.show()
    
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.show()