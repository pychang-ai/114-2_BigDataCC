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


## Ex 08
from keras_nlp.models import GPT2CausalLMPreprocessor 
from keras_nlp.models import GPT2CausalLM 
import gradio as gr 
import keras 

keras.mixed_precision.set_global_policy("mixed_float16") preprocessor = GPT2CausalLMPreprocessor.from_preset( "gpt2_base_en", sequence_length=128,  )

gpt2_1m = GPT2CausalLM.from_preset( "gpt2_base_en", preprocessor=preprocessor )

def predict(input): #使用模型進行預測 
	output = gpt2_1m.generate(input, max_length=200) 	return output

examples = ["My trip to New York was", "My trip to Taipei was"] app = gr.Interface(fn=predict, inputs="text", outputs="text", examples=examples) app.launch()



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

---

# Mini Project 主題（3 選 1 作為專題基礎，可延伸）

> 以下三個專案主題建構在本週 EX01–EX08 之上，**可作為期末專題的起點或練手 demo**。
> 每題列出：**基礎範例 → 核心改造 → 延伸方向**。
> 自由發揮、不繳交、不計分，做完想 demo 課堂上可分享。

---

## Project 1：海洋生物影像辨識器

> **基礎範例**：EX05（MobileNet）或 EX06（ResNet50）

### 核心改造

用預訓練 ImageNet 模型辨識海洋生物（鯨魚、海豚、章魚、海龜、鯊魚、海星、水母…）。Gradio 上傳照片 → 顯示「最可能 Top-3 類別」與信心分數。

### 起手程式範例

```python
import gradio as gr
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from PIL import Image
import numpy as np

model = ResNet50(weights="imagenet")

def classify(img):
    img = Image.fromarray(img).resize((224, 224))
    arr = preprocess_input(np.array(img).reshape((1, 224, 224, 3)))
    pred = model.predict(arr, verbose=0)
    top3 = decode_predictions(pred, top=3)[0]
    return {name: float(score) for _, name, score in top3}

gr.Interface(fn=classify, inputs=gr.Image(), outputs=gr.Label(num_top_classes=3),
             title="海洋生物辨識器").launch()
```

### 延伸方向（任選）

| # | 延伸 | 難度 |
|---|---|---|
| 1 | 收集 30 張高雄港、旗津海邊自己拍的照片，跑一輪看辨識準確率 | ⭐ |
| 2 | 改用 MobileNet 比較速度差異（手機端用 MobileNet 較合理）| ⭐ |
| 3 | 加 `gr.Examples` 內建幾張海洋生物示範圖 | ⭐⭐ |
| 4 | 用 `keras_cv` 換成 YOLOv8 偵測**多隻**生物並標 bounding box | ⭐⭐⭐ |
| 5 | Fine-tune 一個自己的海洋生物分類器（搭配 Kaggle 資料集）| ⭐⭐⭐⭐ |

---

## Project 2：海事新聞情感分析器

> **基礎範例**：EX07（BERT 情感分析）

### 核心改造

把英文情感分析改造為**海事相關文字情感分析**——輸入海事新聞、漁民推文、港口公告，判斷正負情感。Gradio 輸入文字 → 輸出「正面 / 負面」機率。

### 起手程式範例

```python
import gradio as gr
import keras_nlp

labels = ["負面", "正面"]
preprocessor = keras_nlp.models.BertPreprocessor.from_preset(
    "bert_tiny_en_uncased_sst2", sequence_length=128)
classifier = keras_nlp.models.BertClassifier.from_preset(
    "bert_tiny_en_uncased_sst2", num_classes=2, preprocessor=preprocessor)

def analyze(text):
    output = classifier.predict([text])
    return {labels[i]: float(output[0][i]) for i in range(2)}

examples = [
    "The port operation has been smooth this month.",
    "Typhoon warning issued, all fishing boats must return.",
    "Marine pollution detected near Kaohsiung harbor."
]
gr.Interface(fn=analyze, inputs="text", outputs=gr.Label(num_top_classes=2),
             examples=examples, title="海事新聞情感分析").launch()
```

### 延伸方向（任選）

| # | 延伸 | 難度 |
|---|---|---|
| 1 | 一次貼 5–10 則新聞，輸出每則的情感結果（多筆批次處理）| ⭐⭐ |
| 2 | 加 Matplotlib 折線圖，顯示過去 30 天海事新聞情感趨勢 | ⭐⭐⭐ |
| 3 | 抓中央氣象署颱風公告或海委會新聞 RSS，自動分析 | ⭐⭐⭐ |
| 4 | 用中文 BERT（`bert-base-chinese`）改做中文情感分析 | ⭐⭐⭐ |
| 5 | 加入第三類「中立」標籤，用 zero-shot classification | ⭐⭐⭐⭐ |

---

## Project 3：海洋探險故事生成器

> **基礎範例**：EX08（GPT-2 文字生成）

### 核心改造

給開頭一句（如「一艘漁船在颱風夜航向高雄港...」），GPT-2 自動接續寫海洋冒險小故事。Gradio 文字輸入 → 文字輸出，加 slider 控制故事長度。

### 起手程式範例

```python
import gradio as gr
import keras
from keras_nlp.models import GPT2CausalLM, GPT2CausalLMPreprocessor

keras.mixed_precision.set_global_policy("mixed_float16")
preprocessor = GPT2CausalLMPreprocessor.from_preset("gpt2_base_en", sequence_length=128)
gpt2 = GPT2CausalLM.from_preset("gpt2_base_en", preprocessor=preprocessor)

def generate(prompt, max_len):
    return gpt2.generate(prompt, max_length=int(max_len))

examples = [
    "A fishing boat sailed into the typhoon night,",
    "The lighthouse keeper saw something strange in the waves,",
    "Captain Lee discovered an old map showing a sunken ship near"
]
gr.Interface(
    fn=generate,
    inputs=["text", gr.Slider(50, 400, value=200, label="故事長度")],
    outputs="text",
    examples=[[ex, 200] for ex in examples],
    title="海洋探險故事生成器"
).launch()
```

### 延伸方向（任選）

| # | 延伸 | 難度 |
|---|---|---|
| 1 | 加 `gr.Slider` 控制 temperature（創意度）| ⭐⭐ |
| 2 | 用 `gr.Chatbot` 元件做多輪對話式故事接龍 | ⭐⭐⭐ |
| 3 | 用 Gemini API / OpenAI API 取代 GPT-2，產出較好品質故事 | ⭐⭐⭐ |
| 4 | 故事生成後再呼叫 Stable Diffusion 自動畫插圖 | ⭐⭐⭐⭐ |
| 5 | 連結 W14 Docker，把整個故事生成器包成容器部署到 AWS | ⭐⭐⭐⭐⭐ |

---

## 三個專案如何接到期末專題？

| 期末專題方向 | 可用本週哪個專案做起點 |
|---|---|
| 影像辨識類（船型分類、衛星雲圖、海廢辨識）| Project 1 |
| 文字分析類（漁民訪談、海事報告分類、論壇情緒）| Project 2 |
| 互動式 AI 工具（聊天機器人、學習助手）| Project 3 |

選一個動手做，期末就少寫一半。
