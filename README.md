# Dravidian_SMS_Spam_Classification
This GitHub repository contains a Python script for a Spam SMS model designed primarily for Dravidian languages such as Tamil, Kannada, Malayalam, and Telugu. The code implements a Random Forest Classifier trained to detect spam messages based on a set of handcrafted features.

Initially, the model was designed with 17 handcrafted features, derived from two datasets. One of these datasets is publicly available on IEEE Dataport through the link "http://ieee-dataport.org/documents/spam-sms-dravidian-languages." This dataset was collected using Google Forms and meticulously labeled by language experts, under the guidance of the developer's mentor.

Out of the 17 initially created features, six were selected for the final model using a graph-based feature selection algorithm. Unfortunately, the details of this algorithm are not revealed in this repository as the associated research paper is not yet published. However, the algorithm's specifics will be made available in the same repository once the paper is published.

This spam model script utilizes several techniques to process and analyze SMS messages. It includes the identification of HTTP links and phone numbers, checks for the presence of predefined spam keywords and greeting words, measures the length of the message, and counts the distinct words within the message. These features are used to make predictions about whether a given SMS is spam or not.

The files "spam_keywords.txt" and "greeting_words.txt" are included in this repository and can be updated as needed.

Accuracy Details:

Mean Accuracy: 0.9526526526526525
Standard Deviation Accuracy: 0.0037976972042270104
Mean Balanced Accuracy: 0.9007718503555959
Standard Deviation Balanced Accuracy: 0.009179637475376116
Mean ROC AUC: 0.9007718503555959
Standard Deviation ROC AUC: 0.009179637475376144
Mean F1 Score: 0.8602251352010405
Standard Deviation F1 Score: 0.013298673806442559
Mean Recall Score: 0.8202555176383242
Standard Deviation Recall Score: 0.01874728215319389
Mean Precision Score: 0.9047553109035815
Standard Deviation Precision Score: 0.019010236476577163
The earlier version of this model was presented as a paper at ICDSNE 2023, held at NIT Agartala.

Please note that the code provided here is a standalone script for spam detection and may be further integrated into larger systems or applications for real-world usage.

For more details and updates on this project, please stay tuned to this repository
