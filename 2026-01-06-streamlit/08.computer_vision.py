# pip install azure-ai-vision-imageanalysis
# pip install azure-core
# pip install pillow

from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from PIL import Image, ImageDraw, ImageFont

COMPUTER_VISION_ENDPOINT = ""
COMPUTER_VISION_KEY = ""

# 인증을 위한 Credential 객체 생성
credential = AzureKeyCredential(COMPUTER_VISION_KEY)

# 이미지 분석 클라이언트 생성
client = ImageAnalysisClient(
    endpoint=COMPUTER_VISION_ENDPOINT, 
    credential=credential
)

# 이미지 분석을 위한 함수
def get_image_info():
    file_path = input('분석할 이미지 파일 경로를 입력하세요: ')

    with open(file_path, 'rb') as image_file:
        image_data = image_file.read()
    
    # 이미지 분석 요청
    result = client.analyze(
        image_data = image_data, 
        visual_features = [
            VisualFeatures.TAGS, 
            VisualFeatures.CAPTION, 
            VisualFeatures.OBJECTS, 
        ]
    )

    # 분석 결과 출력
    print("이미지 태그: ")
    for tag in result.tags.list:
        print(f"- {tag.name} (신뢰도: {tag.confidence*100:.4f}%)")
    
    print('\n이미지 캡션: ')
    if result.caption is not None:
        print(f"- {result.caption.text} (신뢰도: {result.caption.confidence*100:.4f}%)")

    image = Image.open(file_path)
    draw = ImageDraw.Draw(image)

    print('\n객체 감지: ')
    for obj in result.objects.list:
        print(f"- {obj.tags[0].name} (신뢰도: {obj.tags[0].confidence*100:.4f}%), 위치: {obj.bounding_box}")

        x = obj.bounding_box['x']
        y = obj.bounding_box['y']
        w = obj.bounding_box['w']
        h = obj.bounding_box['h']
        
        draw.rectangle(((x, y), (x + w, y + h)), outline='red', width=3)
        draw.text((x, y - 10), f"{obj.tags[0].name} ({obj.tags[0].confidence*100:.1f}%)", fill='red')
    
    image.show()
    image.save('output.jpg')

get_image_info()