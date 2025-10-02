#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app, db, User

def check_users():
    with app.app_context():
        users = User.query.all()
        print("=== 사용자 데이터 ===")
        print(f"총 사용자 수: {len(users)}")
        print()
        
        for i, user in enumerate(users, 1):
            print(f"{i}. ID: {user.id}")
            print(f"   사용자명: {user.username}")
            print(f"   이메일: {user.email}")
            print(f"   비밀번호 해시: {user.password_hash[:20]}...")
            print()

if __name__ == "__main__":
    check_users()
