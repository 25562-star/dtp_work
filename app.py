import sqlite3

DATABASE_NAME = "study_guide.db"

def setup_database():
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

def view_all_questions():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Questions;")
        questions = cursor.fetchall()
        conn.close()
        print("\n--- All Questions in Database ---")
        if not questions:
            print("The database is empty.")
        else:
            for q in questions:
                print(f"ID: {q[0]} | Q: {q[1]} | A: {q[2]} | B: {q[3]} | C: {q[4]} | Ans: {q[5]}")
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")

def add_question():
    print("\n--- Add a New Question ---")
    while True:
        text = input("Enter the quiz question text: ").strip()
        if text: break
        print("⚠️ Question text cannot be empty!")
    while True:
        opt_a = input("Enter Option A: ").strip()
        if opt_a: break
        print("⚠️ Option A cannot be empty!")
    while True:
        opt_b = input("Enter Option B: ").strip()
        if opt_b: break
        print("⚠️ Option B cannot be empty!")
    while True:
        opt_c = input("Enter Option C: ").strip()
        if opt_c: break
        print("⚠️ Option C cannot be empty!")
    while True:
        ans = input("Enter the correct answer (A, B, or C): ").strip().upper()
        if ans in ['A', 'B', 'C']: break
        print("⚠️ Invalid answer! You must type A, B, or C.")

    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Questions (QuestionText, OptionA, OptionB, OptionC, CorrectAnswer)
            VALUES (?, ?, ?, ?, ?);
        """, (text, opt_a, opt_b, opt_c, ans))
        conn.commit()
        conn.close()
        print("\n✅ Question added successfully!")
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")

def delete_question():
    print("\n--- Delete a Question ---")
    view_all_questions()
    id_input = input("\nEnter the Question ID to delete (or press Enter to cancel): ").strip()
    if not id_input:
        print("Deletion canceled.")
        return
    if not id_input.isdigit():
        print("⚠️ Invalid ID! Please enter a valid numerical ID.")
        return
    question_id = int(id_input)
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * WHERE QuestionID = ?;", (question_id,)) # 故意保持基础版的简单查询
        cursor.execute("SELECT * FROM Questions WHERE QuestionID = ?;", (question_id,))
        if not cursor.fetchone():
            print(f"⚠️ No question found with ID {question_id}.")
            conn.close()
            return
        cursor.execute("DELETE FROM Questions WHERE QuestionID = ?;", (question_id,))
        conn.commit()
        conn.close()
        print(f"\n✅ Question with ID {question_id} has been deleted.")
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")

# ==========================================
# 5. TAKE QUIZ (【阶段 4 新增】测验核心基础版)
# ==========================================
def take_quiz():
    """运行测验并记录分数"""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Questions;")
        questions = cursor.fetchall()
        conn.close()

        if not questions:
            print("\n⚠️ No questions available in the database! Please add some first.")
            return

        score = 0
        for q in questions:
            print(f"\nQuestion: {q[1]}")
            print(f"A. {q[2]}")
            print(f"B. {q[3]}")
            print(f"C. {q[4]}")
            
            # 基础版：直接获取用户输入，暂未做严格的拦截和大小写兼容
            user_answer = input("Your answer: ")
            if user_answer == q[5]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
                
        print(f"\nYour Score: {score} / {len(questions)}")
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")

# ==========================================
# 6. MAIN MENU (更新主菜单加入选项 4)
# ==========================================
def main_menu():
    setup_database()
    while True:
        print("\n" + "="*30)
        print(" STUDY GUIDE - MAIN MENU (STAGE 4)")
        print("="*30)
        print("1. View All Questions")
        print("2. Add a New Question")
        print("3. Delete a Question")
        print("4. Take Quiz")
        print("5. Exit")

        choice = input("Please select an option (1-5): ").strip()

        if choice == '1': view_all_questions()
        elif choice == '2': add_question()
        elif choice == '3': delete_question()
        elif choice == '4': take_quiz()
        elif choice == '5':
            print("\n👋 Goodbye!")
            break
        else:
            print("\n⚠️ Invalid option! Please choose between 1 and 5.")

if __name__ == "__main__":
    main_menu()