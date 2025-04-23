import tensorflow as tf
import streamlit as st
import numpy as np
import pandas as pd
# import PIL.Image as Image

model = tf.keras.models.load_model("full_model.keras")





# model.summary()
class_names = ['Apple scab', 'Apple Black rot', 'Apple Cedar rust', 'Healthy Apple', 'Bacterial leaf blight in Rice Leaf', 'Bacterial Blight in corn Leaf', 'Brown spot in Rice Leaf', 'Common Rust in Corn Leaf', 'Gray Leaf Spot in Maize leaf', 'Healthy Rice', 'Leaf smut in Rice Leaf', 'Potato Early Leaf blight', 'Potato Late Leaf blight', 'Healthy Potato', 'Sogatella Rice Pest', 'Tomato Bacterial Spot', 'Tomato Early Leaf blight', 'Tomato Late Leaf blight', 'Tomato Leaf Mold', 'Tomato Septoria Leaf Spot', 'Two spotted spider mite in Tomato', 'Tomato Target Spot', 'Tomato Mosaic Leaf Virus', 'Healthy Tomato', 'Algal Leaf Spot', 'Anthracnose in Tea', 'Early Leaf Blight in Bell Pepper', 'Fusarium Wilt in Bell Pepper', 'Healthy Bell Pepper', 'Bird Eye spot in Tea', 'Brown Blight in Tea Leaves', 'CP Deficiency in Cabbages', 'Healthy Cabbage ', 'Healthy Maize', 'Healthy Tea Leaf', 'Maize FAW', 'Maize Streak Virus', 'Healthy Onions', 'Powdery Mildew in Onions', 'Hollow Heart in Potatoes', 'Red Leaf Spot in Tea', 'Tomato Canker']

infectious = ["Potato Late Leaf blight", "Tomato Late Leaf Blight","Tomato Mosaic Leaf Virus","Bacterial Leaf Blight in Rice Leaf","Maize Streak Virus","Tomato Bacterial Spot","Apple Cedar Rust","Gray Leaf Spot in Maize leaf","Maize FAW","Two spotted spider mite in Tomato"]

symptoms_list = ["Olive-green leaf spots, cracked/scaly fruit.","Brown leaf lesions with red edges, fruit rot mummy apples.","Yellow-orange leaf spots, swollen galls on juniper hosts.","Your Apple is perfectly healthy 😊🍎","Water-soaked leaf streaks turning yellow/brown.","Yellow, V-shaped leaf lesions.","Oval brown leaf spots with yellow halos.","Red-brown pustules on leaves.","Gray-tan rectangular leaf lesions.","Your rice is healthy 😊🌱","Black, powdery spore masses on leaves.","Dark concentric rings on leaves bullseye.","Water-soaked lesions, white mold in humid conditions.","Your potato is healthy 😊🥔"," Yellowing leaves, stunted plants, white nymphs on stems.","Small, water-soaked leaf spots with yellow halos.","Brown leaf spots with concentric rings.","Dark, greasy-looking leaf lesions.","Yellow upper-leaf patches, white mold underneath.","Small gray leaf spots with dark borders.","Speckled yellow leaves, fine webbing, leaf drop","Brown spots with concentric rings.","Mottled leaves, stunted growth.","Your tomato is healthy 😊🍅","Raised orange-brown spots with velvety texture.","Sunken brown lesions on leaves/stems.","Dark leaf spots with yellow halos.","Yellowing leaves, wilting.","Your Bell Pepper is healthy 😊🌶","Small gray spots with dark margins.","Irregular brown leaf lesions.","Purple-tinged leaves, stunted heads.","Your cabbage is healthy 😊🥬","Your maize is healthy 😊🌽","Your tea is healthy 😊🌱","Ragged leaf holes, windowed leaves, frass (sawdust-like waste) in whorls.Damaged tassels/ears, stunted growth.","Yellow leaf streaks, stunted growth","Your onion is healthy 😊🧄","White powdery patches on leaves.","Hollow cavities in tubers, cracks.","Reddish-brown circular leaf spots.","Wilting, stem cankers, fruit spots."]

Healthy = ["Healthy Apple","Healthy Rice","Healthy Potato","Healthy Tomato","Healthy Bell Pepper","Healthy Cabbage","Healthy Maize","Healthy Onions"]

causes_list = ["Fungus Venturia inaequalis.","Fungus Botryosphaeria obtusa.","Fungus Gymnosporangium juniperi-virginianae.","Your Apple is perfectly healthy 😊🍎","Bacterium Xanthomonas oryzae.","Bacterium Pseudomonas syringae.","Fungus Cochliobolus miyabeanus.","Fungus Puccinia sorghi.","Fungus Cercospora zeae-maydis.","Your rice is healthy 😊🌱","Fungus Entyloma oryzae.","Fungus Alternaria solani.","Oomycete Phytophthora infestans.","Your potato is healthy 😊🥔"," Planthopper (Sogatella furcifera), spreads viral diseases.","Bacterium Xanthomonas vesicatoria.","Fungus Alternaria solani.","Oomycete Phytophthora infestans."," Fungus Passalora fulva.","Fungus Septoria lycopersici.","Mites (Tetranychus urticae) thriving in dry heat.","Fungus Corynespora cassiicola.","Virus (ToMV).","Your tomato is healthy 😊🍅","Alga Cephaleuros virescens.","Fungus Colletotrichum spp.","Fungus Alternaria solani","Fungus Fusarium oxysporum.","Your Bell Pepper is healthy 😊🌶","Fungus Cercospora theae.","Fungus Glomerella cingulata.","Phosphorus/potassium deficiency in soil.","Your cabbage is healthy 😊🥬","Your maize is healthy 😊🌽","Your tea is healthy 😊🌱","Invasive pest (Spodoptera frugiperda), rapid reproduction, migratory moths.","Virus (MSV) spread by leafhoppers.","Your onion is healthy 😊🧄","Fungus Leveillula taurica.","Irregular watering, rapid growth spurts.","Fungus Exobasidium vexans.","Bacterium Clavibacter michiganensis."]

treatment_list = ["Fungicides (sulfur, mancozeb).","Remove infected branches; apply copper fungicides.","Fungicides (myclobutanil).","Your Apple is perfectly healthy 😊🍎","Copper-based sprays."," Copper fungicides.","Azoxystrobin fungicides.","Triazole fungicides.","Strobilurin fungicides.","Your rice is healthy 😊🌱","Carbendazim."," Chlorothalonil sprays.","Metalaxyl-based fungicides.","Your potato is healthy 😊🥔","Sogatella Rice","Copper sprays + mancozeb.","Chlorothalonil.","Fosetyl-Al.","Copper fungicides.","Mancozeb.","Miticides (abamectin) or insecticidal soap.","Azoxystrobin.","None (remove infected plants).","Your tomato is healthy 😊🍅","Copper fungicides.","Thiophanate-methyl.","Mancozeb.","Soil solarization; biofungicides (Trichoderma).","Your Bell Pepper is healthy 😊🌶","Copper oxychloride.","Carbendazim.","Apply balanced fertilizer (NPK 10-20-10).","Your cabbage is healthy 😊🥬","Your maize is healthy 😊🌽","Your tea is healthy 😊🌱","Early stage: Spray Bt (Bacillus thuringiensis) or spinosad.Late stage: Targeted pesticides (chlorantraniliprole).","None (remove plants).","Your onion is healthy 😊🧄","Sulfur sprays.","None (cosmetic issue; safe to eat).","Triadimefon.","Remove plants; disinfect tools."]

prevention_list = ["Resistant varieties (e.g., Liberty apples), prune for airflow.","Sanitize fallen leaves/fruit.","Remove nearby junipers | resistant apple varieties.","Your Apple is perfectly healthy 😊🍎","Use certified seeds | avoid flooding fields.","Rotate crops | avoid overhead irrigation.","Balanced nitrogen fertilization.","Early planting | resistant hybrids.","Crop rotation | tillage to bury residue.","Your rice is healthy 😊🌱"," Burn infected residues | avoid excess nitrogen."," Mulch soil | rotate crops."," Destroy infected tubers | avoid wet foliage.","Your potato is healthy 😊🥔","Remove weeds; avoid excessive nitrogen.","Use pathogen-free seeds | drip irrigation.","Stake plants | remove lower leaves.","Avoid overhead watering | space plants.","Greenhouse ventilation | resistant varieties.","Mulch | avoid wet foliage.","Increase humidity; release predatory mites.","Remove weeds | rotate crops.","Disinfect tools | use resistant varieties.","Your tomato is healthy 😊🍅","Improve air circulation | prune dense foliage.","Remove infected leaves | avoid shade.","Rotate crops | avoid overhead watering.","Resistant varieties | well-drained soil.","Your Bell Pepper is healthy 😊🌶","Prune for sunlight | avoid dense planting.","Balanced fertilization | remove infected leaves."," Test soil; use compost/manure.","Your cabbage is healthy 😊🥬","Your maize is healthy 😊🌽","Your tea is healthy 😊🌱","Plant Bt maize hybrids; use pheromone traps; rotate crops.","Control leafhoppers | plant resistant hybrids.","Your onion is healthy 😊🧄","Avoid overcrowding; drip irrigation.","Consistent irrigation; avoid over-fertilizing"," Prune regularly; avoid excess shade.","Use disease-free seeds | rotate crops."]



def get_prediction(image):
    image = tf.keras.preprocessing.image.load_img(image, target_size=(160, 160))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.expand_dims(image, 0)
    prediction = model.predict(image)
    predicted_index = np.argmax(prediction)
    predicted_class = class_names[np.argmax(prediction)]
    return predicted_index, predicted_class

def give_recommendations(pre_index):
    symptom = symptoms_list[pre_index]
    cause = causes_list[pre_index]
    treatment = treatment_list[pre_index]
    prevention = prevention_list[pre_index]
    return symptom, cause, treatment, prevention

    pass



st.header("_HOW TO USE KUZA :_ 🧙 ")
st.write("Despite the long descriptions on the previous page, KUZA Predict works by you simply taking a picture of a specific part of your crop . 📸")
st.write("Because this project is still relatively small, there's a specific list of crops and diseases below that can be predicted . ")
st.write("I strongly suggest having the table on fullscreen .  ")


valid_plants = pd.read_csv("Out_56.csv")

valid_plants.drop(valid_plants.columns[valid_plants.columns.str.contains(
    'unnamed', case=False)], axis=1, inplace=True)

valid_plants.drop(valid_plants.columns[valid_plants.columns.str.contains(
    '#', case=False)], axis=1, inplace=True)

st.dataframe(valid_plants)

try:
    image = st.file_uploader("Upload an image 📨")

    if image is not None:
        pre_index, preimage = get_prediction(image)
        symptom, cause, treatment, prevention = give_recommendations(pre_index)
        image = st.image(image)
        if preimage in Healthy:
            st.toast("Congratulations,your crop is healthy!🌱", icon="🥳")
            st.balloons()
        elif preimage in infectious:
            st.write(f"Your crop suffers from {preimage}")
            st.toast(f"Infectious disease {preimage} detected!", icon="☣")
            st.error("Be warned, the disease that plagues your crop is INFECTIOUS and you need to take action IMMEDIATELY.")
            st.subheader(preimage)

            col1, col2, col3, col4 = st.columns(4,gap="small",vertical_alignment="top",)
            with col1:
                st.subheader("Causes 👾")
                st.write(cause)
            with col2:
                st.subheader("Symptoms 🤧")
                st.write(symptom)
            with col3:
                st.subheader("Treatment Options ❤️‍🩹")
                st.write(treatment)
            with col4:
                st.subheader("Preventive Measures 😮‍💨")
                st.write(prevention)

        else:
            st.warning(f"Your crop suffers from {preimage}")
            st.toast(f"Disease {preimage} detected", icon="🤕")
            st.subheader(preimage)

            col1, col2, col3, col4 = st.columns(4, gap="small", vertical_alignment="top", )
            with col1:
                st.subheader("Causes")
                st.write(cause)
            with col2:
                st.subheader("Symptoms")
                st.write(symptom)
            with col3:
                st.subheader("Treatment Options")
                st.write(treatment)
            with col4:
                st.subheader("Preventive Measures")
                st.write(prevention)

    else:
        st.warning("Please upload an image")





except Exception as e:
    st.write(f"[error] {e}, please upload an image")

st.sidebar.header("KUZA Farmer's Companion 🧑‍🌾")
st.sidebar.subheader("By Baylen Chalopa - Data Scientist🧑‍💻")
st.sidebar.subheader("Contact me here: +254706574724")
st.sidebar.subheader("Email me at: baylenchalopa@gmail.com")







