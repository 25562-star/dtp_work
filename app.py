import sqlite3

# ==========================================
# 1. CONSTANTS (常量设置)
# ==========================================
DATABASE_NAME = "study_guide.db"

# ==========================================
# 2. DATABASE SETUP (数据库初始化)
# ==========================================
def setup_database():
    """连接到数据库，如果 Questions 表不存在则创建它"""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS Questions (
            QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
            QuestionText TEXT NOT NULL,
            OptionA TEXT NOT NULL,
            OptionB TEXT NOT NULL,
            OptionC TEXT NOT NULL,
            CorrectAnswer TEXT NOT NULL
        );
        """
        cursor.execute(create_table_sql)
        conn.commit()
        conn.close()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")

if __name__ == "__main__":
    setup_database()