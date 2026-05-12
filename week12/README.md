# Exercises
## EX01
```
import gradio as gr def greet(name): 	return "你好: " + name + "!" 	app = gr.Interface(fn=greet, 					inputs="text", 			outputs="text") 
app.launch()
```
## EX02
```
inputs = gr.Textbox(lines=2, placeholder="請輸入姓名..." label="請輸入使用者姓名") outputs = gr.Label() examples = ["陳會安", "江小魚"] app = gr.Interface(fn=greet, inputs=inputs, outputs=outputs, examples=examples, title = "歡迎使用者", description = "輸入姓名顯示歡迎訊息") app.launch()
```


## EX03

```
def greet(name, is_lady, fahrenheit): 	if is_lady: greeting = name + "女士你好!" 
	else: greeting = name + "男士你好!"  	greeting += "今天溫度是華氏: " + str(fahrenheit) 	celsius = (fahrenheit - 32) * 5 / 9 	return greeting, round(celsius, 2) app = gr.Interface(fn=greet, inputs=["text", "checkbox", gr.Slider(0, 100)], 		outputs=["text", "number"]) app.launch()
```

## Ex 04

```
import numpy as np from PIL import Image import gradio as gr 
def rgb2gray(input): 	img = Image.fromarray(input) 	img = img.convert('L') 
	return np.array(img)
app = gr.Interface(rgb2gray, gr.Image(image_mode="RGB"), "image") app.launch()
```

## Ex 05

```
from keras.applications.mobilenet import MobileNet 
from keras.applications.mobilenet import preprocess_input

from keras.applications.mobilenet import decode_predictions 
from PIL import Image 
import numpy as np 
import gradio as gr
model = MobileNet(weights="imagenet", include_top=True)

def resize_image(img, new_w, new_h): 	img = Image.fromarray(img) 
	w, h = img.size 	w_scale = new_w / w  	h_scale = new_h / h 
	scale = min(w_scale, h_scale)  	resized = img.resize((int(w*scale), int(h*scale)), Image.NEAREST)  	resized = resized.crop((0, 0, new_w, new_h))  	return resized

def predict(input): 
	input_resized = resize_image(input, 224, 224) 	img = np.array(input_resized) 
	img = img.reshape((1, 224, 224, 3)) img = preprocess_input(img)  	y_pred = model.predict(img, verbose=0)  label = decode_predictions(y_pred) top_prediction = label[0][0]  formatted_string = "%s (%.2f%%)" % (top_prediction[1], top_prediction[2]*100) return formatted_string
app = gr.Interface(fn=predict, inputs=gr.Image(), outputs="text")  app.launch()
```

## Ex 06

```
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input 
from keras.applications.resnet50 import decode_predictions 
from PIL import Image import numpy as np 
import gradio as gr 
model = ResNet50(weights="imagenet", include_top=True)

def resize_image(img, new_w, new_h): 
	img = Image.fromarray(img) 
	w, h = img.size
	w_scale = new_w / w 
	h_scale = new_h / h 
	scale = min(w_scale, h_scale) 
	resized = img.resize((int(w*scale), int(h*scale)), Image.NEAREST) 
	resized = resized.crop((0, 0, new_w, new_h)) 
	return resized

def predict(input): 	input_resized = resize_image(input, 224, 224) 
	img = np.array(input_resized) 	img = img.reshape((1, 224, 224, 3)) 
	img = preprocess_input(img) 	y_pred = model.predict(img, verbose=0)
	label = decode_predictions(y_pred)	max_len = len(label[0]) 
	max_len = 10 if max_len > 10 else max_len 
	top_10_predictions = {		label[0][i][1]: float(label[0][i][2])
		for i in range(max_len) 	}	return top_10_predictions

inputs = gr.Image() outputs = gr.Label(num_top_classes=3) app = gr.Interface(fn=predict, inputs=inputs, outputs=outputs) app.launch()
```
## Ex 07
import keras_nlp
import gradio as gr 

labels = ["負面", "正面"] 
model_name = "bert_tiny_en_uncased_sst2" 
preprocessor = keras_nlp.models.BertPreprocessor.from_preset( model_name, sequence_length=128,)

classifier = keras_nlp.models.BertClassifier.from_preset( model_name, num_classes=2, preprocessor=preprocessor)

def predict(input): 	output = classifier.predict([input]) 	predictions = { labels[i]: float(output[0][i]) for i in range(len(labels)) } 	return predictions

outputs = gr.Label(num_top_classes=2) examples = ["This movie is good.", "A total waste of my time."] app = gr.Interface(fn=predict, inputs="text", outputs=outputs, examples=xamples) app.launch()



# Software installation
## Download Miniconda

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

## Install Miniconda
```
bash Miniconda3-latest-Linux-x86_64.sh
```

## Setting Path for Miniconda

```
vi ~/.bashrc
```

add the following content into .bashrc file.

```
export PATH="$HOME/miniconda3/bin:$PATH"
```

## Validate the installation
```
conda --version
```
