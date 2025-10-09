from app import app, db

with app.app_context():
    try:
        # chat 테이블의 모든 컬럼 확인
        result = db.engine.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'chat'")
        columns = [row[0] for row in result]
        print("Chat 테이블의 컬럼들:", columns)
        
        # is_read 컬럼이 있는지 확인
        if 'is_read' in columns:
            print("✅ is_read 컬럼이 존재합니다.")
        else:
            print("❌ is_read 컬럼이 없습니다. 추가하겠습니다.")
            db.engine.execute("ALTER TABLE chat ADD COLUMN is_read BOOLEAN DEFAULT FALSE")
            print("✅ is_read 컬럼을 추가했습니다.")
            
            # 다시 확인
            result = db.engine.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'chat'")
            columns = [row[0] for row in result]
            print("업데이트된 컬럼들:", columns)
            
    except Exception as e:
        print(f"오류 발생: {e}")
