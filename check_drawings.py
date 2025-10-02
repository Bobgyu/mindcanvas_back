import sys
import os
sys.path.append('.')

from app import app, db, Drawing, User

with app.app_context():
    try:
        drawings = Drawing.query.all()
        print(f'총 그림 개수: {len(drawings)}')
        
        for drawing in drawings:
            print(f'ID: {drawing.id}, User ID: {drawing.user_id}, 분석결과: {drawing.analysis_result is not None}')
            if drawing.image_path:
                print(f'  이미지 경로: {drawing.image_path}')
                print(f'  파일 존재: {os.path.exists(drawing.image_path)}')
        
        users = User.query.all()
        print(f'\n총 사용자 개수: {len(users)}')
        for user in users:
            print(f'User ID: {user.id}, Username: {user.username}')
            
    except Exception as e:
        print(f'오류: {e}')
