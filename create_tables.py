#!/usr/bin/env python3
"""
데이터베이스 테이블 생성 스크립트
"""

from app import app, db

def create_tables():
    with app.app_context():
        try:
            # 모든 테이블 생성
            db.create_all()
            print("✅ 데이터베이스 테이블 생성 완료")
            
            # 생성된 테이블 목록 확인
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"📋 생성된 테이블: {tables}")
            
        except Exception as e:
            print(f"❌ 테이블 생성 중 오류 발생: {e}")

if __name__ == "__main__":
    create_tables()
