#!/usr/bin/env python3
"""
Drawing 테이블에 새로운 컬럼들을 추가하는 스크립트
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from sqlalchemy import text

def add_columns():
    with app.app_context():
        try:
            # drawing_type 컬럼 추가
            db.engine.execute(text("ALTER TABLE drawing ADD COLUMN IF NOT EXISTS drawing_type VARCHAR(50) DEFAULT 'normal'"))
            print("✅ drawing_type 컬럼 추가 완료")
            
            # original_image 컬럼 추가
            db.engine.execute(text("ALTER TABLE drawing ADD COLUMN IF NOT EXISTS original_image VARCHAR(255)"))
            print("✅ original_image 컬럼 추가 완료")
            
            # title 컬럼 추가
            db.engine.execute(text("ALTER TABLE drawing ADD COLUMN IF NOT EXISTS title VARCHAR(255)"))
            print("✅ title 컬럼 추가 완료")
            
            print("🎉 모든 컬럼이 성공적으로 추가되었습니다!")
            
        except Exception as e:
            print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    add_columns()
