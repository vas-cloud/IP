import streamlit as st

class College:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses


class Student:
    def __init__(self, marks, rank):
        self.marks = marks
        self.rank = rank


def suggest_college(student, preferred_college):
    colleges = [
        College("IIT Bombay", ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Aerospace Engineering", "Biotechnology", "Materials Science", "Mathematics and Computing", "Electronics and Communication"]),
        College("IIT Delhi", ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Biochemical Engineering and Biotechnology", "Production and Industrial Engineering", "Mathematics and Computing", "Electronics and Communication", "Computer Science and Applied Mathematics"]),
        College("IIT Madras", ["Aerospace Engineering", "Biotechnology", "Civil Engineering", "Computer Science", "Electrical Engineering", "Mechanical Engineering", "Chemical Engineering", "Metallurgical and Materials Engineering", "Naval Architecture and Ocean Engineering", "Engineering Physics"]),
        College("IIT Kanpur", ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Aerospace Engineering", "Materials Science and Engineering", "Nuclear Engineering and Technology", "Environmental Engineering", "Industrial and Management Engineering"]),
        College("IIT Kharagpur", ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Agricultural and Food Engineering", "Biotechnology", "Mining Engineering", "Ocean Engineering and Naval Architecture", "Industrial Engineering and Management"]),
        College("NIT Trichy", ["Computer Science", "Electrical and Electronics Engineering", "Mechanical Engineering", "Civil Engineering", "Electronics and Communication", "Instrumentation and Control Engineering", "Metallurgical and Materials Engineering", "Chemical Engineering", "Production Engineering", "Computer Science and Engineering"]),
        College("NIT Warangal", ["Computer Science", "Electrical and Electronics Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Biotechnology", "Metallurgical and Materials Engineering", "Electronics and Communication Engineering", "Industrial and Systems Engineering", "Computer Science and Engineering"]),
        College("NIT Surathkal", ["Computer Science", "Electrical and Electronics Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Electronics and Communication Engineering", "Information Technology", "Metallurgical and Materials Engineering", "Mining Engineering", "Computer Science and Engineering"]),
        College("NIT Calicut", ["Computer Science", "Electrical and Electronics Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Biotechnology", "Electronics and Communication Engineering", "Production Engineering", "Mechatronics", "Computer Science and Engineering"]),
        College("NIT Rourkela", ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Biotechnology", "Metallurgical and Materials Engineering", "Mining Engineering", "Electronics and Communication Engineering", "Industrial Design"]),
    ]

    if preferred_college and preferred_college in [college.name for college in colleges]:
        return next(college for college in colleges if college.name == preferred_college)
    elif student.rank <= 1000:
        return colleges[0]  # IIT Bombay
    elif student.rank <= 2000:
        return colleges[1]  # IIT Delhi
    elif student.rank <= 3000:
        return colleges[2]  # IIT Madras
    elif student.rank <= 4000:
        return colleges[3]  # IIT Kanpur
    elif student.rank <= 5000:
        return colleges[4]  # IIT Kharagpur
    elif student.rank <= 6000:
        return colleges[5]  # NIT Trichy
    elif student.rank <= 7000:
        return colleges[6]  # NIT Warangal
    elif student.rank <= 8000:
        return colleges[7]  # NIT Surathkal
    elif student.rank <= 9000:
        return colleges[8]  # NIT Calicut
    elif student.rank <= 10000:
        return colleges[9]  # NIT Rourkela
    else:
        return None  # No college suggestion


def suggest_course(college, student):
    if college is not None:
        available_courses = college.courses
        if student.marks >= 90:
            return available_courses[0]  # Top course for high marks
        elif student.marks >= 80:
            return available_courses[1]  # Second-best course for decent marks
        elif student.marks >= 70:
            return available_courses[2]  # Third-best course for moderate marks
        else:
            return available_courses[3]  # Fourth-best course for lower marks
    else:
        return None


def suggest_other_colleges(student):
    other_colleges = [
         College("IIT Bombay", ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Aerospace Engineering", "Biotechnology", "Materials Science", "Mathematics and Computing", "Electronics and Communication"]),
        College("IIT Delhi", ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Biochemical Engineering and Biotechnology", "Production and Industrial Engineering", "Mathematics and Computing", "Electronics and Communication", "Computer Science and Applied Mathematics"]),
        College("IIT Madras", ["Aerospace Engineering", "Biotechnology", "Civil Engineering", "Computer Science", "Electrical Engineering", "Mechanical Engineering", "Chemical Engineering", "Metallurgical and Materials Engineering", "Naval Architecture and Ocean Engineering", "Engineering Physics"]),
        College("IIT Kanpur", ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Aerospace Engineering", "Materials Science and Engineering", "Nuclear Engineering and Technology", "Environmental Engineering", "Industrial and Management Engineering"]),
        College("IIT Kharagpur", ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Agricultural and Food Engineering", "Biotechnology", "Mining Engineering", "Ocean Engineering and Naval Architecture", "Industrial Engineering and Management"]),
        College("NIT Trichy", ["Computer Science", "Electrical and Electronics Engineering", "Mechanical Engineering", "Civil Engineering", "Electronics and Communication", "Instrumentation and Control Engineering", "Metallurgical and Materials Engineering", "Chemical Engineering", "Production Engineering", "Computer Science and Engineering"]),
        College("NIT Warangal", ["Computer Science", "Electrical and Electronics Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Biotechnology", "Metallurgical and Materials Engineering", "Electronics and Communication Engineering", "Industrial and Systems Engineering", "Computer Science and Engineering"]),
        College("NIT Surathkal", ["Computer Science", "Electrical and Electronics Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Electronics and Communication Engineering", "Information Technology", "Metallurgical and Materials Engineering", "Mining Engineering", "Computer Science and Engineering"]),
        College("NIT Calicut", ["Computer Science", "Electrical and Electronics Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Biotechnology", "Electronics and Communication Engineering", "Production Engineering", "Mechatronics", "Computer Science and Engineering"]),
        College("NIT Rourkela", ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Biotechnology", "Metallurgical and Materials Engineering", "Mining Engineering", "Electronics and Communication Engineering", "Industrial Design"]),
        College("BITS Pilani", ["Computer Science", "Electrical and Electronics Engineering", "Mechanical Engineering", "Chemical Engineering", "Civil Engineering", "Biotechnology", "Electronics and Communication Engineering", "Computer Science and Engineering"]),
        College("IISc Bangalore", ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "Aerospace Engineering", "Materials Science", "Biotechnology", "Electronics and Communication", "Instrumentation"]),
        College("IIIT Hyderabad", ["Computer Science", "Electronics and Communication Engineering", "Computer Science and Information Technology", "Civil Engineering", "Biotechnology", "Electrical and Electronics Engineering", "Computer-Aided Structural Engineering", "VLSI and Embedded Systems"])
        # Add more colleges as needed
    ]

    good_colleges = [college.name for college in other_colleges if student.marks >= 80 and student.rank <= 5000]
    good_courses = [course for college in other_colleges if college.name in good_colleges for course in college.courses]

    return list(zip(good_colleges, good_courses))

global colleges
def main():
    st.title("Consultation App")
    
    marks = st.text_input("Enter Your JEE Marks", "Type Here....")
    rank = st.text_input("Enter Your JEE Rank", "Type Here....")
    preferred_college = st.selectbox("Select Your Preferred College (Optional)", [""] + [f"{'IIT' if i < 5 else 'NIT'} {i}" for i in range(1, 11)])
    
    if st.button("Submit"):
        student = Student(float(marks), int(rank))

        suggested_college = suggest_college(student, preferred_college)
        suggested_course = suggest_course(suggested_college, student)

        if suggested_college is not None and suggested_course is not None:
            st.success(f"Based on your JEE marks and rank, we suggest you consider {suggested_college.name} for {suggested_course}.")
        else:
            st.error("Sorry, we couldn't suggest a college and course based on your JEE marks and rank.")

        # st.header("Ranked List of Colleges and Courses:")
        # ranked_colleges = sorted([(college.name, suggest_course(college, student)) for college in colleges], key=lambda x: x[0])
        # for i, (college, course) in enumerate(ranked_colleges, start=1):
        #     st.write(f"{i}. {college} - {course}")

        st.header("Other Good Colleges and Courses:")
        other_colleges = suggest_other_colleges(student)
        for i, (college, course) in enumerate(other_colleges, start=1):
            st.write(f"{i}. {college} - {course}")


if __name__ == "__main__":
    main()
