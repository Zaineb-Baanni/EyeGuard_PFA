# Importation des librairies
import cv2
import numpy as np
import face_recognition as face_rec

# Fonction pour redimensionner une image
def resize(img, size):
    height, width = img.shape[:2]  # Extraction de la hauteur et de la largeur de img.shape
    new_width = int(width * size)
    new_height = int(height * size)
    dimensions = (new_width, new_height)
    return cv2.resize(img, dimensions, interpolation=cv2.INTER_AREA)

# Chargement et pré-traitement des images
fadoua = face_rec.load_image_file('smape_images/fadoua.jpg')
fadoua = cv2.cvtColor(fadoua, cv2.COLOR_BGR2RGB)
fadoua = resize(fadoua, 0.50)

fadoua_test = face_rec.load_image_file('smape_images/fadoua_test.jpg')
fadoua_test = cv2.cvtColor(fadoua_test, cv2.COLOR_BGR2RGB)
fadoua_test = resize(fadoua_test, 0.50)


# Affichage des images initiales
cv2.imshow('Image principale', fadoua)
cv2.imshow('Image test', fadoua_test)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Détection des visages et encodage
face_location_fadoua = face_rec.face_locations(fadoua)[0]
encoded_fadoua = face_rec.face_encodings(fadoua)[0]
cv2.rectangle(fadoua, (face_location_fadoua[3], face_location_fadoua[0]), (face_location_fadoua[1], face_location_fadoua[2]), (255, 0, 255), 3)

face_location_fadoua_test = face_rec.face_locations(fadoua_test)[0]
encoded_fadoua_test = face_rec.face_encodings(fadoua_test)[0]
cv2.rectangle(fadoua_test, (face_location_fadoua_test[3], face_location_fadoua_test[0]), (face_location_fadoua_test[1], face_location_fadoua_test[2]), (255, 0, 255), 3)

results = face_rec.compare_faces([encoded_fadoua], encoded_fadoua_test)
print(results)
cv2.putText(fadoua_test, f'{results}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
# Affichage des images annotées
cv2.imshow('Image principale ', fadoua)
cv2.imshow('Image test ', fadoua_test)
cv2.waitKey(0)
cv2.destroyAllWindows()



