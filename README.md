# Amateur Radio AI Project Companion Guide
## Building and Sharing Ham Radio Projects with Generative AI
**By Rus Healy, K2UA**  
*Based on the Project Development for Amateur Radio Session*

---

## 1. The Grounded Ham Builder Philosophy

Amateur radio is fundamentally a maker's hobby. For a century, hams have built antennas, soldered circuits, and wired up stations. Yet, when it came to software, many operators felt locked behind a wall of syntax, complex compiler tooling, and steep learning curves. 

Generative AI has democratized software development, turning code into another "building material" that hams can shape. However, most people approach AI as a generalist chat tool, yielding what is known as **"AI Slop"** —bloated, buggy, or outright hallucinated code that fails even superficial inspection.

To build reliable software, we must adopt the **Grounded AI** model:
*   **Curate Before You Code:** Never let the AI guess the rules or formulas. Always feed the AI primary source documents—rules, mathematical schemas, and log files.
*   **Context Isolation:** Keep your workspace focused on a single project at a time so the AI's attention window remains clean and responsive.
*   **Syntax is Generative, Logic is Human:** Use the AI to generate code structure and handle syntax, but retain control over the system design, error boundaries, and operational constraints.

---

## 2. Curation, Collaborative Workspaces, and Code Editors

To build our software, we use a curated toolbelt. Below is a detailed comparison of the major options on your workbench:

| Capability / Feature | Google Gemini (Canvas) | Claude (Cowork) | ChatGPT (Codex) | Kiro (Spec Mode) |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Strength** | Collaborative, word processor-style canvas for side-by-side editing. | Highly nuanced logical reasoning, desktop folder sync, expressive writing. | Strong general knowledge chat, but lacks code isolation structure. | Advanced, plan-first structured IDE for multi-file systems. |
| **Interface Style** | Flexible sidebar Canvas. | Split-screen artifacts (read-only). | Inline canvas (less flexible). | Integrated development editor (VS Code fork). |
| **Agent Capabilities** | Spark (cloud-based). | Claude Cowork (reads and edits local files natively). | Codex (desktop folder file editing). | Autonomous file modifications, console tools. |
| **Curation Integration** | Built-in Google Notebooks (Gemini Notebook) for source-grounded research. | Connectors (Notion, Drive) and customized Project contexts. | Standard custom GPT files and memory profile settings. | Local steering files (`product.md`, `tech.md`). |
| **Recommendation** | **Highly Recommended** for collaborative planning, brainstorming, and single-file creation. | **Highly Recommended** for multi-file script construction, documentation, and local folder management. | **Not Recommended** due to poor consistently poor results. |

---

## 3. The Art of Technical Prompting: Progressive Staircase

To get clean, operational code on your first try, write structured, progressive prompts. Never ask the AI to build your entire application in a single prompt. Instead, utilize the **Progressive Prompting Staircase**:

```
Step 5: Refine, Polish, & Document (Add emojis, optimize UI, write README)
  ▲
Step 4: Layer on Visuals/UI (Matplotlib, Cartopy, HTML/CSS layout)
  ▲
Step 3: Core Logic & Calculations (Parse files, compute bearing/distance)
  ▲
Step 2: Basic File I/O (Read local Cabrillo logs, print row count)
  ▲
Step 1: Set the Spec & Choose the Architecture (Draft requirements.md)
```

### The Anatomy of a Strong Technical Prompt
When prompting your workspace engine (Gemini Canvas or Claude Cowork, etc), structure your instruction using this blueprint:

1.  **Role:** Tell the AI who it is. *"Act as an expert Python developer who values clean, readable, single-file scripts with minimal external dependencies."*
2.  **Context:** Detail what you are building. *"We are building a Maidenhead grid square map generator from a Cabrillo file."*
3.  **Constraints:** Set clear limits. *"Use Python. For libraries, use ONLY matplotlib and cartopy. Do not use an external database or containerization. Keep it beginner-friendly."* <--If you don't know anything about the libraries you want it to use, leave these out and let the AI engine determine these for you.
4.  **Input Data Schema:** Provide example inputs. *"The script will ingest a CSV file with columns: `callsign`, `freq`, `grid`, `date`."*
5.  **Output Format:** Specify the target deliverable. *"Write a single, executable Python script named `maidenhead_map.py` that processes the CSV and saves a high-resolution PNG map."*

---

## 4. Case Studies: Five Real Ham Radio Projects

Each of these functional, open-source projects demonstrates a distinct design pattern that you can copy, modify, and use to ground your own AI development.

### Case Study 1: Interactive Results Dashboard (`nyqp-dashboard`)
*   **Description:** A modern, interactive web-based dashboard presenting official contest results.
*   **Design Pattern:** **Zero-Dependency Responsive Design**. Built using pure static HTML5, CSS variables, and vanilla JS. Charts are rendered dynamically via CDN-hosted **Chart.js**. No node modules, no frameworks, no build steps required. Highly performant and accessible.
*   **Repository URL:** `https://github.com/rusk2ua/nyqp-dashboard`

### Case Study 2: Maidenhead Grid Square Map Generator (`grid-mapper`)
*   **Description:** Reads contest log files and draws color-coded Maidenhead grid square boundaries on a geographic map.
*   **Design Pattern:** **Geographic Density Visualization**. Uses **matplotlib** and **cartopy** to draw actual 2° × 1° field grid square boundaries. Automatically detects active continents based on log files and scales map bounds. Color intensity highlights contact density.
*   **Repository URL:** `https://github.com/rusk2ua/grid-mapper`

### Case Study 3: Microwave Log Directional Analyst (`10ghz-log-analyzer`)
*   **Description:** A Python-based log evaluator for the ARRL 10 GHz and Up Contest.
*   **Design Pattern:** **Microwave Directional Visualization**. Calculates exact distance (km) and compass bearings between grid squares. Generates beautiful **Polar Radar Plots** mapping total points by compass bearings (16 directions) and frequency bands. Essential for evaluating microwave path obstacles.
*   **Repository URL:** `https://github.com/rusk2ua/10ghz-log-analyzer`

### Case Study 4: Cabrillo Log Normalizer (`nyqp-cabrillo-fixer`)
*   **Description:** Extracts QSO columns from irregular contest PDF files and formats them into rules-compliant Cabrillo 3.0 files.
*   **Design Pattern:** **Irregular Data Extraction**. Uses **PyPDF2** to scan and extract tabular PDF data. Chronologically orders contacts, normalizes date strings to the `YYYY-MM-DD` standard, and formats space-delimited text lines.
*   **Repository URL:** `https://github.com/rusk2ua/nyqp-cabrillo-fixer` 

### Case Study 5: Moonbounce Antenna Siting & Attenuation Calculator (`eme-calculator-project`)
*   **Description:** Guides operators on the optimal residential placement of large Earth-Moon-Earth (EME) dishes.
*   **Design Pattern:** **Cloud-Native Serverless Computing**. Uses **PyEphem** to calculate annual moon trajectories, computes wind loading force (lbf) on parabolic dishes, and models tree attenuation (dB) across microwave bands. Backend runs as an **AWS Lambda function** with a clean REST API.
*   **Repository URL:** `https://github.com/rusk2ua/eme-calculator-project`

---

## 5. The Step-by-Step GitHub Setup Guide (No-Copilot CLI Workflow)

This step-by-step leave-behind walks you through setting up Git, writing code natively inside your local workspace using your AI companion, and pushing updates securely from the terminal. 

### Why We skip Microsoft Copilot

We skip Copilot because we prefer standalone workspace tools for design-first collaboration.

---

### Step 1: Create Your Online Hub
1.  Go to `https://github.com` and create a free account.
2.  Install the official **GitHub CLI (Command Line Interface)** on your computer:
    *   *Mac (via Homebrew):* `brew install gh`
    *   *Windows/Linux:* Download the installer from `https://cli.github.com`
3.  Open your computer’s terminal (Command Prompt, PowerShell, or Terminal) and run:
    ```bash
    gh auth login
    ```
4.  Follow the prompts to log in securely using your web browser. This configures safe, modern credential authentication (no need to type passwords in the terminal).

### Step 2: Initialize Your Local Project Workspace
1.  Create a folder on your computer for your project:
    ```bash
    mkdir ~/my-ham-radio-project
    cd ~/my-ham-radio-project
    ```
2.  Turn this folder into a local Git repository:
    ```bash
    git init -b main
    ```
3.  Create a basic homepage file named `README.md` in markdown format:
    ```markdown
    # My Ham Radio Project
    This is an AI-assisted project designed to solve station logging issues.
    ```
4.  Create a `.gitignore` file to tell Git to ignore temporary computer files (like `.DS_Store` or virtual environments):
    ```text
    venv/
    *.pyc
    .DS_Store
    ```

### Step 3: Run AI-Driven Local Construction (Claude Desktop App)
1.  Launch the **Claude Desktop Application** (which includes Claude Co-work) or open Gemini Canvas [8, 11].
2.  Start a new task in Claude Co-work and select **Choose Folder**. Select your local project directory: `~/my-ham-radio-project` [50].
3.  Write your first progressive prompt. For example:
    > *"I want to create a Python file named `log_parser.py` inside our folder. It should read a Cabrillo-formatted log file named `contest.log` and output the total number of contacts. Please write the Python script directly to my folder."*
4.  Claude will natively write the `log_parser.py` file to your folder. If you encounter errors when testing, type:
    > *"I ran the script but got this error in the terminal: [paste error]. Please modify `log_parser.py` in place to fix this."*

### Step 4: Link and Push Code to GitHub Natively from the CLI
Once your code works locally and you have verified its functionality, push it to GitHub using the terminal:

1.  Create a new, empty repository on GitHub using the CLI:
    ```bash
    gh repo create my-ham-radio-project --public --source=. --remote=origin
    ```
2.  Prepare your files to be saved:
    ```bash
    git add .
    ```
3.  Commit your progress (save a checkpoint locally) with a descriptive message:
    ```bash
    git commit -m "Initial commit of AI-constructed log parser"
    ```
4.  Push your files securely to your online GitHub repository:
    ```bash
    git push -u origin main
    ```
    *(Note: For subsequent updates, simply run `git add .`, `git commit -m "update message"`, and `git push` to keep your repo in sync).*

### Step 5: Activate Free Global Web Hosting
If you built a frontend dashboard (like `nyqp-dashboard`), you can host it live on the web for free [98, 102].

1.  Structure your project so all web files (`index.html`, `style.css`, etc.) reside in a subfolder named `/docs` [103].
2.  Create an empty file named `.nojekyll` inside the `/docs` folder [103]. This tells GitHub Pages to serve your raw HTML without processing it through static generators [102]:
    ```bash
    touch docs/.nojekyll
    ```
3.  Push these files to GitHub:
    ```bash
    git add docs/
    git commit -m "Add docs folder for web deployment"
    git push
    ```
4.  Go to your repository on `github.com` $\rightarrow$ **Settings** $\rightarrow$ **Pages** [102].
5.  Under "Build and deployment", set the source to **Deploy from a branch**. Set the branch to **main** and the folder to **/docs** [102].
6.  Click **Save** [102]. Your dashboard will be live globally at `https://your-username.github.io/my-ham-radio-project/` in under 60 seconds [102]!

---

## 6. Presenter Objection-Handling & Q&A Cheat Sheet

When presenting this material, you may encounter skeptics. Use these grounded talking points to address their concerns:

*   **Skeptic:** *"AI is just generating 'AI slop'—it can't write real, reliable radio software."*
    *   **Response:** "You are 100% correct about generic AI. If you ask a chatbot with no context to write code, you get buggy slop. But by curating our technical specifications (Rules PDFs, schema layouts) and utilizing a **Grounded AI** approach in tools like NotebookLM, we force the AI to write highly precise code that complies exactly with specifications. The difference is context curation."
*   **Skeptic:** *"Using AI is cheating. Real hams write their own code."*
    *   **Response:** "Hams didn't stop building transceivers when we moved from vacuum tubes to microchips—we adapted. AI is simply a smarter calculator. It handles the tedious syntax and typing so you can focus on system design, radio operations, and solving station bottlenecks. It turns ideas into reality faster."
*   **Skeptic:** *"Is this workflow expensive? Do I need to spend hundreds on AI models?"*
    *   **Response:** "No! The free tiers of Claude and Gemini are incredibly capable. You only need to upgrade to paid plans ($20/month) as you scale your projects to multi-file cloud-deployed applications or heavily exceed hourly session usage."
*   **Skeptic:** *"I don't want to upload my logs to the public cloud. What about privacy?"*
    *   **Response:** "By utilizing **Model Context Protocol (MCP)** and local file folder agents like Claude Co-work, your private contest log files never need to leave your computer. The AI reads and queries the data locally on your physical drive, keeping your station records completely secure."
