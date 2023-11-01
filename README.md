# keras-news-classifier
**Do all social media news sources merit trust?**   
The contemporary era grapples with an abundance of misinformation, making it essential to discern fake news from authentic news. Fortunately, the path to fake news detection is illuminated through the application of supervised machine learning techniques.

Fake news comprises fabricated information intentionally crafted to deceive individuals. Typically disseminated via online platforms, particularly social media, its motives often gravitate toward political manipulation, either to confer advantages or disadvantages upon a specific political faction. These deceptive news pieces tend to encompass spurious and overstated assertions, further perpetuating within filter bubbles established by certain algorithms.

This endeavor entails the utilization of two distinct datasets:

1. A comprehensive news dataset sourced from Kaggle.
2. A secondary dataset meticulously curated through the News API. This API will be harnessed to collect data, subsequently appending it to the existing dataset.

The ultimate objective is to employ a passive-aggressive classifier, a machine learning algorithm designed for classification tasks. This classifier dynamically adapts the model in response to erroneous predictions. When predictions are accurate, the model remains unaltered. It is through this approach that we distinguish genuine news from their counterfeit counterparts.
