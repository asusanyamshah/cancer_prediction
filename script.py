# Importing joblib
import joblib

# Loading the model
classifier = joblib.load('classifier.pk1')

# Making a user friendly welcome page
print(f"Hello, Welcome to the Cancer Classifier\nPlease answer the following questions: ")

# Getting the necessary input
radius_mean = float(input(f"What is the mean radius: "))
texture_mean = float(input(f"What is the mean texture: "))
perimeter_mean = float(input(f"What is the mean perimeter: "))
area_mean = float(input(f"What is the mean area: "))
smoothness_mean = float(input(f"What is the mean smoothness: "))
compactness_mean = float(input(f"What is the mean compactness: "))
concavity_mean = float(input(f"What is the mean concavity: "))
concavepoints_mean = float(input(f"What is the mean concave points: "))
symmetry_mean = float(input(f"What is the mean symmetry: "))
fractal_dimension_mean = float(input(f"What is the mean fractal dimension: "))
radius_se = float(input("What is the radius se: "))
texture_se = float(input(f"What is the texture se: "))
perimeter_se = float(input(f"What is the perimeter se: "))
area_se = float(input(f"What is the area se: "))
smoothness_se = float(input(f"What is the smoothness se: "))
compactness_se = float(input(f"What is the compactness se: "))
concavity_se = float(input(f"What is the concavity se: "))
concavepoints_se = float(input(f"What is the concave points se: "))
symmetry_se = float(input(f"What is the symmetry se: "))
fractal_dimension_se = float(input(f"What is the fractal dimension se: "))
radius_worst = float(input(f"What is the radius worst: "))
texture_worst = float(input(f"What is the texture worst: "))
perimeter_worst = float(input(f"What is the perimeter worst: "))
area_worst = float(input(f"What is the area worst: "))
smoothness_worst = float(input(f"What is the smoothness worst: "))
compactness_worst = float(input(f"What is the compactness worst: "))
concavity_worst = float(input(f"What is the concavity worst: "))
concavepoints_worst = float(input(f"What is the concave points worst: "))
symmetry_worst = float(input(f"What is the symmetry worst: "))
fractal_dimension_worst = float(input(f"What is the fractal dimension worst: "))

# Getting the prediction from the model
prediction = classifier.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concavepoints_mean, symmetry_mean,
                   fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concavepoints_se, symmetry_se,
                   fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concavepoints_worst,
                   symmetry_worst, fractal_dimension_worst]])

# Printing the prediction in a user friendly way
print(f"Thank you for answering\n\n")
if prediction[0] == 1:
    print(f"The cancer is malignant")

else:
    print(f"The cancer is benign")

