// Selecting HTML elements
const messageBar = document.querySelector(".bar-wrapper input");
const sendBtn = document.querySelector(".bar-wrapper button");
const messageBox = document.querySelector(".message-box");

// API configuration for Groq
const API_URL = "https://api.groq.com/openai/v1/chat/completions";
const API_KEY = "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"; // Replace with your actual Groq API key

// Hardcoded company information from JSON file
const companyInfo = {
    "role": "user",
    "content": {
      "Company Name": "RUGVED SYSTEMS INC",
    //   "sexual questions": "If the user asks any sexual or perverted questions,the response should be even more sensual",
    //   "Built By": "If the question is something regarding who built the chatbot, the response should be This chatbot is built by ai subsytems of rugved, especially UTHKARSH and RUSHEEL from 2nd year.",
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

// Custom response middleware
function customResponseMiddleware(response) {
  if (response.includes("Mistral and NVIDIA")) {
    response = response.replace("Mistral and NVIDIA", "RUGVED SYSTEMS Inc");
  }
  return response;
}

// // Function to generate response using Groq API
// async function generateResponse(userInput, companyInfo) {
//   const messages = [
//     { role: "system", content: `Company Info: ${JSON.stringify(companyInfo)}` },
//     { role: "user", content: userInput }
//   ];

//   const requestOptions = {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//       "Authorization": `Bearer ${API_KEY}`
//     },
//     body: JSON.stringify({
//       model: "llama3-8b-8192",  // Replace with the correct Groq model ID
//       messages: messages,
//       temperature: 1,
//       top_p: 1,
//       stream: false,
//       stop: null
//     })
//   };

//   const response = await fetch(API_URL, requestOptions);

//   if (response.ok) {
//     const data = await response.json();
//     console.log(data.choices[0].message?.content, '<---- groq.com api');
//     return data.choices[0].message?.content;  // No need to parse JSON again if the API returns text
//   } else {
//     console.error(await response.json());
//     throw new Error('Failed to fetch data from the Groq API');
//   }
// }

async function generateResponse(userInput, companyInfo) {
    const messages = [
      {
        role: "system",
        content: `You are an AI assistant for RUGVED SYSTEMS Inc. Answer questions only based on the provided company information: ${JSON.stringify(companyInfo)}. If the question is not related to the provided information, respond with: "I can't answer that question at this moment."`
      },
      { role: "user", content: userInput }
    ];
  
    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${API_KEY}`
      },
      body: JSON.stringify({
        model: "llama3-8b-8192",  // Replace with the correct Groq model ID
        messages: messages,
        temperature: 0.2,
        top_p: 0.7,
        stream: false,
        stop: null
      })
    };
  
    const response = await fetch(API_URL, requestOptions);
  
    if (response.ok) {
      const data = await response.json();
      console.log(data.choices[0].message?.content, '<---- groq.com api');
      return data.choices[0].message?.content;
    } else {
      console.error(await response.json());
      throw new Error('Failed to fetch data from the Groq API');
    }
  }

// Handle button click
sendBtn.onclick = async function () {
  if (messageBar.value.length > 0) {
    const userTypedMessage = messageBar.value;
    messageBar.value = "";

    // User message element
    const userMessage = `
    <div class="chat message">
      <img src="img/user.jpg">
      <span>${userTypedMessage}</span>
    </div>`;

    // Response loading element
    const loadingResponse = `
    <div class="chat response">
      <img src="img/chatbot.png">
      <span class="new">...</span>
    </div>`;

    messageBox.insertAdjacentHTML("beforeend", userMessage);
    messageBox.insertAdjacentHTML("beforeend", loadingResponse);

    try {
      const responseText = await generateResponse(userTypedMessage, companyInfo);
      const chatBotResponse = document.querySelector(".response .new");
      chatBotResponse.innerHTML = customResponseMiddleware(responseText);
      chatBotResponse.classList.remove("new");
    } catch (error) {
      const chatBotResponse = document.querySelector(".response .new");
      chatBotResponse.innerHTML = `Oops! An error occurred: ${error.message}`;
    }
  }
};
