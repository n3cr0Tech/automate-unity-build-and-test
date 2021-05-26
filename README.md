# Author: Jehoshua Josue
# Unity Dependencies
## Download and import the AltUnityTester from the Unity marketplace
## Make sure that your scene has the AltUnityRunnerPrefab, and all gameObjects has the AltUnityId component

# Things to do BEFORE running shell scripts
## Unity Side:
- Make sure that you're going to use the correct shell script based on your OS
- Make sure that the corresponding script and the method names in the shell script are correct
- Make sure that the C# script that will make the build in Unity has the proper parameters

## Python side:
- Create virtualenv with command: python -m venv NAME-YOUR-VIRTUALENV-HERE
- Install python dependencies with command: pip install -r requirements.txt
- Activate your virtualenv (for Windows) with command: source NAME-OF-VIRTUALENV/Scripts/activate 
- Activate your virtualenv (for MacOS) with command: source NAME-OF-VIRTUALENV/bin/activate
- chmod +x NAME-OF-SHELL-SCRIPT
- ./NAME-OF-SHELL-SCRIPT

# Troubleshooting
- If something goes wrong as you try to build your game, check the generated "build.log" file for some insight
- If the altunity dependency for python doesn's install properly, try to get the latest from PyPi and explicitly install it