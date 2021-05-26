echo Starting Build Process
'/Applications/Unity/Hub/Editor/2020.3.0f1/Unity.app/Contents/MacOS/Unity' -batchmode -projectPath ../automated-test-unity -executeMethod AutomateBuild.CreateBuild -logFile build.log -nographics -quit

echo Opening Build
open ../automated-test-unity/Builds/sampleBuild.app

pytest ./game_page_test.py