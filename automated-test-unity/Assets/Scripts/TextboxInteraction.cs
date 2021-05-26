using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TextboxInteraction : MonoBehaviour
{
    public void OnButtonClick()
	{
        GetComponent<Text>().text = "Hello there";
	}
}
