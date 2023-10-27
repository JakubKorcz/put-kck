import os
import matplotlib.pyplot as plt
import numpy as np

path = "csvFiles"

def main():
    lines = readFiles()
    values, generations, efforts = calculateValues(lines)
    labels = ["1-Coev", "1-Coev-RS", "1-Evol-RS", "2-Coev", "2-Coev-RS"]
    drawPlots(generations, values, efforts, labels, lines)


def readFiles():
    lines = []
    for file in os.listdir(path):
        path_to_file = os.path.join(path, file)
        row = []
        with open(path_to_file) as f:
            for line in f:
                line = line.rstrip('\n')
                row.append(line.split(','))
        lines.append(row)
    return lines


def calculateValues(lines):
    values = []
    generations = []
    efforts = []
    for i in range(len(os.listdir(path))):
        val = []
        gen = []
        eff = []
        for j in range(1, 201):
            suma = 0
            for k in range(0, 34):
                if k == 0:
                    gen.append(lines[i][j][k])
                elif k == 1:
                    eff.append(lines[i][j][k])
                else:
                    suma += float(lines[i][j][k])
            suma /= 32
            suma *= 100
            suma = round(suma, 4)
            val.append(suma)
        values.append(val)
        generations.append(gen)
        efforts.append(eff)
    return values, generations, efforts


def drawPlots(generations, values, efforts, labels, lines):
    fig, (plt1, plt2) = plt.subplots(1, 2, figsize=(10, 10))

    markers = ['o', '^', '*', 'v', 's']
    sequence = [2, 1, 4, 0, 3]

    # ////////////////////plt 1///////////////////////////
    for i in sequence:
        plt1.plot(efforts[0], values[i], label=labels[i], marker=markers[i], markevery=25, markeredgecolor='black')

    # label x down
    plt1.set_xlabel('Rozegranych gier (x1000)', fontsize="16")
    plt1.set_xlim(0, 200)
    plt1.set_xticks(np.arange(0, 240, 40))
    plt1.set_xticklabels(['0', '100', '200', '300', '400', '500'])
    plt1.grid(True, linestyle=':')

    # label y
    plt1.set_ylim(60, 100)
    # yticks_values = np.arange(60, 105, 5)
    # plt1.set_yticks(yticks_values)

    plt1.set_ylabel('Odsetek wygranych gier [%]', fontsize="16")

    # label x up
    ax2 = plt1.twiny()
    ax2.set_xlabel('Pokolenie', fontsize="16")
    ax2.set_xticks(np.arange(0, 240, 40))

    # legend
    plt1.legend(loc='lower right', fontsize="16")

    # //////////////////////// plt 2 /////////////////////////
    val = []
    for i in sequence:
        data = []
        for j in range(2, 34):
            data.append(float(lines[i][199][j]))
        val.append(data)

    plt2.boxplot(val, notch="True", boxprops=dict(linestyle='-', linewidth=1, color='blue'), showmeans=True,
                 meanprops=dict(marker='o', markerfacecolor='red', markersize=6))
    plt2.set_xticklabels(labels)

    plt2.set_ylim(0.6, 1)

    # plt2.set_yticks[50, 60, 70, 80, 90, 100]
    # plt2.set_yticklabels(['50', '60', '70', '80', '90', '100'])

    plt2.grid(True, linestyle=':')

    # /////////////////////// save plots///////////////////////////////
    plt.savefig('my-plot1.pdf')
    plt.close()


if __name__ == '__main__':
    main()
