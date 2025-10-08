#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2
from werkzeug.security import generate_password_hash

# 데이터베이스 연결 정보
DB_HOST = "34.64.71.12"
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "codelab0080**A"
DB_SCHEMA = "juyeoung"

# 관리자 계정 정보
ADMIN_USERNAME = "admin@gmail.com"
ADMIN_PASSWORD = "admin123"
ADMIN_EMAIL = "admin@gmail.com"

def setup_admin():
    try:
        # 데이터베이스 연결
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            options=f'-c search_path={DB_SCHEMA}'
        )
        cur = conn.cursor()
        
        print("✅ 데이터베이스 연결 성공!")
        
        # 1. is_admin 컬럼이 존재하는지 확인
        cur.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name='user' AND column_name='is_admin'
        """)
        
        if cur.fetchone() is None:
            print("📝 is_admin 컬럼 추가 중...")
            cur.execute('ALTER TABLE "user" ADD COLUMN is_admin BOOLEAN DEFAULT FALSE')
            conn.commit()
            print("✅ is_admin 컬럼 추가 완료!")
        else:
            print("ℹ️  is_admin 컬럼이 이미 존재합니다.")
        
        # 2. 기존 관리자 계정 확인
        cur.execute('SELECT id, username FROM "user" WHERE username = %s', (ADMIN_USERNAME,))
        existing_user = cur.fetchone()
        
        if existing_user:
            print(f"ℹ️  사용자 '{ADMIN_USERNAME}'이 이미 존재합니다.")
            print(f"   사용자 ID: {existing_user[0]}")
            
            # 관리자 권한 부여
            cur.execute('UPDATE "user" SET is_admin = TRUE WHERE username = %s', (ADMIN_USERNAME,))
            conn.commit()
            print(f"✅ 사용자 '{ADMIN_USERNAME}'에게 관리자 권한이 부여되었습니다!")
        else:
            # 3. 관리자 계정 생성
            print(f"📝 관리자 계정 '{ADMIN_USERNAME}' 생성 중...")
            password_hash = generate_password_hash(ADMIN_PASSWORD)
            
            cur.execute(
                'INSERT INTO "user" (username, password_hash, email, is_admin) VALUES (%s, %s, %s, %s)',
                (ADMIN_USERNAME, password_hash, ADMIN_EMAIL, True)
            )
            conn.commit()
            
            print("✅ 관리자 계정이 성공적으로 생성되었습니다!")
        
        # 계정 정보 출력
        print("\n" + "="*50)
        print("관리자 계정 정보:")
        print(f"  사용자명: {ADMIN_USERNAME}")
        print(f"  비밀번호: {ADMIN_PASSWORD}")
        print(f"  이메일: {ADMIN_EMAIL}")
        print("="*50)
        
        # 연결 종료
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    setup_admin()
