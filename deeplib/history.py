import matplotlib.pyplot as plt
from IPython.display import clear_output


class History:

    def __init__(self):
        self.history = {
            'train_acc': [],
            'val_acc': [],
            'train_loss': [],
            'val_loss': [],
            'lr': []
        }

    def save(self, train_acc, val_acc, train_loss, val_loss, lr):
        self.history['train_acc'].append(train_acc)
        self.history['val_acc'].append(val_acc)
        self.history['train_loss'].append(train_loss)
        self.history['val_loss'].append(val_loss)
        self.history['lr'].append(lr)

    def display_accuracy(self):
        epoch = len(self.history['train_acc'])
        epochs = list(range(1, epoch + 1))
        plt.title('Training accuracy')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.plot(epochs, self.history['train_acc'], label='Train')
        plt.plot(epochs, self.history['val_acc'], label='Validation')
        plt.legend()
        plt.show()

    def display_loss(self):
        epoch = len(self.history['train_acc'])
        epochs = list(range(1, epoch + 1))
        plt.title('Training loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.plot(epochs, self.history['train_loss'], label='Train')
        plt.plot(epochs, self.history['val_loss'], label='Validation')
        plt.legend()
        plt.show()

    def display_lr(self):
        epoch = len(self.history['train_acc'])
        epochs = list(range(1, epoch + 1))
        plt.title('Learning rate')
        plt.xlabel('Epochs')
        plt.ylabel('Lr')
        plt.plot(epochs, self.history['lr'], label='Lr')
        plt.show()

    def display(self, display_lr=True):
        epoch = len(self.history['train_acc'])
        epochs = list(range(1, epoch + 1))

        num_plots = 3 if display_lr else 2
        fig, axes = plt.subplots(num_plots, 1, sharex=True)
        plt.tight_layout()

        axes[0].set_ylabel('Accuracy')
        axes[0].plot(epochs, self.history['train_acc'], label='Train')
        axes[0].plot(epochs, self.history['val_acc'], label='Validation')
        axes[0].legend()

        axes[1].set_ylabel('Loss')
        axes[1].plot(epochs, self.history['train_loss'], label='Train')
        axes[1].plot(epochs, self.history['val_loss'], label='Validation')

        if display_lr:
            axes[2].set_xlabel('Epochs')
            axes[2].set_ylabel('Lr')
            axes[2].plot(epochs, self.history['lr'], label='Lr')

        plt.show()


def plot_poutyne_history(history):
    epochs = list(range(1, len(history) + 1))

    train_acc = [entry['acc'] for entry in history]
    val_acc = [entry['val_acc'] for entry in history]
    train_loss = [entry['loss'] for entry in history]
    val_loss = [entry['val_loss'] for entry in history]

    fig, axes = plt.subplots(2, 1, sharex=True)
    plt.tight_layout()

    axes[0].set_ylabel('Accuracy')
    axes[0].plot(epochs, train_acc, label='Train')
    axes[0].plot(epochs, val_acc, label='Validation')
    axes[0].legend()

    axes[1].set_xlabel('Epochs')
    axes[1].set_ylabel('Loss')
    axes[1].plot(epochs, train_loss, label='Train')
    axes[1].plot(epochs, val_loss, label='Validation')

    plt.show()
