import coremltools
from keras.models import load_model

coreml_model = coremltools.converters.keras.convert(
'animal_cnn_aug.h5',
input_names='image',
image_input_names='image',
output_names='Prediction',
class_labels=['monkey','boar','crow'],)
coreml_model.save('/Users/daiki/animalai/animal_cnn_aug.mlmodel')
