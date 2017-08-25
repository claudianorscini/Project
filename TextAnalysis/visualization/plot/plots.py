import matplotlib.pyplot as plt

def plot_30_words(tot_tf):

    top20tot_tf=tot_tf[0:30]

    fig, ax = plt.subplots()
    x = []
    y = []
    for topword in top20tot_tf:
        x.append(topword['word'])
        y.append(topword ['tottf'])


    plt.bar(range(len(x)), y, align='center')
    plt.xticks(range(len(x)), x)
    ax.set_xticklabels(x,rotation=30)
    plt.draw()
    plt.show()
def plot_20_words_per_tf(tot_tf,tf):

    top20tot_tf=tot_tf[0:20]

    fig=plt.figure(1)
    i=0
    for topword in top20tot_tf:
        i=i+1
        fig.add_subplot(2,10,i)
        x=[]
        y=[]
        for word in tf:
            if word['word'] == topword ['word']:       #print('docID','tf', key)print('docID','tf', key)
                x.append(word['document_id'])
                y.append(word['frequencynorm'])

        plt.plot(x,y,label = topword['word'])
        #plt.pcolormesh(x,y,label = topword['word'])

        plt.legend()
    plt.show()
