import mysql.connector as mysql

attempts=3
while attempts>0:
    print("-"*75)
    password=input("Enter your administration password: ")
    print()

    if password=="admin123":
        print("Access Granted!")
        print("-"*75)

        quizdb=mysql.connect(host="localhost",user="root",password="password",database="Quiz")
        quizcur=quizdb.cursor()
        quizcur.execute("CREATE TABLE IF NOT EXISTS questionsquiz(qno INT PRIMARY KEY, question VARCHAR(5000), opta VARCHAR(500), optb VARCHAR(500), optc VARCHAR(500), optd VARCHAR(500), answer VARCHAR(5000));")
        quizcur.execute("CREATE TABLE IF NOT EXISTS register(reg_no INT(5) PRIMARY KEY, pname VARCHAR(50), age INT(10), city VARCHAR(50), no_of_app INT(10));")
        quizcur.execute("CREATE TABLE IF NOT EXISTS scores(rege_no INT(5) PRIMARY KEY, partname VARCHAR(50), scores INT(50), totcorans INT(50), totwrong INT(50), totatt INT(50));")
        
        while True:
            print("Quiz Management Software")
            print()
            print("1. Import Questions")
            print("2. Participant Registration")
            print("3. Import Scores")
            print("4. Display Questions")
            print("5. Display Participants")
            print("6. Display Scores")
            print("-"*75)
            choice=int(input(">>> "))
            print("-"*75)

            if choice==1:
                while True:
                    try:
                        ques_no=int(input("Enter the Question Number: "))
                        ques_desc=input("Enter the Question: ")
                        ans_a=input("Enter Option A: ")
                        ans_b=input("Enter Option B: ")
                        ans_c=input("Enter Option C: ")
                        ans_d=input("Enter Option D: ")
                        ans=input("Enter the Correct Answer: ").upper()

                        quesquery=f"INSERT INTO questionsquiz VALUES({ques_no},'{ques_desc}','{ans_a}','{ans_b}','{ans_c}','{ans_d}','{ans}');"
                        quizcur.execute(quesquery)
                        quizdb.commit()
                        print("-"*75)
                        print("Quiz Question has successfully been added.")
                        print("-"*75)

                        more=input("Press N to stop adding more questions: ").upper()
                        print()
                        if more=='N':
                            break

                    except mysql.errors.IntegrityError:
                        print("Question number already in use!")

                    except ValueError:
                        print("Incorrect Value Type")


            elif choice==2:
                while True:
                    try:
                        regno=int(input("Enter the Participant Registration Number: "))
                        regname=input("Enter the Participant Name: ")
                        regage=int(input("Enter the Participant Age: "))
                        regcity=input("Enter the City: ")
                        regappear=int(input("Enter the Number of Appearances Made: "))

                        regquery=f"INSERT INTO register VALUES({regno},'{regname}',{regage},'{regcity}',{regappear});"
                        quizcur.execute(regquery)
                        quizdb.commit()
                        print("-"*75)
                        print("Participant Details have successfully been added.")
                        print("-"*75)

                        more=input("Press N to stop adding more participants: ").upper()
                        print()
                        if more=='N':
                            break

                    except mysql.errors.IntegrityError:
                            print("Participant registration number already in use.")
                    
                    except ValueError:
                        print("Incorrect Value Type")

            elif choice==3:
                while True:
                    try:
                        score_regno=int(input("Enter the Participant Registration Number: "))
                        score_regname=input("Enter the Participant Name: ")
                        scores=int(input("Enter the Scores: "))
                        tot_cor_ans=int(input("Enter the Total Correct Answers: "))
                        inc_ans=int(input("Enter the Incorrect Answers: "))
                        no_att_ques=int(input("Enter the Number of Attempted Questions: "))

                        scorequery=f"INSERT INTO scores VALUES({score_regno},'{score_regname}',{scores},{tot_cor_ans},{inc_ans},{no_att_ques});"
                        quizcur.execute(scorequery)
                        quizdb.commit()
                        print("-"*75)
                        print("Participant Scores have successfully been added.")
                        print("-"*75)

                        more=input("Press N to stop adding more scores: ").upper()
                        print()
                        if more=='N':
                            break
                    
                    except mysql.errors.IntegrityError:
                            print("Participant registration number already in use.")

                    except ValueError:
                        print("Incorrect Value Type")
                        
            elif choice==4:
                quizcur.execute("SELECT * FROM questionsquiz;")
                data=quizcur.fetchall()
                print()
                for i in data:
                    print(f"Quesition No.: {i[0]}")
                    print(f"Quesition: {i[1]}")
                    print(f"Option A: {i[2]}")
                    print(f"Option B: {i[3]}")
                    print(f"Option C: {i[4]}")
                    print(f"Option D: {i[5]}")
                    print(f"Answer: {i[6]}")
                    print()
                print("-"*75)

            elif choice==5:
                quizcur.execute("SELECT * FROM register;")
                data=quizcur.fetchall()
                print()
                for i in data:
                    print(f"Registration No.: {i[0]}")
                    print(f"Name: {i[1]}")
                    print(f"Age: {i[2]}")
                    print(f"City: {i[3]}")
                    print(f"No. of Appearances: {i[4]}")
                    print()
                print("-"*75)

            elif choice==6:
                quizcur.execute("SELECT * FROM scores;")
                data=quizcur.fetchall()
                print()
                for i in data:
                    print(f"Registration No.: {i[0]}")
                    print(f"Name: {i[1]}")
                    print(f"Scores: {i[2]}")
                    print(f"Total Correct Answers: {i[3]}")
                    print(f"Total Wrong Answers: {i[4]}")
                    print(f"Total Attempted: {i[5]}")
                    print()
                print("-"*75)

else:
    print("Access Denied")
    attempts-=1
print("-"*75)