import sys
import matplotlib.pyplot as plt

def main():
    val_losses = []; val_accuracies=[]
    train_losses = []; train_accuracies=[]
    fin = sys.argv[1]
    epochs = 15
    if len(sys.argv) > 2:
        epochs = int(sys.argv[2])
    train_loss = -1
    train_acc = -1
    with open(fin) as f:
        i=0
        for line in f:
            splitLine = line.split()
            if not len(splitLine) or len(splitLine[0]) < 5:
                continue
            if splitLine[0][:5] == 'Train':
                train_loss = float(splitLine[5][:-1])
                train_acc = float(splitLine[7])
            elif splitLine[0][:5] == 'Valid':
                i+=1
                val_loss = float(splitLine[5][:-1])
                val_acc = float(splitLine[7])
                train_losses.append(train_loss)
                train_accuracies.append(train_acc)
                val_losses.append(val_loss)
                val_accuracies.append(val_acc)
                if i == epochs:
                    break
    plt.figure(figsize = (10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(val_losses, 'bo-', label = 'val-loss')
    plt.plot(train_losses, 'ro-', label = 'train-loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['validation', 'training'], loc='upper right')

    plt.subplot(1, 2, 2)
    plt.plot(val_accuracies, 'bo-', label = 'val-acc')
    plt.plot(train_accuracies, 'ro-', label = 'train-acc')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['validation', 'training'], loc='lower right')
    plt.show()

main()
