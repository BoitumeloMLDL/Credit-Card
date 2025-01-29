# Resampling Methods
	•	Oversampling: Duplicate or synthetically generate samples of the minority class (e.g., SMOTE).
I decided to use SMOTE because the dataset was highly disproportionate and the minority class was severely underrepresented.  

Precision, Recall, and F1 Score are key metrics used to evaluate the performance of classification models, particularly in cases where the dataset is imbalanced. Here’s what they mean and how to interpret them:

# 1. Precision

Definition: Precision measures the proportion of correctly predicted positive observations to the total predicted positive observations. It tells you how “precise” your model is when predicting the positive class.
 • High Precision: The model has few false positives. When the model predicts positive, it is likely to be correct.
 • Use Case: Important when false positives are costly (e.g., fraud detection, where marking legitimate transactions as fraud is undesirable).

# 2. Recall (Sensitivity/True Positive Rate)

Definition: Recall measures the proportion of actual positive observations that were correctly identified. It shows how well the model captures the positive class.
 • High Recall: The model has few false negatives. It captures most of the positive instances.
 • Use Case: Critical when missing a positive case is costly (e.g., fraud detection, where missing a fraudulent transaction is serious).

# 3. F1 Score

Definition: The F1 Score is the harmonic mean of Precision and Recall. It provides a single metric that balances both Precision and Recall, especially when the dataset is imbalanced.
 • High F1 Score: Indicates a good balance between Precision and Recall.
 • Use Case: Useful when both false positives and false negatives have consequences, and you want a balanced performance measure.

This is why I incorporated these metrics.

# Machine Learning Algorithm

	•	Some machine learning algorithms, like logistic regression, support vector machines, or k-nearest neighbors, are more sensitive to class imbalances because they aim to minimize overall error or distance. These models might struggle without balanced data. That is reason I used SMOTE.
	•	On the other hand, tree-based methods like Random Forest or Gradient Boosting are somewhat robust to class imbalance but can still benefit from balanced data in extreme cases.

Random Forest

1. Handles Imbalanced Data Well
	•	Fraud detection datasets are often highly imbalanced (fraud cases are rare).
	•	Random Forest uses multiple decision trees, which reduces the bias towards the majority class.

2. Works Well with Non-Linear and Complex Patterns
	•	Fraudulent transactions often follow complex patterns that are non-linear and non-trivial.
	•	Random Forest captures these patterns by combining multiple decision trees, improving accuracy.

3. Resistant to Overfitting
	•	Unlike a single decision tree, which can overfit, Random Forest averages multiple trees, reducing overfitting.
	•	Bagging (Bootstrap Aggregating) ensures that each tree sees different parts of the data, leading to better generalization.

4. Feature Importance Analysis
	•	Random Forest provides feature importance scores, helping identify key factors that contribute to fraud.
	•	This helps fraud analysts understand what influences fraud detection and refine business rules.

5. Handles Missing Values and Noisy Data
	•	Real-world fraud detection datasets often have missing values or incorrect information.
	•	Random Forest can handle missing values internally by using surrogate splits in decision trees.

6. Can Be Used for Both Classification and Anomaly Detection
	•	Supervised Learning: Train with labeled fraud and non-fraud cases.
	•	Unsupervised Learning: Use Random Forest for outlier detection by setting a threshold on low-confidence predictions.

7. Works Well with Large Datasets
	•	Can handle thousands of features and millions of records efficiently.
	•	Supports parallelization (using multiple cores for training).

8. Robust Against Feature Scaling Issues
	•	Unlike logistic regression or SVM, Random Forest does not require feature scaling.
	•	Saves preprocessing time compared to models that require MinMaxScaler or StandardScaler.

9. Easy to Interpret and Explain
	•	Compared to deep learning models, Random Forest is easier to interpret and provides clear decision paths.
	•	Helps businesses and fraud analysts understand why a transaction was flagged as fraud.

Conclusion: Why Use Random Forest for Fraud Detection?

✅ Handles class imbalance effectively
✅ Captures complex fraud patterns
✅ Resistant to overfitting
✅ Provides feature importance analysis
✅ Handles missing/noisy data well
✅ Can be used for both classification and anomaly detection
✅ Scales well with large datasets
✅ Does not require feature scaling
✅ Interpretable and explainable

