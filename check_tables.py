from app import app, db

with app.app_context():
    try:
        # 모든 테이블 목록 확인
        result = db.engine.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        tables = [row[0] for row in result]
        print("데이터베이스의 모든 테이블들:", tables)
        
        # chat 테이블이 있는지 확인
        if 'chat' in tables:
            print("✅ chat 테이블이 존재합니다.")
            
            # chat 테이블의 컬럼들 확인
            result = db.engine.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'chat'")
            columns = [row[0] for row in result]
            print("chat 테이블의 컬럼들:", columns)
            
        else:
            print("❌ chat 테이블이 존재하지 않습니다.")
            print("테이블을 생성하겠습니다.")
            
            # 테이블 생성
            db.create_all()
            print("✅ 테이블 생성 완료")
            
            # 다시 확인
            result = db.engine.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            tables = [row[0] for row in result]
            print("생성된 테이블들:", tables)
            
    except Exception as e:
        print(f"오류 발생: {e}")
        import traceback
        traceback.print_exc()
