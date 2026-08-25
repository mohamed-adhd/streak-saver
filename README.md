# streak-saver

A Vercel-hosted watchdog that keeps your GitHub contribution streak alive — checks if you've committed today, and if not, either commits for you or spams you with increasingly unhinged emails until you do. Paired with a small Avalonia desktop app for one-time setup.

![Python](https://img.shields.io/badge/Python-FastAPI-3776AB?style=flat-square&logo=python&logoColor=white)
![Vercel](https://img.shields.io/badge/Hosted%20on-Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![Redis](https://img.shields.io/badge/Upstash-Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Cron](https://img.shields.io/badge/Vercel-Cron-8F6BFF?style=flat-square)
![C#](https://img.shields.io/badge/C%23-Avalonia-5B4CFF?style=flat-square&logo=csharp&logoColor=white)
![MVVM](https://img.shields.io/badge/Pattern-MVVM-8F6BFF?style=flat-square)

## Overview
***DISCLAIMER : this project doesn't inflate commits , the app is allowed to only commit 1 time if i miss my day just to preserve my streak , it cannot inflate or fake commits*** 
streak-saver is a two-part project: a **FastAPI backend deployed on Vercel** that runs on a daily cron, checks whether you've made a commit that day, and auto-commits a small marker line to a file in your repo if you haven't — plus a **desktop setup app** built with C#, Avalonia, and MVVM that walks you through connecting your GitHub account so you never have to touch a config file by hand.

Your GitHub token is encrypted with Fernet before it's stored in Upstash Redis, so the backend never keeps it in plaintext. Alongside the auto-commit safety net, there's an email-alert system that fires off increasingly chaotic "get back to work" emails in the hours before the streak would break, in case you'd rather save it yourself.

## Demo / Screenshots

| Screen | Preview |
|---|---|
| Welcome | <img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/75905d3a-27ab-4192-b6b3-910adbffa224" />|
| Setup (connect repo) | <img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/1aa0c7cc-ebbe-4f69-9040-495291b8c967" />|
| Done |<img width="1279" height="719" alt="image" src="https://github.com/user-attachments/assets/139cea4e-628d-4033-b86d-81dc56986438" />|


## Core Workflow

```
Desktop app: enter username + repo + file path + PAT
      |
      v
POST /setup -> token encrypted (Fernet) -> config saved to Upstash Redis
      |
      v
Vercel Cron fires daily -> GET /api/cron
      |
      v
Check GitHub for a commit today (PyGithub search)
      |
      +-- already committed --> do nothing
      |
      +-- no commit yet --> append marker line to your file + push commit
      |
      v
/check1, /check2, /check3 (optional, called later in the day)
      |
      v
Still no commit? -> fire off an alert email via Gmail SMTP
```

## What streak-saver Does

| Area | Details |
|---|---|
| Setup flow | Desktop app collects GitHub username, target repo, file path, and a personal access token, then posts it to the backend. |
| Token security | The PAT is encrypted with `cryptography.Fernet` before being written to Redis, and decrypted only in-memory when needed. |
| Config storage | Upstash Redis (serverless, REST-based) holds the single active config as JSON. |
| Streak check | Uses PyGithub to search commits by `author:<user> committer-date:<today>` to see if you've already committed. |
| Auto-commit fallback | If no commit is found, it fetches your target file, appends a timestamped marker line, and pushes an update commit. |
| Scheduling | A Vercel Cron job hits `/api/cron` once a day (see `vercel.json`) to run the check/commit flow automatically. |
| Nag emails | `/check1`–`/check3` endpoints re-check the streak later in the day and, if it's still at risk, send an HTML email via Gmail SMTP nudging you to commit yourself. |
| Desktop client | An Avalonia MVVM app with a Welcome → Setup → Done flow for configuring the backend without editing JSON by hand. |

## Architecture

| Layer | Files                                                                                      | Role                                                                              |
|---|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| API entrypoint | `api/index.py`                                                                             | Vercel serverless entrypoint, re-exports the FastAPI `app`.                       |
| App core | `app/main.py`                                                                              | Defines all FastAPI routes: `/setup`, `/status`, `/api/cron`, `/check1-3`.        |
| GitHub integration | `app/github/auth.py`, `client.py`, `commits.py`, `init.py`                                 | Authenticates with a PAT, checks for today's commits, and pushes the auto-commit. |
| Streak alerts | `app/streak/checker.py`                                                                    | Builds and sends the HTML nag emails over Gmail SMTP.                             |
| Config/storage | Upstash Redis (via `upstash-redis`)                                                        | Stores the encrypted, single active user config.                                  |
| Scheduling | cron-job.org                                                                               | Defines the daily crons triggers.         |
| Desktop shell | `ssaver/App.axaml.cs`, `ViewLocator.cs`, `Program.cs`                                      | Bootstraps the Avalonia app and resolves views from view models.                  |
| Desktop view models | `ViewModels/welcomeViewModel.cs`, `configsViewModel.cs`, `DoneViewModel.cs`, `MainWindowViewModel.cs` | Own navigation state and drive the setup flow.                                    |
| Desktop views | `Views/welcomeView.axaml`, `configsView.axaml`, `DoneView.axaml`                           | Dark, purple-accented Avalonia screens for each setup step.                       |
| Desktop networking | `Models/Api.cs`                                                                            | Posts the collected setup data to the `/setup` endpoint.                          |

## Tech Stack

| Tech | Usage |
|---|---|
| Python / FastAPI | Backend API and route handling |
| Vercel | Serverless hosting |
| Upstash Redis | Serverless config storage |
| cryptography (Fernet) | Encrypting the stored GitHub token |
| PyGithub | Checking commit history and pushing auto-commits |
| smtplib / Gmail SMTP | Sending nag/alert emails |
| C# / .NET 10 | Desktop setup app |
| Avalonia 12 | Cross-platform desktop UI |
| CommunityToolkit.Mvvm | Observable properties and relay commands |
|cron-job.org| Cron scheduling |
## Running Locally

**Backend**

```bash
pip install -r requirements.txt
```

Set the required environment variables:

```
UPSTASH_REDIS_REST_URL=...
UPSTASH_REDIS_REST_TOKEN=...
ENCRYPTION_KEY=...      # Fernet key
smtp=...                # Gmail app password
```

Then run the FastAPI app (e.g. with `uvicorn app.main:app --reload`), or deploy it straight to Vercel , needs cron-job schedualing thou.

**Desktop app**

```bash
cd ssaver
dotnet restore
dotnet run
```

## Why I Built This
github streak is not something i can break , like literally i get sick if i dont commit and push at least 7 times a day, but better be safe than sorry , so this is here just in case the 
electricity cuts or something unexpected happens , 9/10 times i wont even need it 


## Developer Notes
- this is a personal project , i dont intend on making it a production level app , but if someone managed to set it up for themselves, then cheers .
- i didnt use vercel cron due to the hooby plan allowing me to hit an endpoint only once a day and its not even precise , so i used cron-job.org 
- hours poured : 35 as far as i counted
- further improvement include customizing the vercel home endpoint , etc , but so far i attained my goal , learned github automation and vercel deployment (which will help in the next repo(Oscuola))


Built with FastAPI, Vercel Cron, Upstash Redis, Avalonia, and redbulls at 2 am
