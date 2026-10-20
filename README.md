# Preet Sports Remote Windows PC

This repository installs and tests a Python automation project on your own Windows PC. It does not create a free hosted VM or expose RDP.

## Remote access
On your always-on Windows PC, visit https://remotedesktop.google.com/access and set up unattended remote access. Sign in with the same Google account from another device, select your PC, and enter the PIN. Enable account 2FA. Do not expose Windows RDP port 3389 to the internet.

## Setup
1. Install Chrome Remote Desktop on the host PC.
2. Open PowerShell and run `Set-ExecutionPolicy -Scope Process Bypass`, then `./setup.ps1`.
3. Close and reopen PowerShell so Git/Python/FFmpeg are on PATH.
4. Run `./install-project.ps1`.
5. Run `./.venv/Scripts/python.exe app.py`.
6. Confirm the MP3 exists in output/.

## GitHub synchronization
Create a GitHub repository, then from this directory:
```
git init
git add .
git commit -m "Initial Preet Sports setup"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```
On the host computer, clone your repository and run the setup scripts. To update: `git pull --ff-only`.

## Important
The PC must be powered on, awake, connected to the internet, and have enough free storage. Windows Home can host Chrome Remote Desktop even though it cannot host native Microsoft RDP. This starter app generates a test TTS MP3; replace app.py with your actual project. Never commit credentials, cookies, API keys, or remote access PINs.
