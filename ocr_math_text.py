import argparse
from PIL import Image
from IPython.display import display

import cv2
from pix2text import Pix2Text

parser = argparse.ArgumentParser(
            prog='ProgramName',
            description='What the program does',
            epilog='Text at the bottom of help')
parser.add_argument('-f', '--filename',
                    default="./Test1.png", 
                    help='File to process')          
parser.add_argument('-o', '--output',
                    default='output.txt',
                    help='Output file')     

if __name__=="__main__":
    args = parser.parse_args()
    
    mfd_config = {
        "model_name":"mfd",
        "model_backend":"onnx"
    }

    formula_ocr_config = {
        "model_name":"mfr",
        "model_backend":"onnx"
    }

    languages = ['en', 'vi']

    text_formula_config = {
        'languages': languages,  # 'en,ch_sim
        'mfd': mfd_config,
        'formula': formula_ocr_config,
        'text': {},
    }

    total_config = {
        'layout': {},
        'text_formula': text_formula_config,
    }

    p2t = Pix2Text.from_config(
        total_configs=total_config,
        enable_formula=True,
        enable_table=True,
        device='cpu',
    )

    rec_kwargs = {}
    rec_kwargs['resized_shape'] = 640
    rec_kwargs['return_text'] = True
    rec_kwargs['auto_line_break'] = False

    # read image
    mixed_img = cv2.cvtColor(cv2.imread(args.filename), cv2.COLOR_BGR2RGB)  # load image
    mixed_img = Image.fromarray(mixed_img)

    outs2 = p2t.recognize(mixed_img,
                        file_type='text_formula',
                        return_text=True,
                        auto_line_break=False,
                        save_analysis_res=args.output + ".jpg")  # recognize mixed images
    
    with open(args.output + ".md", 'w', encoding="utf-8") as f:
        f.write(outs2)
        