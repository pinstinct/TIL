from PIL import Image, ImageDraw, ImageFont  # pip install pillow


def main():
    """이미지 크기 변경 및 회전 """
    path = './python/python-library-recipe/8-특정-데이터-포맷-다루기/sample.jpg'
    # 이미지 파일 불러오기
    img = Image.open(path)
    # 이미지 크기 변경
    # 인수: size(width, height 튜플 지정), resample(리샘플링 필터 지정)
    # 리샘플링 필터: PIL.Image.NEAREST(최근접법), PIL.Image.BILINEAR(바이리니어법), PIL.Image.BICUBIC(바이큐빅법), PIL.Image.LANCZOS(란초스법)
    # 일반적으로 란초스 또는 바이큐빅 리샘플링이 완성도가 좋음
    # 처리 속도가 요구될 때는 비용 대비 효과가 좋은 바이리니어법도 좋음
    resized_img = img.resize((200, 200))
    # 이미지 회전
    rotated_img = resized_img.rotate(90)
    # 이미지 저장
    # 인수: file_path, format(JPEG, JPEG200, PNG, BMP 등), **params(format에 따라 옵션이 다름)
    rotated_img.save('processed_sample1.jpg', quality=100)
    # format 인수를 생략하면 파일 이름 확장자로 자동 판별
    rotated_img.save('processed_sample1.png', format='PNG', compress_level=1)
    rotated_img.save('processed_sample2.png', compress_level=1)
    rotated_img.save('processed_sample1.gif')
    rotated_img.save('processed_sample1.bmp')

    """텍스트 넣기 """
    draw = ImageDraw.Draw(img)
    # 폰트 크기와 종류를 지정
    font = ImageFont.truetype('~/Library/Fonts/Hack-Bold.ttf', 22)
    # 텍스트 넣기
    draw.text((63, 7), 'Python!', font=font, fill='#000')
    img.save('draw_text.png', format='PNG')


if __name__ == "__main__":
    main()
