using System;
using System.Collections.Generic;

MORSE_CODE_LOOKUP = new Dictionary<string, string> {
    { ".-", "A" },
    { "-...", "B" },
    { "-.-.", "C" },
    { "-..", "D" },
    { ".", "E"},
    { "..-.", "F"},
    { "--.", "G" },
    { "....", "H"},
    { "..", "I" },
    { ".---", "J" },
    { "-.-", "K" },
    { ".-..", "L" },
    { "--", "M" },
    { "-.", "N" },
    { "---", "O" },
    { ".--.", "P" },
    { "--.-", "Q" },
    { ".-.", "R" },
    { "...", "S" },
    { "-", "T" },
    { "..-", "U" },
    { "...-", "V" },
    { ".--", "W" },
    { "-..-", "X" },
    { "-.--", "Y" },
    { "--..", "Z" }
};

public class MorseCodeDecoder
{

    public static string DecodeBits(string bits)
    {
        return ".";
    }

    public static string DecodeMorse(string morseCode)
    {
        return MorseCode.Get(morseCode);
    }
}