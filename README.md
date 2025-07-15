This project, titled **"Data-driven Pathways for Change,"** focuses on developing a **binary classification model to predict the survival of colorectal cancer (CRC) patients**. This initiative directly addresses CRC as a significant global health burden, ranking as the third most diagnosed cancer and the second leading cause of cancer-related deaths worldwide.

The **primary objective** of this endeavour was to estimate whether a patient diagnosed with CRC will survive, utilizing **advanced data mining techniques**. This involved identifying key contributors to survival, uncovering underlying patterns, and deriving insightful recommendations for effective interventions.

**Methodology:**

1.  **Data Exploration and Preprocessing:** The project began with **extensive exploratory data analysis (EDA) and preprocessing** to uncover patterns and address data quality issues.
    *   The dataset consisted of patient records detailing demographics, medical history, lifestyle factors, and healthcare metrics, with "survival prediction" as the target variable.
    *   Initial analysis identified twenty-four categorical and five numerical variables.
    *   **Key preprocessing steps** included:
        *   **Handling missing values and outliers**: Categorical columns with minor missing values (e.g., 'Healthcare Access', 'Gender') were imputed using the mode, and rows with nulls and duplicate records were removed. Outliers in numerical features (e.g., 'Healthcare Costs', 'Tumor Size') were addressed using the **Interquartile Range (IQR) method with Winsorization**, and negative values were imputed with the median.
        *   **Correcting formatting inconsistencies**: For instance, inconsistencies in capitalization for variables like 'Urban or Rural' were standardized.
        *   **Feature Engineering**: New features like 'patient’s age' (derived from 'Date of Birth'), 'Advanced_age' (patients 65+), 'Cardiometabolic Risk' (combining diabetes and heart disease), and 'Cancer_Severity' (integrating Cancer Stage and Tumor Size) were created to enhance predictive capacity.
        *   **Feature Removal**: Redundant and non-informative features, such as 'Transfusion History' (constant values) and 'Smoking History' (due to redundancy with 'Non Smoker'), were removed.
        *   **Scaling and Encoding**: All numerical variables were scaled using **Robust Scaler**, chosen for its robustness to outliers and skewness, while Min-Max scaling resulted in less favourable model performance. Ordinal variables (e.g., 'Cancer Stage') were encoded according to their natural order, and nominal categorical variables (e.g., 'Country') were one-hot encoded.

2.  **Feature Selection:** To reduce noise, minimize overfitting, and improve model interpretability, two distinct approaches were used:
    *   **Sequential Feature Selection (SFS)**: Both Forward and Backward Selection variants were tested using a logistic regression estimator to retain the top 15 features based on the f1_macro score.
    *   **Recursive Feature Elimination with Cross-Validation (RFECV)**: Applied using 5-fold cross-validation and a logistic regression classifier, this method automatically determined the number of features to retain.
    *   The **Sequential Backward Selection (SBS) method** was ultimately chosen as it demonstrated **superior model stability** with low standard deviations and minimal overfit gaps across models, indicating strong generalization capabilities.

3.  **Model Benchmarking and Comparison:**
    *   Multiple machine learning algorithms were trained and evaluated using stratified 5-fold cross-validation.
    *   An `evaluate_models_with_cv()` function performed 10-fold Cross-Validation for Logistic Regression, Random Forest, and Decision Tree models.
    *   **F1-Macro Score** was chosen as the main evaluation metric, giving equal importance to both precision and recall across classes, which helped address the initial tendency of models to only predict the positive class.
    *   Logistic Regression and Random Forest were selected as primary candidates due to their good performance and stability. Ensemble methods like AdaBoost, Voting Classifier, and Stacking Classifier were also explored to improve predictive performance and robustness.

4.  **Hyperparameter Tuning and Final Model Selection:**
    *   **Grid Search with 5-fold cross-validation** was performed to find the best hyperparameter combination for candidates, balancing class weights to address slight class imbalance (approximately 60% positive vs 40% negative) and minimize false positives, which are considered more costly in oncology prediction.
    *   The **Voting Classifier was ultimately selected as the final model**, combining Logistic Regression (weight 3) and AdaBoost (weight 2).
    *   It provided the **best balance between reducing false positives and maintaining stable predictions**, with a precision of 0.60, recall of 0.57, and minimal overfitting (validation gap of 0.01). While other models had slightly better metrics in some areas, they showed greater overfitting, making the Voting Classifier more reliable on unseen data.

**Key Findings and Insights:**

*   The project highlights the **significant value of data mining techniques, particularly clustering**, in identifying and understanding complex patterns.
*   Beyond core clinical predictors (e.g., cancer stage, age, treatment type, early detection, healthcare access), **systemic factors emerged as strong predictors**:
    *   **Country of origin**: Countries with well-established healthcare systems like South Korea and the United Kingdom were consistently associated with higher survival rates, while those with limited resources, such as Nigeria and Pakistan, showed poorer outcomes. Country-related features likely served as proxies for healthcare systems and structural differences.
    *   **Urban versus rural residence**: CRC mortality is consistently higher in rural areas due to factors like lower screening rates, delayed diagnosis, fewer healthcare resources, socioeconomic challenges, and transportation barriers.
    *   **Health insurance coverage**: Disparities in insurance coverage significantly influence CRC outcomes, particularly in countries like the US, where uninsured individuals often experience late screening and inadequate treatment.

**Limitations:**

*   The dataset presented **inherent imbalances and possible inconsistencies**.
*   Some variables, especially socioeconomic indicators, may not have been captured with the same level of detail across all countries or regions, potentially introducing bias.
*   The **generalizability of the model to external populations remains uncertain**.

**Conclusion and Future Work:**

This project developed a **functional survival prediction model for colorectal cancer patients**, uncovering meaningful patterns with clinical and public health implications. The model offers a comprehensive view of CRC survival, highlighting both medical and structural factors that can be addressed to improve patient outcomes worldwide.

Future work may include incorporating **more granular data sources** (e.g., genetic profiles), exploring **alternative ensemble approaches**, and **validating the model on external cohorts or in clinical practice** for a more robust assessment of its real-world applicability. The model could also serve as a valuable tool for simulating the impact of interventions aimed at improving healthcare access and screening programs, particularly in resource-limited settings.
