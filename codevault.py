import streamlit as st
from random import shuffle

logo_path = "image.jpg"  # Replace with the path to your logo file
st.image(logo_path, width=150)  # Adjust width as necessary

# Define the quiz data
questions = [
    {
        "question": "1. Which data structure uses LIFO(last in, First out) principle?",
        "options": ["Stack", "Queue", "Linked List", "Binary Tree"],
        "answer": "Stack"
    },
    {
        "question": "2. What is the worst-case time complexity of Quick Sort?",
        "options": ["O(n^2)", "O(n log n)", "O(n)", "O(log n)"],
        "answer": "O(n^2)"
    },
    {
        "question": "3. Which of the following is not a NoSQL database?",
        "options": ["MongoDB", "Redis","MySQL", "Cassandra"],
        "answer": "MySQL"
    },
    {
        "question": "4. What is the purpose of a DDoS attack?",
        "options": ["To overwhelm a system with traffic", "To steal data", "To encrypt data for ransom", "To install malware"],
        "answer": "To overwhelm a system with traffic"
    },
    {
        "question": "5. In networking, what does the 'ping' command check?",
        "options": ["Connectivity", "Data speed", "Data encryption", "Bandwidth"],
        "answer": "Connectivity"
    },
    {
        "question": "6. Which programming paradigm focuses on objects and classes?",
        "options": ["Procedural Programming", "Functional Programming", "Object-Oriented Programming", "Logic Programming"],
        "answer": "Object-Oriented Programming"
    },
    {
        "question": "7. Which protocol is used for secure data transmission over the web?",
        "options": ["HTTP", "HTTPS", "FTP", "SMTP"],
        "answer": "HTTPS"
    },
    {
        "question": "8. Which of the following algorithms is used for finding the shortest path in a graph?",
        "options": ["Dijkstra's Algorithm", "Merge Sort", "Binary Search", "Quick Sort"],
        "answer": "Dijkstra's Algorithm"
    },
    {
        "question": "9. Which one is a client-side scripting language?",
        "options":  ["JavaScript", "Python", "Java", "PHP"],
        "answer": "JavaScript"
    },
    {
        "question": "10. In a relational database, what does SQL stand for?",
        "options": ["Structured Query Language", "Sequential Query Language", "Simple Query Language", "Standard Query Language"],
        "answer": "Structured Query Language"
    },
    {
        "question": "11. Which data structure is commonly used to implement recursion?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Stack"
    },
    {
        "question": "12. What is the main purpose of a firewall in computer networks?",
        "options": ["Prevent unauthorized access", "Increase bandwidth", "Provide data encryption", "Improve system speed"],
        "answer": "Prevent unauthorized access"
    },
    {
        "question": "13.Which sorting algorithm is known for having the best average case performance?",
        "options": ["Merge Sort", "Quick Sort", "Bubble Sort", "Selection Sort"],
        "answer": "Merge Sort"
    },
    {
        "question": "14.Which of the following is a low-level programming language?",
        "options": ["Assembly", "Python", "Java", "C++"],
        "answer":"Assembly"
    },
    {
        "question": "15. In computer architecture, which cache is closest to the CPU?",
        "options": ["L1 Cache", "L2 Cache", "L3 Cache", "Main Memory"],
        "answer": "L1 Cache"
    }
]

# Initialize or reset session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.correct_option = None

# Display score and question
st.title("Quiz Game")
st.subheader(f"Score: {st.session_state.score}")

# Function to display the next question
def next_question():
    st.session_state.current_question += 1

# Get current question
if st.session_state.current_question < len(questions):
    question_data = questions[st.session_state.current_question]
    question = question_data['question']
    options = question_data['options']
    correct_answer = question_data['answer']
    shuffle(options)

    st.session_state.correct_option = correct_answer  # Save the correct answer

    # Display question
    st.write(f"**{question}**")
    
    # Display options as buttons
    for i, option in enumerate(options):
        if st.button(option):
            if option == st.session_state.correct_option:
                st.session_state.score += 1
                st.success("WOW! ITS CORRECT! 🎉")
            else:
                st.error("OOPS! WRONG ANSWER! 😢")
                st.warning(f"The correct answer was: {st.session_state.correct_option}")
            
            st.button("Next Question", on_click=next_question)
            st.stop()  # Stop the app to allow the user to see the result
else:
 st.write(f"Quiz has ended! Your Score: {st.session_state.score}")
 st.write(f"THANK YOU")
 st.button("Restart", on_click=lambda: st.experimental_rerun())  # Reset the game
