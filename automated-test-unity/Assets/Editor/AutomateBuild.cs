using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;

public class AutomateBuild
{
    public static void CreateBuild()
    {
        string[] scenesToBuild = { "Assets/Scenes/SampleScene.unity" };
        // string buildPath = "./Builds/sampleBuild.exe";
        string buildPath = "./Builds/sampleBuild.app"; //for MacOS
        // var buildTarget = UnityEditor.BuildTarget.StandaloneWindows64;
        var buildTarget = UnityEditor.BuildTarget.StandaloneOSX; //for MacOS
        var buildOptions = UnityEditor.BuildOptions.Development;
        var errorMsg = UnityEditor.BuildPipeline.BuildPlayer(scenesToBuild, buildPath, buildTarget, buildOptions);
    }
    
}
