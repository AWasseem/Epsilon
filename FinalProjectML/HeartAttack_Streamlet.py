import streamlit as st
import pandas as pd
import joblib
from imblearn.pipeline import  Pipeline
from sklearn.impute import  SimpleImputer, KNNImputer
from sklearn.preprocessing import  RobustScaler, OneHotEncoder, OrdinalEncoder
from category_encoders import  BinaryEncoder
from imblearn.over_sampling import  SMOTE
from sklearn.neighbors import KNeighborsClassifier
from imblearn.pipeline import Pipeline as ImbPipeline

st.set_page_config(layout= 'wide', page_title= 'Heart Attack Prediction Project')
html_title = "<h1 style=color:white;text-align:center;> Heart Attack Prediction Project </h1>"
st.markdown(html_title, unsafe_allow_html=True)

df = pd.read_csv('FinalProjectML/HeartAttack_cleaned_df.csv')
df.dropna(inplace=True)
st.dataframe(df)

Sex = st.sidebar.radio('Sex', df.Sex.unique())
PhysicalHealthDays= st.sidebar.slider('Physical Health Days', int(df.PhysicalHealthDays.min()), int(df.PhysicalHealthDays.max()), int(df.PhysicalHealthDays.mean()))
MentalHealthDays= st.sidebar.slider('Mental Health Days', int(df.MentalHealthDays.min()), int(df.MentalHealthDays.max()), int(df.MentalHealthDays.mean()))
SleepHours= st.sidebar.slider('Sleep Hours', float(df.SleepHours.min()), float(df.SleepHours.max()), float(df.SleepHours.mean()))
HeightInMeters= st.sidebar.slider('Height In Meters', float(df.HeightInMeters.min()), float(df.HeightInMeters.max()), float(df.HeightInMeters.mean()))
BMI= st.sidebar.slider('BMI', float(df.BMI.min()), float(df.BMI.max()), float(df.BMI.mean()))
GeneralHealth = st.sidebar.selectbox('PLease provid General Health ', df.GeneralHealth.unique())
LastCheckupTime = st.sidebar.selectbox('When was your last checkup?', df.LastCheckupTime.unique())
PhysicalActivities = st.sidebar.radio('Do you do physical activities?', df.PhysicalActivities.unique())
RemovedTeeth= st.sidebar.selectbox('Removed Teeth',df.RemovedTeeth.unique())
HadAngina= st.sidebar.radio('Had Angina',df.HadAngina.unique())
HadStroke= st.sidebar.radio('Had Stroke',df.HadStroke.unique())
HadCOPD= st.sidebar.radio('Had COPD',df.HadCOPD.unique())
HadDepressiveDisorder= st.sidebar.radio('Had Depressive Disorder',df.HadDepressiveDisorder.unique())
HadKidneyDisease= st.sidebar.radio('Had Kidney Disease',df.HadKidneyDisease.unique())
HadArthritis= st.sidebar.radio('Had Arthritis',df.HadArthritis.unique())
HadDiabetes= st.sidebar.selectbox('Had Diabetes',df.HadDiabetes.unique())
DeafOrHardOfHearing= st.sidebar.radio('Deaf Or Hard Of Hearing',df.DeafOrHardOfHearing.unique())
BlindOrVisionDifficulty= st.sidebar.radio('Blind Or Vision Difficulty',df.BlindOrVisionDifficulty.unique())
DifficultyConcentrating= st.sidebar.radio('Difficulty Concentrating',df.DifficultyConcentrating.unique())
DifficultyWalking= st.sidebar.radio('Difficulty Walking',df.DifficultyWalking.unique())
DifficultyDressingBathing= st.sidebar.radio('Difficulty Dressing Bathing',df.DifficultyDressingBathing.unique())
DifficultyErrands= st.sidebar.radio('Difficulty Errands',df.DifficultyErrands.unique())
SmokerStatus= st.sidebar.selectbox('Smoker Status',df.SmokerStatus.unique())
ECigaretteUsage= st.sidebar.selectbox('E-Cigarette Usage',df.ECigaretteUsage.unique())
ChestScan= st.sidebar.radio('Chest Scan',df.ChestScan.unique())
AgeCategory= st.sidebar.selectbox('Age Category',df.AgeCategory.unique())
AlcoholDrinkers= st.sidebar.radio('Alcohol Drinkers',df.AlcoholDrinkers.unique())
HIVTesting= st.sidebar.radio('HIV Testing',df.HIVTesting.unique())
FluVaxLast12= st.sidebar.radio('Flu Vax Last 12 Months',df.FluVaxLast12.unique())
PneumoVaxEver= st.sidebar.radio('Pneumo Vax Ever',df.PneumoVaxEver.unique())
TetanusLast10Tdap= st.sidebar.selectbox('Tetanus Last 10 Tdap',df.TetanusLast10Tdap.unique())
HighRiskLastYear= st.sidebar.radio('High Risk Last Year',df.HighRiskLastYear.unique())
CovidPos= st.sidebar.selectbox('Covid Positive',df.CovidPos.unique())

# Import Model
Model = joblib.load('FinalProjectML/LightGPM.pkl')

input_cols = df.columns.drop('HadHeartAttack')
input_data = pd.DataFrame(columns=input_cols,data= [ [Sex,GeneralHealth,PhysicalHealthDays,MentalHealthDays,LastCheckupTime
,PhysicalActivities,SleepHours,RemovedTeeth,HadAngina,HadStroke,HadCOPD,HadDepressiveDisorder,HadKidneyDisease,HadArthritis
,HadDiabetes,DeafOrHardOfHearing,BlindOrVisionDifficulty,DifficultyConcentrating,DifficultyWalking,DifficultyDressingBathing
,DifficultyErrands,SmokerStatus,ECigaretteUsage,ChestScan,AgeCategory,HeightInMeters,BMI,AlcoholDrinkers
,HIVTesting,FluVaxLast12,PneumoVaxEver,TetanusLast10Tdap,HighRiskLastYear,CovidPos] ])

if st.button('Predict'):

    result = Model.predict(input_data)[0]

    if result == 0:
        st.write('Heart Attack : NO')

    else:
        st.write('Heart Attack : YES')


