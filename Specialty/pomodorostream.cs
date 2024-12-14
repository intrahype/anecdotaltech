using System;
{
    public bool Execute()
    {
        //Attempt to retrieve the raw input argument
        if (!args.TryGetValue("rawInput", out object rawInputObj) || rawInputObj == null)
        {
            CPH.LogWarn("No input provided. Use the format '!timer focus/break' (e.g. '!timer 25/5)').");
            return false;
        }
        string rawInput = rawInputObj.ToString().Trim();
        // validate rawInput 
        if (string.IsNullorWhiteSpace(rawInput))
        {
            CPH.LogWarn("No input provided. Use the format '!timer focus/break' (e.g. '!timer 25/5)').");
            return false;
        }
        //debug log to verify rawInput
        CPH.LogInfo($"Raw input recieved: {rawInput}");
        
        //split the input into focus and break times
        string[] timerParts = rawInput.Split('/');
            if (timerParts.Length != 2)
            {
                CPH.LogWarn("Invalid input format. Use the format '!timer focus/break' (e.g. '!timer 25/5)').");
                return false;
            }
            //parse focus and break times as integers
            
    }
}