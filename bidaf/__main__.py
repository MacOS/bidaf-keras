from .models import BidirectionalAttentionFlow
from .scripts.data_generator import load_data_generators


def main():
    bidaf = BidirectionalAttentionFlow(emdim=600, num_highway_layers=2, num_decoders=1)
    train_generator, validation_generator = load_data_generators(batch_size=40)
    model = bidaf.train_model(train_generator, epochs=20, validation_data=validation_generator,
                              save_history=True, save_model_per_epoch=True)


if __name__ == '__main__':
    main()
