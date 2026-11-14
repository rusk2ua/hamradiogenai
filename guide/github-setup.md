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

If you'd rather do it yourself, or want to see what Claude is doing for you, here is the whole process: setting up Git and GitHub, building in a local folder with your AI companion, and publishing from the terminal.

### Step 1: Create your online hub

1. Create a free account at [github.com](https://github.com).
2. Install the official **GitHub CLI**:
   - Mac (Homebrew): `brew install gh`
   - Windows or Linux: download from [cli.github.com](https://cli.github.com)
3. In a terminal (Terminal, PowerShell or Command Prompt), run:

   ```bash
   gh auth login
   ```

   Follow the prompts to sign in through your browser. No passwords typed into the terminal.

### Step 2: Protect your email address

Before your first commit, set Git to use your GitHub **noreply** address. Find it in GitHub **Settings → Emails**:

```bash
git config --global user.name "Your Name, CALL"
git config --global user.email "1234567+yourname@users.noreply.github.com"
```

While you're there, turn on **"Block command line pushes that expose my email."**

### Step 3: Start a project folder

```bash
mkdir ~/my-ham-radio-project
cd ~/my-ham-radio-project
git init -b main
```

Add a `.gitignore` so Git skips local clutter:

```text
.venv/
venv/
__pycache__/
*.pyc
.DS_Store
.env
```

### Step 4: Build with your AI, in that folder

1. Open the **Claude desktop app** and point it at `~/my-ham-radio-project`.
2. Attach your source material: the rules, a datasheet, a sample log.
3. Start up the [staircase](prompting.md) with step 1. For example:

   > Ask me clarifying questions before you write any code. I want a Python script named `log_parser.py` in this folder that reads my Cabrillo log `contest.log` and prints the number of contacts per band, so I can check my totals before I submit.

4. When something breaks, give it the evidence:

   > I ran the script and got this error: [paste]. Find the root cause and fix `log_parser.py` in place.

5. Ask for a README and a CHANGELOG as you go, not at the end.

### Step 5: Publish to GitHub

Start private; make it public when you're ready to share.

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

### Step 6 (optional): Free web hosting with GitHub Pages

If you built a web page or dashboard (like [nyqp-dashboard](https://github.com/rusk2ua/nyqp-dashboard)):

1. Put the web files (`index.html` and friends) in a `docs/` folder.
2. Add an empty `docs/.nojekyll` file so GitHub serves the files as they are:

   ```bash
   touch docs/.nojekyll
   git add docs/
   git commit -m "Add web page"
   git push
   ```

3. On GitHub: **Settings → Pages → Build and deployment**, source **Deploy from a branch**, branch **main**, folder **/docs**. Save.
4. A minute or so later it's live at `https://your-username.github.io/my-ham-radio-project/`.

On a free GitHub account, Pages needs a public repository, and the published site is public.

## Connecting Claude to GitHub

You can also connect Claude to your GitHub account so it can read and update your repositories directly. Ask Claude: "How do I connect you to my GitHub account?" and follow the current instructions for your plan. See also GitHub's [getting started docs](https://docs.github.com/en/get-started).
