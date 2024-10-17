Formula detection
https://www.kaggle.com/code/mikhailshkarubski/math-formula-detection-yolov8/notebook

p2t predict -l en,vi --mfd-config '{\"model_name\":\"mfd-pro\",\"model_backend\":\"onnx\"}' --formula-ocr-config '{\"model_name\":\"mfr-pro\",\"model_backend\":\"onnx\"}' --resized-shape 608 --no-auto-line-break --file-type text_formula -i ./Test1.png --save-debug-res ./out-debug-vi.jpg

p2t predict -l en,vi --mfd-config '{\"model_name\":\"mfd\",\"model_backend\":\"onnx\"}' --formula-ocr-config '{\"model_name\":\"mfr\",\"model_backend\":\"onnx\"}' --resized-shape 608 --no-auto-line-break --file-type text_formula -i ./Test1.png --save-debug-res ./out-debug-vi.jpg