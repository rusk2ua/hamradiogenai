# Getting started with GitHub

GitHub is a free place on the web where your project files live, with every version saved, and where you can share them when you're ready.

## The easy way: ask Claude

You don't need to learn GitHub's commands to use it. After a one-time setup, Claude can manage it for you.

1. **Make a free GitHub account** at [github.com](https://github.com), in your web browser.
2. **Connect it once, with guidance.** You can use the GitHub website or the command line, whichever you're comfortable with. Claude can walk you through either, one step at a time.
3. **Start one project with Claude.** Attach the rules or the datasheet, and [climb the staircase](prompting.md).
4. **Let Claude manage GitHub.** Saving versions, keeping your email address private, and sharing the project when you're ready. Just ask.

Don't know where to start? Ask Claude:

> Walk me through getting started with GitHub, step by step.

Two good habits to ask for on day one: start projects **private** and make them public only when you mean to share, and use your GitHub **noreply** email address so your personal one never appears in public.

## The manual way: every step yourself

If you'd rather do it yourself, or want to see what Claude is doing for you, here is the whole process: installing Git and the GitHub command-line tool, building in a local folder with your AI companion, and publishing. Open the section for your computer. Each one is complete on its own.

<details markdown="1">
<summary><b>Windows (PowerShell)</b></summary>

#### Step 1: Install the tools and sign in

1. Create a free account at [github.com](https://github.com).
2. Open **PowerShell**: click Start, type `PowerShell`, and open **Windows PowerShell** (or **Terminal**, which opens PowerShell). Use it rather than the old Command Prompt.
3. Install **Git** and the official **GitHub CLI** with Windows' built-in installer, `winget`:

    ```powershell
    winget install --id Git.Git -e --source winget
    winget install --id GitHub.cli -e --source winget
    ```

4. **Close PowerShell and open it again** so it finds the new commands. Then sign in:

    ```powershell
    gh auth login
    ```

    Follow the prompts to sign in through your browser. No passwords typed into PowerShell.

#### Step 2: Protect your email address

Before your first commit, set Git to use your GitHub **noreply** address. Find it in GitHub **Settings → Emails**:

```powershell
git config --global user.name "Your Name, CALL"
git config --global user.email "1234567+yourname@users.noreply.github.com"
```

While you're there, turn on **"Block command line pushes that expose my email."**

#### Step 3: Start a project folder

```powershell
mkdir $HOME\my-ham-radio-project
cd $HOME\my-ham-radio-project
git init -b main
notepad .gitignore
```

Notepad opens a new `.gitignore` file, which tells Git to skip local clutter. Paste this in, save, and close Notepad:

```text
.venv/
venv/
__pycache__/
*.pyc
Thumbs.db
.env
```

#### Step 4: Build with your AI, in that folder

1. Open the **Claude desktop app** and point it at your **my-ham-radio-project** folder (in your user folder, for example `C:\Users\yourname\my-ham-radio-project`).
2. Attach your source material: the rules, a datasheet, a sample log.
3. Start up the [staircase](prompting.md) with step 1. For example:

    > Ask me clarifying questions before you write any code. I want a Python script named `log_parser.py` in this folder that reads my Cabrillo log `contest.log` and prints the number of contacts per band, so I can check my totals before I submit.

4. When something breaks, give it the evidence:

    > I ran the script and got this error: [paste]. Find the root cause and fix `log_parser.py` in place.

5. Ask for a README and a CHANGELOG as you go, not at the end.

#### Step 5: Publish to GitHub

Start private; make it public when you're ready to share. In PowerShell, in your project folder:

```powershell
gh repo create my-ham-radio-project --private --source=. --remote=origin
git add .
git commit -m "First working log parser"
git push -u origin main
```

After that, each update is:

```powershell
git add .
git commit -m "Describe what changed and why"
git push
```

To share later: repository **Settings → General → Danger Zone → Change visibility**. To share privately, add collaborators under **Settings → Collaborators**.

#### Step 6 (optional): Free web hosting with GitHub Pages

If you built a web page or dashboard (like [nyqp-dashboard](https://github.com/rusk2ua/nyqp-dashboard)):

1. Put the web files (`index.html` and friends) in a `docs` folder in your project.
2. Add an empty `.nojekyll` file there so GitHub serves the files as they are, and publish:

    ```powershell
    New-Item docs\.nojekyll -ItemType File
    git add docs
    git commit -m "Add web page"
    git push
    ```

3. On GitHub: **Settings → Pages → Build and deployment**, source **Deploy from a branch**, branch **main**, folder **/docs**. Save.
4. A minute or so later it's live at `https://your-username.github.io/my-ham-radio-project/`.

On a free GitHub account, Pages needs a public repository, and the published site is public.

</details>

<details markdown="1">
<summary><b>Mac (Terminal)</b></summary>

#### Step 1: Install the tools and sign in

1. Create a free account at [github.com](https://github.com).
2. Open **Terminal**: press Cmd+Space, type `Terminal`, and press Return.
3. Install **Homebrew** if you don't have it yet, by following the one-line instructions at [brew.sh](https://brew.sh). Then install **Git** and the official **GitHub CLI**:

    ```bash
    brew install git gh
    ```

4. Sign in:

    ```bash
    gh auth login
    ```

    Follow the prompts to sign in through your browser. No passwords typed into Terminal.

#### Step 2: Protect your email address

Before your first commit, set Git to use your GitHub **noreply** address. Find it in GitHub **Settings → Emails**:

```bash
git config --global user.name "Your Name, CALL"
git config --global user.email "1234567+yourname@users.noreply.github.com"
```

While you're there, turn on **"Block command line pushes that expose my email."**

#### Step 3: Start a project folder

```bash
mkdir ~/my-ham-radio-project
cd ~/my-ham-radio-project
git init -b main
touch .gitignore
open -e .gitignore
```

TextEdit opens a new `.gitignore` file, which tells Git to skip local clutter. Paste this in, save, and close TextEdit:

```text
.venv/
venv/
__pycache__/
*.pyc
.DS_Store
.env
```

#### Step 4: Build with your AI, in that folder

1. Open the **Claude desktop app** and point it at your **my-ham-radio-project** folder (in your home folder).
2. Attach your source material: the rules, a datasheet, a sample log.
3. Start up the [staircase](prompting.md) with step 1. For example:

    > Ask me clarifying questions before you write any code. I want a Python script named `log_parser.py` in this folder that reads my Cabrillo log `contest.log` and prints the number of contacts per band, so I can check my totals before I submit.

4. When something breaks, give it the evidence:

    > I ran the script and got this error: [paste]. Find the root cause and fix `log_parser.py` in place.

5. Ask for a README and a CHANGELOG as you go, not at the end.

#### Step 5: Publish to GitHub

Start private; make it public when you're ready to share. In Terminal, in your project folder:

```bash
gh repo create my-ham-radio-project --private --source=. --remote=origin
git add .
git commit -m "First working log parser"
git push -u origin main
```

After that, each update is:

```bash
git add .
git commit -m "Describe what changed and why"
git push
```

To share later: repository **Settings → General → Danger Zone → Change visibility**. To share privately, add collaborators under **Settings → Collaborators**.

#### Step 6 (optional): Free web hosting with GitHub Pages

If you built a web page or dashboard (like [nyqp-dashboard](https://github.com/rusk2ua/nyqp-dashboard)):

1. Put the web files (`index.html` and friends) in a `docs` folder in your project.
2. Add an empty `.nojekyll` file there so GitHub serves the files as they are, and publish:

    ```bash
    touch docs/.nojekyll
    git add docs
    git commit -m "Add web page"
    git push
    ```

3. On GitHub: **Settings → Pages → Build and deployment**, source **Deploy from a branch**, branch **main**, folder **/docs**. Save.
4. A minute or so later it's live at `https://your-username.github.io/my-ham-radio-project/`.

On a free GitHub account, Pages needs a public repository, and the published site is public.

</details>

## Connecting Claude to GitHub

You can also connect Claude to your GitHub account so it can read and update your repositories directly. Ask Claude: "How do I connect you to my GitHub account?" and follow the current instructions for your plan. See also GitHub's [getting started docs](https://docs.github.com/en/get-started).
