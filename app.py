# import streamlit as st
# from streamlit_chat import message
# import requests
# import json

# # API configuration for Groq
# API_URL = "https://api.groq.com/openai/v1/chat/completions"
# API_KEY = "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"  # Replace with your actual Groq API key

# # Hardcoded company information from JSON file
# company_info = {
#     "role": "user",
#     "content": {
#       "Company Name": "RUGVED SYSTEMS INC",
#       "Full Form": "Remote Unmanned Ground Vehicular Electronics Defence systems",
#       "Description": "RUGVED SYSTEMS is a defence related student project from MIT Manipal. They work on different panels like surveillance, law enforcement, military assist, and civil defence. They participate in international competitions like IGVC, etc. They also had a contract with DRDO in building defence related projects.",
#       "Subsytems": [
#         {
#           "Name": "AI and Robotics",
#           "Activities": [
#             "AI Nav - Anonymously traversing based on the input of sensor and data.",
#             "Image Stitching - Enables better view of surroundings.",
#             "Operationalizing Deep learning in real-world scenarios - Detect lanes, objects, track humans, face verification in real-time.",
#             "Path Planning - Navigating the shortest route from current position to target position.",
#             "Control - Feedback from IMU, Encoder, and GPS.",
#             "Sensor Fusion - Combining various sensor data for precise data.",
#             "Communication - Designing software pipelines for hardware interfacing."
#           ],
#           "Achievements": [
#             "AI Gun - Sorting and tracking algorithms to detect and track humans for Border Security Force personnel.",
#             "TRAFFICMUNDA - Traffic management app using reinforcement learning.",
#             "Guiding Gaze - Top 7 in OpenCV AI International Competition 2023.",
#             "IIT Bombay Eyantra - Ranked 10th in India.",
#             "AI FOR CHANGE - Winners in the 'AI FOR CHANGE' hackathon."
#           ]
#         },
#         {
#           "Name": "Electronics",
#           "Projects": [
#             "6 DOF Robotic Arm - Driven by servos and controlled by Arduino.",
#             "3-Wheeled omni-directional bot - Developed on STM32 Platform, Bluetooth controlled.",
#             "Line Follower Robot - Developed for BITs Goa’s QUARK 2024.",
#             "Quadcopter - Developed on PIXHAWK Platform.",
#             "Line Follower/ Roboclench Bot/ Roborace Bot - Compete at BITS Goa Techfest.",
#             "OMNI BOT V - Introduction to robotics and unconventional steering.",
#             "DRONE - High-range UAV for aerial mapping."
#           ]
#         },
#         {
#           "Name": "RESEARCH",
#           "Achievements": [
#             "AI in Aerospace - GCAAMS-2024 accepted paper.",
#             "Image Dehazing - Novel method using GANs and transformers.",
#             "Optimization Algorithm - Research on optimization algorithms in AI.",
#             "SpaceCraft Pose Estimation - Novel approach using YOLO, CNN, and multi-task training."
#           ]
#         },
#         {
#           "Name": "MECHANICAL",
#           "Activities": [
#             "Simulations and FEA - Simulating parts using finite element analysis.",
#             "Vehicle dynamics - Designing based on vehicle dynamics.",
#             "Structures and CAD - Designing power architecture, converters, battery packs.",
#             "Materials and Manufacturing - Selection of materials and in-house manufacturing.",
#             "ROBOTIC ARM - Precision engineering project.",
#             "Omni bot V2 - Upgraded omni-directional bot.",
#             "Mini Walrus - Unmanned vehicle with caterpillar track wheels.",
#             "IGVC - Intelligent ground vehicle with advanced sensors and AI."
#           ]
#         },
#         {
#           "Name": "Management",
#           "Activities": [
#             "MERCH Designing",
#             "RECRUITMENT PROCESS",
#             "SOCIAL MEDIA",
#             "WEBSITE maintenance",
#             "Event calendar"
#           ]
#         }
#       ],
#       "Competitions": [
#         "Line following Robot, BITS goa (Top 7)",
#         "Guiding Gaze - Top 7 in OpenCV AI International Competition 2023",
#         "IIT Bombay Eyantra (Currently Ranked 3rd in India)",
#         "Finalist in SIH and Second runner-up in internal hackathon SIH 2023",
#         "Finalist in MedTech Hackathon organized by MAHE-GOK bioincubator 2022",
#         "Finalist in Manthan",
#         "Finalist in CDAC Grand Challenge",
#         "1st place in Pragyaan Fusion Hackathon, NIT-Trichy 2021",
#         "1st place in 'Covideate', IIT Bombay's Techfest 2020",
#         "1st place in Def Hacks Global 2.0, hosted by Major League Hacking internationally - 2020",
#         "Finalist for E-Yantra (EYRC) 2019-20",
#         "Manipal Hackathon Finalist (Special Mention Prize) - 2020",
#         "Finalists at Manipal Covid Challenge, 2020 (wearable tech)",
#         "2nd place in GME Ford Hackathon 2020",
#         "3rd place in IISF under the category 'Swastha Bharat'"
#       ],
#       "IGVC": {
#         "Description": "The Intelligent Ground Vehicle Competition (IGVC) is an annual international robotics competition for teams of undergraduate and graduate students. Teams design and build an autonomous ground vehicle capable of completing several difficult challenges.",
#         "Preparation": [
#           "Manufacturing and assembling the robot.",
#           "Implementing firmware and software solutions in electronics and SBC.",
#           "Investigating advanced multimodal architectures to improve data integration.",
#           "Developing robust vision models.",
#           "Enhancing NLP techniques.",
#           "Conducting research on model fusion techniques.",
#           "Exploring innovative transformer designs.",
#           "Implementing transfer learning and self-supervised learning.",
#           "Handling diverse modalities within unified frameworks."
#         ]
#       },
#       "WALRUS 2.0": {
#         "Features": [
#           "Solenoid trigger and gimbal mechanism for small arms.",
#           "Long-range secure communication systems.",
#           "Extreme weather operational capabilities.",
#           "Autonomous landing of mini-drone on moving UGV platform.",
#           "Real-time transmission of system parameters and video feed."
#         ]
#       },
#       "Technology": [
#         "Novel method of manufacturing PCB.",
#         "Deep Learning based Lane detection on grass surface.",
#         "Facial Verification algorithms using Deep Learning.",
#         "Novel architecture for Aerial Image segmentation and classification.",
#         "Lithium-ion battery packs design and assembly.",
#         "Usage of testing equipment like oscilloscope and logic analyzer.",
#         "Migrating from ROS1 to ROS2 Foxy Fitzroy version.",
#         "Implementation of encoders for feedback from motors."
#       ],
#       "Additional Initiatives": [
#         "Encouraging Indian MSMEs and OEMs by purchasing items.",
#         "Course on Udemy - 'Basic to advanced about the ESP32 controller'.",
#         "Sharing knowledge through tutorials and projects on the blog page - WattTheFarad.",
#         "Conducting seminars and guest lectures at MIT.",
#         "Prototype Webapp for simplifying reimbursement process.",
#         "Manufacturing PCB in-house.",
#         "Intranet portal for task management and accountability."
#       ],
#       "Sponsors": [
#         "Altium Designer - Top-tier PCB and electronic design automation software by Altium Limited."
#       ],
#       "Past Projects": [
#         "Drone - Maneuvering across air, planned for WALRUS Project.",
#         "GESSURE - Face authentication enabled dynamic gesture recognition GUI application.",
#         "RASPICO DEV - Multipurpose development board with RP2040 microcontroller.",
#         "BATTERY PACK - 16 cell configuration with BMS for cell balancing and protection."
#       ],
#       "Contact Information": {
#         "Website": "https://www.manipal.edu/mit/why/student-projects-manipal-university/rugved-systems.html",
#         "Instagram": "https://www.instagram.com/rugved_systems/"
#       }
#     }
# }

# # Function to generate response using Groq API
# def generate_response(user_input, company_info):
#     messages = [
#         {
#             "role": "system",
#             "content": f"You are an AI assistant for RUGVED SYSTEMS Inc. Answer questions only based on the provided company information: {json.dumps(company_info)}. If the question is not related to the provided information, respond with: 'I can't answer that question at this moment. Don't ever give replay based on information given'"
#         },
#         {"role": "user", "content": user_input}
#     ]

#     request_options = {
#         "method": "POST",
#         "headers": {
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {API_KEY}"
#         },
#         "body": json.dumps({
#             "model": "llama3-8b-8192",  # Replace with the correct Groq model ID
#             "messages": messages,
#             "temperature": 0.2,
#             "top_p": 0.7,
#             "stream": False,
#             "stop": None
#         })
#     }

#     response = requests.post(API_URL, headers=request_options["headers"], data=request_options["body"])
    
#     if response.status_code == 200:
#         data = response.json()
#         return data['choices'][0]['message']['content']
#     else:
#         return "Failed to fetch data from the Groq API"

# # Streamlit App Layout
# st.set_page_config(page_title="Chatbot", page_icon="chatbot.png")
# st.title("RUGVED SYSTEMS Inc Chatbot")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages
# for i, msg in enumerate(st.session_state.messages):
#     message(msg["message"], is_user=msg["is_user"], key=str(i))

# # User input
# user_input = st.text_input("Enter your message...", "")
# if st.button("send"):
#   if user_input:
#       # Display user's message
#       st.session_state.messages.append({"message": user_input, "is_user": True})

#       # Generate response from API
#       with st.spinner("Generating response..."):
#           response = generate_response(user_input, company_info)

#       # Display bot's response
#       st.session_state.messages.append({"message": response, "is_user": False})

#       # Clear the input field
#       st.rerun()
import streamlit as st
from streamlit_chat import message
import requests
import json

def clear_text():
    st.session_state.my_text = ""

# API configuration for Groq
API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = "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"  # Replace with your actual Groq API key

# Hardcoded company information from JSON file
company_info = {
    "role": "user",
    "content": {
      "Company Name": "RUGVED SYSTEMS INC",
      "Full Form": "Remote Unmanned Ground Vehicular Electronics Defence systems",
      "Description": "RUGVED SYSTEMS is a defence related student project from MIT Manipal. They work on different panels like surveillance, law enforcement, military assist, and civil defence. They participate in international competitions like IGVC, etc. They also had a contract with DRDO in building defence related projects.",
      "Subsytems": [
        {
          "Name": "AI and Robotics",
          "Activities": [
            "AI Nav - Anonymously traversing based on the input of sensor and data.",
            "Image Stitching - Enables better view of surroundings.",
            "Operationalizing Deep learning in real-world scenarios - Detect lanes, objects, track humans, face verification in real-time.",
            "Path Planning - Navigating the shortest route from current position to target position.",
            "Control - Feedback from IMU, Encoder, and GPS.",
            "Sensor Fusion - Combining various sensor data for precise data.",
            "Communication - Designing software pipelines for hardware interfacing."
          ],
          "Achievements": [
            "AI Gun - Sorting and tracking algorithms to detect and track humans for Border Security Force personnel.",
            "TRAFFICMUNDA - Traffic management app using reinforcement learning.",
            "Guiding Gaze - Top 7 in OpenCV AI International Competition 2023.",
            "IIT Bombay Eyantra - Ranked 10th in India.",
            "AI FOR CHANGE - Winners in the 'AI FOR CHANGE' hackathon."
          ]
        },
        {
          "Name": "Electronics",
          "Projects": [
            "6 DOF Robotic Arm - Driven by servos and controlled by Arduino.",
            "3-Wheeled omni-directional bot - Developed on STM32 Platform, Bluetooth controlled.",
            "Line Follower Robot - Developed for BITs Goa’s QUARK 2024.",
            "Quadcopter - Developed on PIXHAWK Platform.",
            "Line Follower/ Roboclench Bot/ Roborace Bot - Compete at BITS Goa Techfest.",
            "OMNI BOT V - Introduction to robotics and unconventional steering.",
            "DRONE - High-range UAV for aerial mapping."
          ]
        },
        {
          "Name": "RESEARCH",
          "Achievements": [
            "AI in Aerospace - GCAAMS-2024 accepted paper.",
            "Image Dehazing - Novel method using GANs and transformers.",
            "Optimization Algorithm - Research on optimization algorithms in AI.",
            "SpaceCraft Pose Estimation - Novel approach using YOLO, CNN, and multi-task training."
          ]
        },
        {
          "Name": "MECHANICAL",
          "Activities": [
            "Simulations and FEA - Simulating parts using finite element analysis.",
            "Vehicle dynamics - Designing based on vehicle dynamics.",
            "Structures and CAD - Designing power architecture, converters, battery packs.",
            "Materials and Manufacturing - Selection of materials and in-house manufacturing.",
            "ROBOTIC ARM - Precision engineering project.",
            "Omni bot V2 - Upgraded omni-directional bot.",
            "Mini Walrus - Unmanned vehicle with caterpillar track wheels.",
            "IGVC - Intelligent ground vehicle with advanced sensors and AI."
          ]
        },
        {
          "Name": "Management",
          "Activities": [
            "MERCH Designing",
            "RECRUITMENT PROCESS",
            "SOCIAL MEDIA",
            "WEBSITE maintenance",
            "Event calendar"
          ]
        }
      ],
      "Competitions": [
        "Line following Robot, BITS goa (Top 7)",
        "Guiding Gaze - Top 7 in OpenCV AI International Competition 2023",
        "IIT Bombay Eyantra (Currently Ranked 3rd in India)",
        "Finalist in SIH and Second runner-up in internal hackathon SIH 2023",
        "Finalist in MedTech Hackathon organized by MAHE-GOK bioincubator 2022",
        "Finalist in Manthan",
        "Finalist in CDAC Grand Challenge",
        "1st place in Pragyaan Fusion Hackathon, NIT-Trichy 2021",
        "1st place in 'Covideate', IIT Bombay's Techfest 2020",
        "1st place in Def Hacks Global 2.0, hosted by Major League Hacking internationally - 2020",
        "Finalist for E-Yantra (EYRC) 2019-20",
        "Manipal Hackathon Finalist (Special Mention Prize) - 2020",
        "Finalists at Manipal Covid Challenge, 2020 (wearable tech)",
        "2nd place in GME Ford Hackathon 2020",
        "3rd place in IISF under the category 'Swastha Bharat'"
      ],
      "IGVC": {
        "Description": "The Intelligent Ground Vehicle Competition (IGVC) is an annual international robotics competition for teams of undergraduate and graduate students. Teams design and build an autonomous ground vehicle capable of completing several difficult challenges.",
        "Preparation": [
          "Manufacturing and assembling the robot.",
          "Implementing firmware and software solutions in electronics and SBC.",
          "Investigating advanced multimodal architectures to improve data integration.",
          "Developing robust vision models.",
          "Enhancing NLP techniques.",
          "Conducting research on model fusion techniques.",
          "Exploring innovative transformer designs.",
          "Implementing transfer learning and self-supervised learning.",
          "Handling diverse modalities within unified frameworks."
        ]
      },
      "WALRUS 2.0": {
        "Features": [
          "Solenoid trigger and gimbal mechanism for small arms.",
          "Long-range secure communication systems.",
          "Extreme weather operational capabilities.",
          "Autonomous landing of mini-drone on moving UGV platform.",
          "Real-time transmission of system parameters and video feed."
        ]
      },
      "Technology": [
        "Novel method of manufacturing PCB.",
        "Deep Learning based Lane detection on grass surface.",
        "Facial Verification algorithms using Deep Learning.",
        "Novel architecture for Aerial Image segmentation and classification.",
        "Lithium-ion battery packs design and assembly.",
        "Usage of testing equipment like oscilloscope and logic analyzer.",
        "Migrating from ROS1 to ROS2 Foxy Fitzroy version.",
        "Implementation of encoders for feedback from motors."
      ],
      "Additional Initiatives": [
        "Encouraging Indian MSMEs and OEMs by purchasing items.",
        "Course on Udemy - 'Basic to advanced about the ESP32 controller'.",
        "Sharing knowledge through tutorials and projects on the blog page - WattTheFarad.",
        "Conducting seminars and guest lectures at MIT.",
        "Prototype Webapp for simplifying reimbursement process.",
        "Manufacturing PCB in-house.",
        "Intranet portal for task management and accountability."
      ],
      "Sponsors": [
        "Altium Designer - Top-tier PCB and electronic design automation software by Altium Limited."
      ],
      "Past Projects": [
        "Drone - Maneuvering across air, planned for WALRUS Project.",
        "GESSURE - Face authentication enabled dynamic gesture recognition GUI application.",
        "RASPICO DEV - Multipurpose development board with RP2040 microcontroller.",
        "BATTERY PACK - 16 cell configuration with BMS for cell balancing and protection."
      ],
      "Contact Information": {
        "Website": "https://www.manipal.edu/mit/why/student-projects-manipal-university/rugved-systems.html",
        "Instagram": "https://www.instagram.com/rugved_systems/"
      }
    }
}

# Function to generate response using Groq API
def generate_response(user_input, company_info):
    messages = [
        {
            "role": "system",
            "content": f"You are an AI assistant for RUGVED SYSTEMS Inc. Answer questions only based on the provided company information: {json.dumps(company_info)}. If the question is not related to the provided information, respond with: 'I can't answer that question at this moment'. Don't ever give replay based on information given"
        },
        {"role": "user", "content": user_input}
    ]

    request_options = {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        },
        "body": json.dumps({
            "model": "llama3-8b-8192",  # Replace with the correct Groq model ID
            "messages": messages,
            "temperature": 0.2,
            "top_p": 0.7,
            "stream": False,
            "stop": None
        })
    }

    response = requests.post(API_URL, headers=request_options["headers"], data=request_options["body"])
    
    if response.status_code == 200:
        data = response.json()
        return data['choices'][0]['message']['content']
    else:
        return "Failed to fetch data from the Groq API"

# Streamlit App Layout
st.set_page_config(page_title="Chatbot", page_icon="chatbot.png")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("chatbot.png", width=195)
with col2:
    st.title("RUGVED SYSTEMS Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for i, msg in enumerate(st.session_state.messages):
    message(msg["message"], is_user=msg["is_user"], key=str(i))

# User input with callback
def on_enter():
    user_input = st.session_state.user_input
    if user_input:
        # Display user's message
        st.session_state.messages.append({"message": user_input, "is_user": True})

        # Generate response from API
        with st.spinner("Generating response..."):
            response = generate_response(user_input, company_info)

        # Display bot's response
        st.session_state.messages.append({"message": response, "is_user": False})

        # Clear the input field
        st.session_state.user_input = ""
        # st.rerun()

user_input = st.text_input("Enter your message...", key="user_input", on_change=on_enter)

