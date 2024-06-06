# Creating a tabular form for the literature review
import pandas as pd

# Data for the literature review
literature_review_data = {
    "Study": [
        "Djeundje et al. (2021)",
        "Óskarsdóttir et al. (2019)",
        "Simumba et al. (2021)",
        "Yap et al. (2011)",
        "Njuguna and Sowon (2021)",
        "Zhang et al. (2020)",
        "Yang et al. (2021)",
        "Niu et al. (2020)",
        "He et al. (2018)",
        "Bao et al. (2019)"
    ],
    "Title": [
        "Enhancing credit scoring with alternative data",
        "The value of big data for credit scoring: Enhanced predictive performance using call-detail records and social network data",
        "Spatiotemporal Integration of Mobile, Satellite, and Public Data Improves Credit Scoring for Financially Excluded Persons",
        "Using data mining to improve assessment of credit risk",
        "Poster: A Scoping Review of Alternative Credit Scoring Methods",
        "Research on personal credit scoring model based on weighted average method",
        "A novel multi-stage ensemble model with enhanced performance using alternative data",
        "A Deep Learning Based Online Credit Scoring Model with Alternative Data",
        "A novel ensemble method for credit scoring: Addressing class imbalance with alternative data",
        "Integration of unsupervised and supervised machine learning techniques for credit scoring models"
    ],
    "Authors": [
        "V. Djeundje, J. Crook, R. Calabrese, Mona Hamid",
        "M. Óskarsdóttir, Cristián Bravo, Carlos Sarraute, M. Vanhoof",
        "Naomi Simumba, Suguru Okami, A. Kodaka, N. Kohno",
        "B. W. Yap, S. Ong, Nor Huselina Mohamed Husain",
        "R. Njuguna, Karen Sowon",
        "Haichao Zhang, Ruishuang Zeng, Lin-long Chen, Shuai Huang",
        "Wenyu Zhang, Dongqi Yang, Shuai Zhang, J. Abla",
        "Zaimei Zhang, Kun Niu, Yan Liu",
        "Hongliang He, Wenyu Zhang, Shuai Zhang",
        "Wang Bao, Lianju Ning, Kong Yue"
    ],
    "Year": [
        2021,
        2019,
        2021,
        2011,
        2021,
        2020,
        2021,
        2020,
        2018,
        2019
    ],
    "Citations": [
        51,
        119,
        5,
        176,
        5,
        5,
        38,
        18,
        173,
        91
    ],
    "Takeaway": [
        "Using email usage and psychometric variables, improves credit scoring for individuals with sparse credit histories.",
        "Adding call-detail records and social network data enhances traditional models.",
        "Integrating mobile-phone, satellite, and public data better assesses financially excluded persons.",
        "Data mining techniques can improve credit scoring accuracy.",
        "Alternative credit scoring using non-financial data is promising but faces challenges.",
        "Weighted average model using various alternative data sources enhances credit scoring accuracy.",
        "Multi-stage ensemble model leveraging alternative data improves prediction performance.",
        "Deep learning-based online credit scoring model incorporating alternative data.",
        "Novel ensemble method integrates various data types for more accurate credit scoring.",
        "Integration of unsupervised and supervised machine learning techniques enhances credit scoring models."
    ]
}

# Creating a DataFrame
literature_review_df = pd.DataFrame(literature_review_data)

# Save the DataFrame to an Excel file
output_file_path = 'Literature_Review_Alternative_Data_Credit_Scoring.xlsx'
literature_review_df.to_excel(output_file_path, index=False)

print(f"File saved as {output_file_path}")
