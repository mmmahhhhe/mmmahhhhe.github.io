# 新建AipOCR
from aip import AipOcr

from PIL import Image
import pytesseract

config = {
    'appId': '18352046',
    'apiKey': 'G8xejksIwpikkqODzWRrYlQK',
    'secretKey': 'fzQkupPRPc9YTY5E5vqWr5FPnLiAG9eg'
}

options = {}
options["probability"] = "true"
client = AipOcr(**config)

def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()

def img_to_str(image_path):
    image = get_file_content(image_path)
    result = client.basicGeneral(image, options)
    if 'words_result' in result:
        # average:置信度平均值
        # variance:置信度方差
        return '\n'.join([w['words'] for w in result['words_result']]) ,result['words_result'][0]['probability']
if __name__ == '__main__' :
    imagepath = './test/1.png'
    print('=='*20)
    word ,acc = img_to_str(imagepath)
    word2 = pytesseract.image_to_string(Image.open(imagepath), lang='chi_sim')
    print('百度云aip识别结果：', word)
    print('tesseract识别结果：', word2)

    print('文字识别的置信度均值：', float(acc['average'])*100,'%')
    print('文字识别的置信度方差：', acc['variance'])
    print('文字识别的置信度最小值：', float(acc['average'])*100, '%')