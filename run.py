import argparse
from your_module import MachineLearningAI, DeepLearningAI, save_best_models_and_data, train_and_save_deep_learning_model

def main():
    parser = argparse.ArgumentParser(description='Run TryAgain Project')
    parser.add_argument('--mode', type=str, choices=['ml', 'dl'], required=True, help='Mode to run: ml or dl')
    args = parser.parse_args()

    if args.mode == 'ml':
        save_best_models_and_data(classifier_params)
    elif args.mode == 'dl':
        train_and_save_deep_learning_model()
    else:
        print("Invalid mode selected. Please choose 'ml' or 'dl'.")

if __name__ == '__main__':
    main()
