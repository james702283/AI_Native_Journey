# Pursuit AI Cohort: The "Hello World" Journey

![Project Banner](https://images.unsplash.com/photo-1534972195531-d756b9bfa9f2?q=80&w=2070&auto=format&fit=crop)

Welcome to the "Hello World" Journey repository! This project documents the evolution of a simple Python greeting script into a dynamic, interactive web application and a polished, multi-slide presentation. It serves as a practical case study in software development, showcasing iterative enhancement, the application of conditional logic, and the transformation from a back-end script to a user-facing front-end experience.

---

## 🚀 Live Demos

This project has two live deployments on Netlify:

* **[View the Interactive Presentation](https://hello-world-script-demo.netlify.app/)**
* **[View the Standalone Message Generator App](https://ai-cohort-message-generator.netlify.app/)**

---

## ✨ Key Features

The final web application is an interactive slideshow that demos the project itself. Its key features include:

* **Interactive Slideshow:** A multi-slide presentation built with HTML, CSS, and JavaScript.
* **Thematic Design:** Each slide features a unique, high-quality background image related to its topic, with a sleek, dark aesthetic for a modern feel.
* **Live Applet:** An interactive "Welcome Message Generator" is embedded directly into the presentation, allowing users to test the core logic in real-time.
* **Conditional Logic:** The generator uses smart conditional logic to provide different messages based on user input (e.g., a special greeting for "James Nelson") and the current time of day.
* **Responsive Design:** The presentation is fully responsive and looks great on devices of all sizes.

---

## 밟 Project Evolution

This project was built iteratively, with each step adding a new layer of functionality and polish.

1.  **The Foundation (`welcome_script.py`):** The project began as a basic Python script. Its sole purpose was to generate and print a simple, hardcoded welcome message to the console.

2.  **Adding Intelligence:** The Python script was enhanced with conditional logic. An `if/else` statement was added to check for a specific name ("James Nelson") and provide a unique greeting. Further logic was added using the `datetime` library to make the greetings time-sensitive (e.g., "Good morning").

3.  **The Leap to the Web (`generator.html`):** The core logic was translated from Python to JavaScript and built into a standalone web page. This transformed the command-line tool into an interactive application.

4.  **Professional UI/UX Design:** The focus shifted to the user experience. The generator page was styled using Tailwind CSS, incorporating the official Pursuit branding (logo and fonts) and a professional background image to create a polished, visually appealing tool.

5.  **The Final Product (`presentation.html`):** The project culminated in the creation of an interactive, multi-slide presentation to showcase the journey. The generator app itself was embedded within the presentation, creating a "demo within a demo" and providing a comprehensive overview of the project's evolution.

---

## 💻 Technologies Used

* **Python:** For the initial script and core logic concept.
* **HTML5:** For the structure of the web pages.
* **CSS3 (Tailwind CSS):** For all styling, layout, and responsive design.
* **JavaScript:** For the interactive logic, including the message generator, slide navigation, and DOM manipulation.
* **Google Fonts:** For professional typography (`Poppins` and `Inter`).
* **Netlify:** For deployment and hosting of the final web application.

---

## ⚙️ How to Run Locally

To run this project on your local machine, simply download or clone the repository and open the `presentation.html` file in your preferred web browser.

```bash
# Clone the repository
git clone [https://github.com/james702283/AI_Native_Journey.git](https://github.com/james702283/AI_Native_Journey.git)

# Navigate to the project directory
cd AI_Native_Journey

# Open the main presentation file in your browser
# (On macOS, you can use the 'open' command)
open presentation.html
```

---

## 🙏 Acknowledgements

This project was developed as part of the Pursuit AI Cohort learning journey. The entire process, from ideation and coding to design and deployment, was a collaborative effort with **Google's Gemini**, which served as a creative and technical partner.
