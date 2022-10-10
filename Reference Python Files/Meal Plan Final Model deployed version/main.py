# Imported Libraries

from sklearn.preprocessing import OneHotEncoder
import warnings

warnings.filterwarnings('ignore')
oneH = OneHotEncoder()
import heart_patient_meal as hm
import diabetes_meal as dm

''' =========================================================================================='''
''' ================================ diabetes meal plan ========================='''
''' =========================================================================================='''

Gender = 'Male'
age = 50
Polyuria = 'No'
Polydipsia = 'Yes'
sudden_weight_loss = 'No'
weakness = 'Yes'
Polyphagia = 'No'
Genital_thrush = 'No'
visual_blurring = 'No'
Itching = 'Yes'
Irritability = 'No'
delayed_healing = 'Yes'
partial_paresis = 'No'
muscle_stiffness = 'Yes'
Alopecia = 'Yes'
Obesity = 'Yes'
# -------------------------------------
height = 5.7  # feet
weight = 85  # kg
activity_level = 'none'
goals = 'gain'
foodtype = 'Non-Veg'

diabetes_meal_plan = dm.is_diabetes_mealplan_needed(
    [Gender, age, Polyuria, Polydipsia, sudden_weight_loss, weakness, Polyphagia, Genital_thrush, visual_blurring,
     Itching, Irritability, delayed_healing, partial_paresis, muscle_stiffness, Alopecia, Obesity,height,weight,activity_level,goals,foodtype])

print(diabetes_meal_plan)

''' =========================================================================================='''
''' ================================ heart patient meal ======================================'''
''' =========================================================================================='''

gender = 'female'
height = 5.7
weight = 85
ap_hi = 140
ap_lo = 90
age = 50
BMI_Class = 'Obesity'
MAP_Class = 'High'
cholesterol = 'well_above_normal'
gluc = 'normal'
smoke = 'no'
alco = 'no'
active = 'yes'
# ====================

activity_level = 'none'
goals = 'gain'
foodtype = 'Non-Veg'

heart_mealplan_output = hm.is_heartpatient_mealplan_needed(
    [gender, height, weight, ap_hi, ap_lo, age, BMI_Class, MAP_Class, cholesterol, gluc, smoke, alco, active,
     activity_level, goals, foodtype])

print(heart_mealplan_output)
