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
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")

# ==========================================
# 3. ADD QUESTION (添加新题目)
# ==========================================
def add_question(question, opt_a, opt_b, opt_c, answer):
    """向数据库中插入一道新题目"""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        insert_sql = """
        INSERT INTO Questions (QuestionText, OptionA, OptionB, OptionC, CorrectAnswer) 
        VALUES (?, ?, ?, ?, ?);
        """
        cursor.execute(insert_sql, (question, opt_a, opt_b, opt_c, answer))
        conn.commit()
        conn.close()
        print("Question added successfully!")
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")

# ==========================================
# 4. VIEW ALL QUESTIONS (查看所有题目)
# ==========================================
def view_all_questions():
    """从数据库中获取并打印所有题目"""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Questions;")
        questions = cursor.fetchall()
        conn.close()
        for q in questions:
            print(f"ID: {q[0]} | Q: {q[1]} | Ans: {q[5]}")
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")

if __name__ == "__main__":
    setup_database()
    # 测试新添加的功能
    add_question("What is 1+1?", "1", "2", "3", "B")
    view_all_questions()