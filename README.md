# Amateur Radio AI Project Companion Guide
## A Living Document for Building and Sharing Ham Radio Projects with Generative AI
**By Rus Healy, K2UA**  
*Based on the Project Development for Amateur Radio Session*

---

## 1. The Grounded Ham Builder Philosophy

Amateur radio is fundamentally a maker's hobby. For a century, hams have built antennas, soldered circuits, and wired up stations. Yet, when it came to software, many operators felt locked behind a wall of syntax, complex compiler tooling, and steep learning curves. 

Generative AI has democratized software development, turning code into another "building material" that hams can shape. However, most people approach AI as a generalist chat tool, yielding what is known as **"AI Slop"** [3]—bloated, buggy, or outright hallucinated code that fails even superficial inspection.

To build reliable software, we must adopt the **Grounded AI** model [3]:
*   **Curate Before You Code:** Never let the AI guess the rules or formulas. Always feed the AI primary source documents—rules, mathematical schemas, and log files [107].
*   **Context Isolation:** Keep your workspace focused on a single project at a time so the AI's attention window remains clean and responsive [114].
*   **Syntax is Generative, Logic is Human:** Use the AI to generate code structure and handle syntax, but retain control over the system design, error boundaries, and operational constraints [153].

---

## 2. The Toolbelt: Curation, Collaborative Workspaces, and Code Editors

To build our software, we use a curated toolbelt. Below is a detailed comparison of the major options on your workbench:

| Capability / Feature | Google Gemini (Canvas) | Claude (Co-work) | ChatGPT (Codex) | Kiro (Spec Mode) |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Strength** | Collaborative, word processor-style canvas for side-by-side editing [8]. | Highly nuanced logical reasoning, desktop folder sync, expressive writing [6, 11]. | Strong general knowledge chat, but lacks code isolation structure [3, 12]. | Advanced, plan-first structured IDE for multi-file systems [153, 154]. |
| **Interface Style** | Flexible sidebar Canvas [8]. | Split-screen artifacts (read-only) [7]. | Inline canvas (less flexible) [7, 8]. | Integrated development editor (VS Code fork) [154]. |
| **Agent Capabilities** | Spark (cloud-based) [13]. | Co-work (reads and edits local files natively) [11, 12]. | Codex (desktop folder file editing) [12]. | Autonomous file modifications, console tools [153]. |
| **Curation Integration** | Built-in Google Notebooks (NotebookLM) for source-grounded research [15, 16]. | Connectors (Notion, Drive) and customized Project contexts [9, 41]. | Standard custom GPT files and memory profile settings [37, 123]. | Local steering files (`product.md`, `tech.md`) [165]. |
| **Recommendation** | **Highly Recommended** for collaborative planning, brainstorming, and single-file creation [8]. | **Highly Recommended** for multi-file script construction, documentation, and local folder management [11]. | **Not Recommended** due to lack of plan-first coding modes, cluttered Codex app, and inflexible Canvas [12]. | **Advanced Track** for hams with stronger development backgrounds wanting to build large-scale applications [154]. |

### The Codex Critique
Although OpenAI's **Codex** desktop application is capable, it is not recommended for this workflow [12]. Codex lacks native, plan-first structured coding modes [12, 153], lacks grounded research workspaces equivalent to Google NotebookLM [15], and its desktop app has no mechanism to distinguish between standard conversational chats, folder co-work tasks, and coding sessions [12]. This leads to cluttered sessions where code context easily degrades, resulting in buggy outcomes [12].

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
*   **Design Pattern:** **Zero-Dependency Responsive Design**. Built using pure static HTML5, CSS variables, and vanilla JS [100]. Charts are rendered dynamically via CDN-hosted **Chart.js** [100]. No node modules, no frameworks, no build steps required [100, 101]. Highly performant and accessible [98].
*   **Repository URL:** `https://github.com/rusk2ua/nyqp-dashboard` [95]

### Case Study 2: Maidenhead Grid Square Map Generator (`grid-mapper`)
*   **Description:** Reads contest log files and draws color-coded Maidenhead grid square boundaries on a geographic map [79].
*   **Design Pattern:** **Geographic Density Visualization**. Uses **matplotlib** and **cartopy** to draw actual 2° × 1° field grid square boundaries [79, 84]. Automatically detects active continents based on log files and scales map bounds [79]. Color intensity highlights contact density [79].
*   **Repository URL:** `https://github.com/rusk2ua/grid-mapper` [76]

### Case Study 3: Microwave Log Directional Analyst (`10ghz-log-analyzer`)
*   **Description:** A Python-based log evaluator for the ARRL 10 GHz and Up Contest [58].
*   **Design Pattern:** **Microwave Directional Visualization**. Calculates exact distance (km) and compass bearings between grid squares [58]. Generates beautiful **Polar Radar Plots** mapping total points by compass bearings (16 directions) and frequency bands [63]. Essential for evaluating microwave path obstacles [64].
*   **Repository URL:** `https://github.com/rusk2ua/10ghz-log-analyzer` [55]

### Case Study 4: Cabrillo Log Normalizer (`nyqp-cabrillo-fixer`)
*   **Description:** Extracts QSO columns from irregular contest PDF files and formats them into rules-compliant Cabrillo 3.0 files [90].
*   **Design Pattern:** **Irregular Data Extraction**. Uses **PyPDF2** to scan and extract tabular PDF data [90]. Chronologically orders contacts, normalizes date strings to the `YYYY-MM-DD` standard, and formats space-delimited text lines [91, 92, 93].
*   **Repository URL:** `https://github.com/rusk2ua/nyqp-cabrillo-fixer` [87]

### Case Study 5: Moonbounce Antenna Siting & Attenuation Calculator (`eme-calculator-project`)
*   **Description:** Guides operators on the optimal residential placement of large Earth-Moon-Earth (EME) dishes [69].
*   **Design Pattern:** **Cloud-Native Serverless Computing**. Uses **PyEphem** to calculate annual moon trajectories, computes wind loading force (lbf) on parabolic dishes, and models tree attenuation (dB) across microwave bands [69, 71, 75]. Backend runs as an **AWS Lambda function** with a clean REST API [70, 72].
*   **Repository URL:** `https://github.com/rusk2ua/eme-calculator-project` [66]

---

## 5. The Step-by-Step GitHub Setup Guide (No-Copilot CLI Workflow)

This step-by-step leave-behind walks you through setting up Git, writing code natively inside your local workspace using your AI companion, and pushing updates securely from the terminal. 

### Why We SKIP Microsoft Copilot
Microsoft Copilot acts as a transactional, inline autocomplete engine. It is designed for experienced programmers who want to speed up repetitive syntax typing. For the grounded builder, **Copilot leads to fragmented, unvetted, and buggy "slop" code** because it does not encourage design-stage planning, lacks localized context curation, and locks you into specific commercial code editors. Instead, we use standalone AI workspaces (Gemini Canvas or Claude Co-work) where we can curate reference materials first and collaborate on design before writing a single file.

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
