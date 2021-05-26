echo Starting Build Process
'C:/Program Files/Unity/Hub/2020.3.4f1/Editor/Unity.exe' -batchmode -projectPath ../automated-test-unity -executeMethod AutomateBuild.CreateBuild -logFile build.log -nographics -quit

echo Opening Build
start ../automated-test-unity/Builds/sampleBuild.exe
sleep 10

echo about to call pytest
pytest game_page_test.py
echo past pytest line