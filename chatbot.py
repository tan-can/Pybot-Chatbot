
import streamlit as st
import random
import re
import requests
import urllib.parse


# ============================================================
# PYBOT V3
# Python + AI + ML + Data Science + India + Shopping + GK
# ============================================================


# ============================================================
# KNOWLEDGE BASE
# ============================================================

intents = {

    # --------------------------------------------------------
    # GENERAL CONVERSATION
    # --------------------------------------------------------

    "greeting": {
        "patterns": [
            "hello",
            "hi",
            "hey",
            "hey there",
            "good morning",
            "good afternoon",
            "good evening",
            "how are you",
            "how are you doing"
        ],
        "responses": [
            "Hey! 👋 I'm PyBot.",
            "Hello! How can I help you today?",
            "Hey there! 😄 Ask me anything.",
            "Hi! Ready when you are 🐍"
        ]
    },

    "name": {
        "patterns": [
            "what is your name",
            "who are you",
            "tell me your name",
            "what should i call you",
            "your name"
        ],
        "responses": [
            "I'm PyBot 🐍",
            "You can call me PyBot!",
            "I'm PyBot — a Python-powered chatbot."
        ]
    },

    "creator": {
        "patterns": [
            "who created you",
            "who made you",
            "who built you",
            "who programmed you"
        ],
        "responses": [
            "I was built using Python! 🐍",
            "I was created as a Python chatbot project.",
            "Python is doing most of the heavy lifting here 😎"
        ]
    },

    "help": {
        "patterns": [
            "help",
            "what can you do",
            "what do you know",
            "how can you help me",
            "what can i ask you"
        ],
        "responses": [
            "I can answer questions about Python, AI, ML, Data Science, Data Analytics, India, humans and general knowledge.",
            "Try asking me: 'What is machine learning?', 'What is Python?', or 'Tell me about India'.",
            "Ask me technical questions or general-knowledge questions!"
        ]
    },

    "goodbye": {
        "patterns": [
            "bye",
            "goodbye",
            "see you",
            "see you later",
            "exit",
            "quit"
        ],
        "responses": [
            "Bye! 👋 Keep learning.",
            "See you later! 🐍",
            "Goodbye! Keep coding!",
            "Bye! Come back when you have another question 😄"
        ]
    },


    # ========================================================
    # PYTHON
    # ========================================================

    "python": {
        "patterns": [
            "what is python",
            "tell me about python",
            "what is python programming",
            "why learn python",
            "why is python popular",
            "is python easy",
            "what is python used for",
            "applications of python",
            "uses of python",
            "python programming language"
        ],
        "responses": [
            "Python is a high-level, general-purpose programming language known for readable syntax. It's widely used in web development, automation, data science, AI and machine learning.",
            "Python is popular because its syntax is relatively simple and its ecosystem has libraries for almost every major area of software development.",
            "Python is used for AI, machine learning, data analysis, automation, web development, scientific computing and scripting."
        ]
    },

    "python_variables": {
        "patterns": [
            "what is a variable in python",
            "python variables",
            "how do variables work in python",
            "what are variables"
        ],
        "responses": [
            "A Python variable is a name that refers to an object. Example: age = 22.",
            "Python variables don't require you to explicitly declare a type. Example: name = 'Tanishka' and age = 22."
        ]
    },

    "python_list": {
        "patterns": [
            "what is a list in python",
            "python list",
            "explain python lists",
            "list in python"
        ],
        "responses": [
            "A Python list is an ordered, mutable collection. Example: fruits = ['apple', 'banana', 'mango'].",
            "Lists can store multiple values and can be modified after creation."
        ]
    },

    "python_dictionary": {
        "patterns": [
            "what is a dictionary in python",
            "python dictionary",
            "dictionary in python",
            "explain dictionaries"
        ],
        "responses": [
            "A Python dictionary stores data as key-value pairs. Example: student = {'name': 'Alex', 'age': 21}.",
            "Dictionaries are useful when you want to associate keys with values."
        ]
    },

    "python_function": {
        "patterns": [
            "what is a function in python",
            "python functions",
            "explain python functions",
            "what are functions"
        ],
        "responses": [
            "A function is a reusable block of code. You define one using 'def'. Example: def greet(): print('Hello!').",
            "Functions help organize code into reusable pieces."
        ]
    },

    "python_oop": {
        "patterns": [
            "what is oop in python",
            "python oop",
            "object oriented programming python",
            "classes in python",
            "objects in python"
        ],
        "responses": [
            "Object-oriented programming organizes software around classes and objects. Python supports concepts such as classes, inheritance, encapsulation and polymorphism.",
            "A class is like a blueprint, while an object is an instance created from that blueprint."
        ]
    },

    "python_libraries": {
        "patterns": [
            "python libraries",
            "important python libraries",
            "best python libraries",
            "python libraries for data science",
            "python libraries for ai"
        ],
        "responses": [
            "Popular Python libraries include NumPy, Pandas, Matplotlib, Requests, OpenCV, PyTorch and TensorFlow.",
            "For data work, Pandas and NumPy are especially common. For visualization, Matplotlib is widely used."
        ]
    },


    # ========================================================
    # ARTIFICIAL INTELLIGENCE
    # ========================================================

    "ai": {
        "patterns": [
            "what is ai",
            "what is artificial intelligence",
            "explain artificial intelligence",
            "define ai",
            "how does ai work",
            "what can ai do"
        ],
        "responses": [
            "Artificial intelligence is the field of building systems that can perform tasks associated with human intelligence, such as recognizing patterns, understanding language and making predictions.",
            "AI includes areas such as machine learning, deep learning, computer vision, natural language processing and robotics."
        ]
    },

    "generative_ai": {
        "patterns": [
            "what is generative ai",
            "what is gen ai",
            "explain generative ai",
            "how does generative ai work"
        ],
        "responses": [
            "Generative AI creates new content such as text, images, audio or code based on patterns learned from data.",
            "Large language models are a type of generative AI focused on generating and understanding language."
        ]
    },

    "chatbot": {
        "patterns": [
            "what is a chatbot",
            "how do chatbots work",
            "explain chatbot",
            "how is a chatbot made"
        ],
        "responses": [
            "A chatbot is software designed to communicate with users through text or voice. Modern chatbots can use rules, NLP models, machine learning or large language models.",
            "Simple chatbots use predefined rules, while advanced chatbots can use machine-learning or language models."
        ]
    },

    "computer_vision": {
        "patterns": [
            "what is computer vision",
            "explain computer vision",
            "computer vision ai",
            "what is image recognition"
        ],
        "responses": [
            "Computer vision is a field of AI that enables computers to process and interpret images and video.",
            "Computer vision is used for face detection, object detection, medical imaging, OCR, autonomous systems and more."
        ]
    },

    "nlp": {
        "patterns": [
            "what is nlp",
            "what is natural language processing",
            "explain nlp",
            "natural language processing"
        ],
        "responses": [
            "Natural Language Processing, or NLP, focuses on enabling computers to work with human language.",
            "NLP powers applications such as chatbots, translation, sentiment analysis, search and text classification."
        ]
    },


    # ========================================================
    # MACHINE LEARNING
    # ========================================================

    "machine_learning": {
        "patterns": [
            "what is machine learning",
            "what is ml",
            "explain machine learning",
            "how does machine learning work",
            "machine learning definition",
            "what is machine learning used for"
        ],
        "responses": [
            "Machine learning is a branch of AI where algorithms learn patterns from data and use those patterns to make predictions or decisions.",
            "Instead of explicitly programming every rule, machine-learning systems learn relationships from examples."
        ]
    },

    "supervised_learning": {
        "patterns": [
            "what is supervised learning",
            "supervised machine learning",
            "explain supervised learning",
            "examples of supervised learning"
        ],
        "responses": [
            "Supervised learning uses labeled training data. Common tasks include classification and regression.",
            "Examples include predicting house prices and classifying emails as spam or not spam."
        ]
    },

    "unsupervised_learning": {
        "patterns": [
            "what is unsupervised learning",
            "unsupervised machine learning",
            "explain unsupervised learning",
            "examples of unsupervised learning"
        ],
        "responses": [
            "Unsupervised learning finds patterns in data without predefined labels. Clustering is a common example.",
            "Customer segmentation using clustering is a common unsupervised-learning application."
        ]
    },

    "classification": {
        "patterns": [
            "what is classification",
            "classification in machine learning",
            "ml classification",
            "classification algorithm"
        ],
        "responses": [
            "Classification predicts a category or class. Examples include spam detection, disease classification and image recognition.",
            "Common classification algorithms include logistic regression, decision trees, random forests and support vector machines."
        ]
    },

    "regression": {
        "patterns": [
            "what is regression",
            "regression in machine learning",
            "ml regression",
            "regression algorithm"
        ],
        "responses": [
            "Regression predicts a numerical value. For example, predicting house prices or sales revenue.",
            "Linear regression, decision-tree regression and random-forest regression are examples of regression methods."
        ]
    },

    "overfitting": {
        "patterns": [
            "what is overfitting",
            "explain overfitting",
            "machine learning overfitting",
            "how to prevent overfitting"
        ],
        "responses": [
            "Overfitting happens when a model learns the training data too closely and performs poorly on unseen data.",
            "Techniques such as regularization, cross-validation, simpler models and more training data can help reduce overfitting."
        ]
    },

    "train_test": {
        "patterns": [
            "what is train test split",
            "why split data",
            "training and testing data",
            "train test data"
        ],
        "responses": [
            "A train-test split separates data used to train a model from data used to evaluate it on unseen examples.",
            "The test set should be kept separate from training so evaluation better reflects generalization."
        ]
    },

    "features": {
        "patterns": [
            "what are features in machine learning",
            "what is a feature",
            "ml features",
            "feature engineering"
        ],
        "responses": [
            "Features are input variables used by a machine-learning model to make predictions.",
            "Feature engineering involves creating or transforming useful input variables from raw data."
        ]
    },


    # ========================================================
    # DATA SCIENCE
    # ========================================================

    "data_science": {
        "patterns": [
            "what is data science",
            "explain data science",
            "what does a data scientist do",
            "data science definition",
            "what is data science used for"
        ],
        "responses": [
            "Data science combines statistics, programming, data analysis and machine learning to extract useful insights and build predictive systems.",
            "A data scientist may collect, clean, analyze and model data and communicate the resulting insights."
        ]
    },

    "data_analysis": {
        "patterns": [
            "what is data analysis",
            "explain data analysis",
            "what does a data analyst do",
            "data analytics",
            "data analyst"
        ],
        "responses": [
            "Data analysis involves examining, cleaning and interpreting data to find patterns, trends and useful insights.",
            "Data analysts commonly use SQL, Excel, Python, Pandas, visualization tools and business intelligence platforms."
        ]
    },

    "pandas": {
        "patterns": [
            "what is pandas",
            "python pandas",
            "why use pandas",
            "pandas library"
        ],
        "responses": [
            "Pandas is a Python library widely used for working with structured and tabular data.",
            "Pandas provides useful tools for filtering, cleaning, grouping, joining and analyzing datasets."
        ]
    },

    "numpy": {
        "patterns": [
            "what is numpy",
            "python numpy",
            "numpy library",
            "why use numpy"
        ],
        "responses": [
            "NumPy is a Python library for numerical computing. Its main structure is the multidimensional array.",
            "NumPy is widely used for numerical operations and forms part of the Python data-science ecosystem."
        ]
    },

    "data_visualization": {
        "patterns": [
            "what is data visualization",
            "data visualization",
            "why visualize data",
            "data charts",
            "data graphs"
        ],
        "responses": [
            "Data visualization represents information graphically so patterns and trends are easier to understand.",
            "Common visualizations include bar charts, line charts, scatter plots, histograms and box plots."
        ]
    },

    "sql": {
        "patterns": [
            "what is sql",
            "explain sql",
            "what is mysql",
            "what is a database",
            "sql database"
        ],
        "responses": [
            "SQL is a language used to work with relational databases. You can use it to query, insert, update and manage data.",
            "MySQL and PostgreSQL are examples of relational database systems that use SQL."
        ]
    },


    # ========================================================
    # HUMAN / BIOLOGY
    # ========================================================

    "human": {
        "patterns": [
            "what is a human",
            "what are humans",
            "tell me about humans",
            "human body",
            "how does the human body work"
        ],
        "responses": [
            "Humans are members of the species Homo sapiens. The human body contains interconnected systems such as the nervous, circulatory, respiratory and digestive systems.",
            "The human body is made up of cells organized into tissues, organs and organ systems."
        ]
    },

    "brain": {
        "patterns": [
            "what is the brain",
            "how does the brain work",
            "human brain",
            "tell me about brain"
        ],
        "responses": [
            "The brain is the central organ of the nervous system. It processes sensory information and helps coordinate movement, behavior and many other functions.",
            "The brain contains billions of neurons that communicate through electrical and chemical signals."
        ]
    },

    "dna": {
        "patterns": [
            "what is dna",
            "explain dna",
            "human dna",
            "what does dna do"
        ],
        "responses": [
            "DNA is a molecule that stores genetic information in living organisms.",
            "DNA contains sequences of bases that provide biological instructions, including information used to make proteins."
        ]
    },


    # ========================================================
    # INDIA
    # ========================================================

    "india": {
        "patterns": [
            "tell me about india",
            "what is india",
            "india",
            "about india",
            "indian history"
        ],
        "responses": [
            "India is a country in South Asia. It is a federal parliamentary democratic republic with New Delhi as its capital.",
            "India has a long history and enormous linguistic, cultural and geographic diversity."
        ]
    },

    "indian_cities": {
        "patterns": [
            "capital of india",
            "largest city in india",
            "cities in india",
            "famous cities in india",
            "indian cities"
        ],
        "responses": [
            "New Delhi is the capital of India. Major Indian cities include Mumbai, Delhi, Bengaluru, Chennai, Hyderabad and Kolkata.",
            "India has many major urban centers, including Mumbai, Delhi, Bengaluru, Chennai and Hyderabad."
        ]
    },

    "indian_technology": {
        "patterns": [
            "technology in india",
            "tech industry india",
            "indian tech industry",
            "software industry india"
        ],
        "responses": [
            "India has a large technology sector spanning IT services, software, startups, fintech, e-commerce, AI and semiconductor-related work.",
            "Major Indian technology hubs include Bengaluru, Hyderabad, Delhi NCR, Mumbai, Pune and Chennai."
        ]
    },


    # ========================================================
    # SHOPPING
    # ========================================================

    "shopping": {
        "patterns": [
            "where can i shop",
            "online shopping india",
            "shopping in india",
            "best shopping websites",
            "buy things online",
            "online shopping"
        ],
        "responses": [
            "For online shopping in India, common platforms include Amazon, Flipkart, Myntra, Ajio and Tata CLiQ.",
            "You can compare products across major Indian e-commerce platforms before buying."
        ]
    },

    "shopping_advice": {
        "patterns": [
            "how to choose a laptop",
            "how to choose a phone",
            "what should i check before buying",
            "shopping advice",
            "buying advice"
        ],
        "responses": [
            "Before buying, compare specifications, price, warranty, return policy, independent reviews and seller reputation.",
            "For electronics, pay particular attention to processor, RAM, storage, display, battery, warranty and after-sales support."
        ]
    },


    # ========================================================
    # GENERAL KNOWLEDGE
    # ========================================================

    "general_knowledge": {
        "patterns": [
            "what is the earth",
            "what is the sun",
            "what is the moon",
            "what is gravity",
            "what is photosynthesis",
            "what is the solar system",
            "what is a planet",
            "what is an atom"
        ],
        "responses": [
            "That's a general-knowledge question! I can also search Wikipedia when I don't recognize a question.",
            "I can look up general-knowledge questions using Wikipedia."
        ]
    }
}


# ============================================================
# TEXT PROCESSING
# ============================================================

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        "",
        text
    )

    return set(text.split())


def similarity(user_message, pattern):

    user_words = clean_text(user_message)

    pattern_words = clean_text(pattern)

    if not user_words or not pattern_words:
        return 0

    common_words = (
        user_words.intersection(pattern_words)
    )

    return len(common_words) / len(pattern_words)


def find_intent(user_message):

    best_intent = None

    best_score = 0

    for intent, data in intents.items():

        for pattern in data["patterns"]:

            score = similarity(
                user_message,
                pattern
            )

            if score > best_score:

                best_score = score

                best_intent = intent

    if best_score < 0.25:

        return None

    return best_intent


# ============================================================
# WIKIPEDIA SEARCH
# ============================================================

def wikipedia_search(question):

    search_url = (
        "https://en.wikipedia.org/w/api.php"
    )

    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": question,
        "srlimit": 1
    }

    try:

        response = requests.get(
            search_url,
            params=params,
            timeout=5
        )

        data = response.json()

        results = (
            data
            .get("query", {})
            .get("search", [])
        )

        if not results:

            return None

        title = results[0]["title"]

        encoded_title = urllib.parse.quote(
            title.replace(" ", "_")
        )

        summary_url = (
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            + encoded_title
        )

        summary_response = requests.get(
            summary_url,
            timeout=5
        )

        summary_data = (
            summary_response.json()
        )

        extract = summary_data.get(
            "extract"
        )

        if not extract:

            return None

        page_url = (
            summary_data
            .get("content_urls", {})
            .get("desktop", {})
            .get("page")
        )

        return {
            "title": title,
            "text": extract,
            "url": page_url
        }

    except Exception:

        return None


# ============================================================
# RESPONSE ENGINE
# ============================================================

def get_response(user_message):

    intent = find_intent(
        user_message
    )

    # Known chatbot topic
    if intent:

        return {
            "type": "chat",
            "text": random.choice(
                intents[intent]["responses"]
            )
        }

    # Unknown question → Wikipedia
    result = wikipedia_search(
        user_message
    )

    if result:

        return {
            "type": "wiki",
            "title": result["title"],
            "text": result["text"],
            "url": result["url"]
        }

    return {
        "type": "chat",
        "text": (
            "I don't know that one yet 🤔\n\n"
            "Try asking me about Python, AI, "
            "machine learning, data science, "
            "India or general knowledge."
        )
    }


# ============================================================
# STREAMLIT UI
# ============================================================

st.set_page_config(
    page_title="PyBot",
    page_icon="🐍",
    layout="centered"
)


st.title("🐍 PyBot")

st.caption(
    "Python • AI • ML • Data Science • India • GK"
)


# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------

with st.sidebar:

    st.header("🐍 PyBot")

    st.write(
        "Your Python-powered knowledge assistant."
    )

    st.divider()

    st.subheader("Try asking:")

    st.write("• What is machine learning?")

    st.write("• Explain supervised learning")

    st.write("• What is Pandas?")

    st.write("• What is artificial intelligence?")

    st.write("• Tell me about India")

    st.write("• What is DNA?")

    st.write("• Who was Albert Einstein?")

    st.divider()

    if st.button("🗑️ Clear conversation"):

        st.session_state.messages = []

        st.rerun()


# ============================================================
# CHAT HISTORY
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )

        if message.get("url"):

            st.caption(
                "Source: " + message["url"]
            )


# ============================================================
# USER INPUT
# ============================================================

user_message = st.chat_input(
    "Ask PyBot anything..."
)


if user_message:

    # --------------------------------------------------------
    # USER
    # --------------------------------------------------------

    st.session_state.messages.append({

        "role": "user",

        "content": user_message

    })

    with st.chat_message("user"):

        st.write(user_message)


    # --------------------------------------------------------
    # BOT
    # --------------------------------------------------------

    response = get_response(
        user_message
    )


    with st.chat_message("assistant"):

        if response["type"] == "wiki":

            st.write(
                "**" + response["title"] + "**"
            )

            st.write(
                response["text"]
            )

            if response["url"]:

                st.caption(
                    "Source: " + response["url"]
                )

        else:

            st.write(
                response["text"]
            )


    # --------------------------------------------------------
    # SAVE
    # --------------------------------------------------------

    st.session_state.messages.append({

        "role": "assistant",

        "content": (
            response.get("title", "")
            + "\n\n"
            + response["text"]
        ),

        "url": response.get("url")

    })

