from transformers import pipeline 

# Load sentiment-analysis pipeline
classifier = pipeline("sentiment-analysis")


while True: 
    # Get user input
    text = input("Enter a sentence for sentiment analysis: ")

    # Run prediction
    result = classifier(text)

    # Display the result
    label = result[0]['label']
    score = result[0]['score']

    print(f"Sentiment: {label} (Confidence: {score:.2f})")