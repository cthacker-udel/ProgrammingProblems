#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <time.h>
#include <algorithm>
#include <string>
#include <set>
#include <list>
using namespace std;

string ans_list[12]; // NEVER USE GLOBAL VARIABLES!!!
int ans_ct;          // SEE ABOVE

// void readandwriteFile(string fn);
void testingdoWordsMatch(string s1, string s2);
void testingfindGs(string s1, string s2, char chararr[], bool foundarr[]);
void testingfindYs(string s1, string s2, char chararr[], bool foundarr[]);
int getSize(string fn);
void readFile(string fn, string arr[], int num_words);
void playGame(int num_words, string arr[]);
string getWord(int num, string arr[]);
bool startGuessing(string curr_word);
void printResults();
bool checkWord(string guess, string curr_word);
bool doWordsMatch(string guess, string curr_word);
void findGs(string guess, string curr_word, char ans[], bool found[]);
void findYs(string guess, string curr_word, char ans[], bool found[]);
void reset_ans_list();

int main()
{

    /********************************************************************************
     * PART 1a:
     * 1) Write the function doWordsMatch.  The function takes as input 2 strings
     *    (both 5 letters long), and returns a boolean value indicating whether the
     *    two strings match.
     *    1a) Test with the first 4 function calls, below.
     *
     *    Output should be:
     *    		match and match are matches!! :-)
     * 			match and matcy do not match :-(
     *			match and gummy do not match :-(
     *			matcy and match do not match :-(
     * *******************************************************************************
     */
    testingdoWordsMatch("match", "match");
    testingdoWordsMatch("match", "matcy");
    testingdoWordsMatch("match", "gummy");
    testingdoWordsMatch("matcy", "match");

    /********************************************************************************
     * PART 1b:
     * 2) Write the function findGs.  The function takes as input 2 strings
     *    (both 5 letters long), an array of characters (5 characters long) and an
     *    array of boolean values (5 long).
     *    The function places a 'G' character in the character array everywhere that
     *    the two strings have identical characters in the identical indices.
     *    It also places a True (1) in the boolean array at that same index.
     *    In other words, if the two strings were, "match" and "harsh", the character
     *    arra would place a 'G' at index 1 and at index 4.  The boolean array would
     *    place a True (aka 1) at index 1 and index 4 also.
     *    2a)  Test with the 4 function calls, below
     *
     *    Output should be:
     *    	Part 1b
     *		**********************************
            m a t c h
            m a t c h
            G G G G G
            1 1 1 1 1
            **********************************
            m a t c h
            w a l s h
              G     G
            0 1 0 0 1
            **********************************
            m a t c h
            a m a z e

            0 0 0 0 0
            **********************************
            m a t c h
            m o o c h
            G     G G
            1 0 0 1 1
            **********************************
     * *******************************************************************************
    */

    cout << endl
         << endl
         << "Part 1b" << endl
         << "**********************************" << endl;
    char chararr[5] = {' ', ' ', ' ', ' ', ' '};
    bool foundarr[5] = {0, 0, 0, 0, 0};
    testingfindGs("match", "match", chararr, foundarr);
    testingfindGs("match", "walsh", chararr, foundarr);
    testingfindGs("match", "amaze", chararr, foundarr);
    testingfindGs("match", "mooch", chararr, foundarr);

    /********************************************************************************
     * PART 1c:
     * 3) Write the function findYs.  The function takes as input 2 strings
     *    (both 5 letters long), an array of characters (5 characters long) and an
     *    array of boolean values (5 long).
     *
     *    Bear with me.  This one is a bit detailed to describe.  It is looking for
     *    matching letters that ARE NOT in the right place between the two strings.
     *    If a letter in the first string occurs in the second string in an index
     *    other than the index where it occurs in the first string, you'll put a 1
     *    in the foundarr at the index where the letter occurs in the second string
     *    and a 'y' at the index where the letter occurs in the first string.
     *
     *    E.g., in "match"(string 1) and "llama" (string 2), the m and the a both
     *    occur in both words, but not in the same place.  Results would be
     *    {'Y','Y',' ',' ',' '} in the chararr (matching the indices for m and a in
     *    "match"),and {0 0 1 1 0} in the foundarr (matching the indices of a and m
     *    in "llama".
     *
     *    Some notes:  ONLY the first a in llama was mapped to 1 in the found array.
     *    This is because if we had 2 'a's in the first word, we'd want them to only
     *    match if there are 2 a's in 'llama'
     *    So, if we were matching "llama" and "match", the results would be:
     *    {' ',' ','Y','Y',' '} and {1 1 0 0 0}
     *
     *    What this means:  YOU ONLY WANT TO CHANGE A LETTER TO 'Y' IN THE CHARARR IF
     *    THERE IS NOT A CORRESPONDING 1 IN THE FOUNDARR.
     *
     *    In other words, if the FOUNDARR has a 1 in it, don't bother to check if that
     *    letter in the second string matches the letter in the first string.
     *    3a)  Test with the  5 function calls, below
     *
     *    Output should be:
     *
     *    	Part 1c
            **********************************
            m a t c h
            m a r s h
            G G     G
            1 1 0 0 1
            **********************************
            e n t e r
            r e s t s
            Y   Y   Y
            1 1 0 1 0
            **********************************
            r e s t s
            e n t e r
            Y Y   Y
            1 0 1 0 1
            **********************************
            e n t e r
            t e e t h
            Y   Y Y
            1 1 1 0 0
            **********************************
            m o m m y
            s i m o n
              Y G
            0 0 1 1 0
            **********************************
     * *******************************************************************************
    */

    cout << endl
         << endl
         << "Part 1c" << endl
         << "**********************************" << endl;
    char a1[] = {'G', 'G', ' ', ' ', 'G'};
    bool f1[] = {1, 1, 0, 0, 1};
    testingfindYs("match", "marsh", a1, f1);
    char a2[] = {' ', ' ', ' ', ' ', ' '};
    bool f2[] = {0, 0, 0, 0, 0};
    testingfindYs("enter", "rests", a2, f2);
    char a3[] = {' ', ' ', ' ', ' ', ' '};
    bool f3[] = {0, 0, 0, 0, 0};
    testingfindYs("rests", "enter", a3, f3);
    char a4[] = {' ', ' ', ' ', ' ', ' '};
    bool f4[] = {0, 0, 0, 0, 0};
    testingfindYs("enter", "teeth", a4, f4);

    char a5[] = {' ', ' ', 'G', ' ', ' '};
    bool f5[] = {0, 0, 1, 0, 0};
    testingfindYs("mommy", "simon", a5, f5);

    ///********************************************************************************
    // * PART 2:
    // * 1) comment out everything below the int main(){ line (on my program it's line 33)
    // *    down to the line above these comments (right above the above started line).
    // *    TO DO THAT EASILY:
    // *    a) highlight everything above this part 2 section up until (but below) the
    // *       line int main()
    // *    b) in Eclipse, go to Source (upper 3rd left tab)
    // *    c) Select Toggle Comment
    // *    d) (To undo that, just select again and Toggle Comment again)
    // *
    // * 2) uncomment out everything below this line to the return (0); line
    // * 3) compile and run the code
    // * 4) play wordle.
    // * *******************************************************************************
    //*/
    //	srand(time(NULL));  // for random numbers - you must include this, but don't worry about
    //	//it for now.
    //
    //	int num_words = getSize("wordlist.txt");
    //	string arr[num_words];
    //	readFile("wordlist.txt", arr, num_words);
    //
    ////	comment this in to test whether you are successfully reading in words from the worlist file.
    ////  If this isn't working:  make sure that "wordlist.txt" is in the same project
    ////	folder that contains wordle.cpp.
    ////	for (int i = 0; i < num_words; i++) {
    ////		cout << arr[i]<<endl;
    ////	}
    //
    //
    ////	This function is the function for the wordle game.  Other functions
    //// 	directly pertaining to the game itself will be called from inside
    ////	the PlayGame function.
    ////	Input: the number of words (an int), and the array of possible words (an array
    ////	of strings)
    //	playGame(num_words, arr);
    //
    return 0;
}

/*******************HERE IS WHERE THE CODE GOES! **********************************/
bool doWordsMatch(string guess, string curr_word)
{
    return guess == curr_word;
}

void findGs(string guess, string curr_word, char ans[], bool found[])
{
    for (int i = 0; i < guess.length(); i++)
    {
        if (guess[i] == curr_word[i])
        {
            ans[i] = 'G';
            found[i] = true;
        }
    }
}

void findYs(string guess, string curr_word, char ans[], bool found[])
{
    for (int i = 0; i < guess.length(); i++)
    {
        if (curr_word.find(guess[i]) != string::npos && curr_word[i] != guess[i])
        {
            for (int j = 0; j < curr_word.length(); j++)
            {
                if (curr_word[j] == guess[i] && !found[j])
                {
                    found[j] = true;
                    ans[i] = 'Y';
                    break;
                }
            }
        }
    }
}

/****************** END OF CODE YOU HAVE TO WRITE ********************************/

/***************************************************************************/

void testingdoWordsMatch(string s1, string s2)
{
    if (doWordsMatch(s1, s2))
    {
        cout << s1 << " and " << s2 << " are matches!! :-)" << endl;
    }
    else
    {
        cout << s1 << " and " << s2 << " do not match :-(  " << endl;
    }
}

void testingfindGs(string s1, string s2, char chararr[], bool foundarr[])
{
    findGs(s1, s2, chararr, foundarr);
    for (int i = 0; i < 5; i++)
    {
        cout << s1[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << s2[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << chararr[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << foundarr[i] << " ";
    }
    cout << endl;
    cout << "**********************************" << endl;
    for (int i = 0; i < 5; i++)
    {
        chararr[i] = ' ';
        foundarr[i] = 0;
    }
}

void testingfindYs(string s1, string s2, char chararr[], bool foundarr[])
{
    findYs(s1, s2, chararr, foundarr);
    for (int i = 0; i < 5; i++)
    {
        cout << s1[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << s2[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << chararr[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << foundarr[i] << " ";
    }
    cout << endl;
    cout << "**********************************" << endl;
    for (int i = 0; i < 5; i++)
    {
        chararr[i] = ' ';
        foundarr[i] = 0;
    }
}

void playGame(int num_words, string arr[])
{
    string keepPlaying = "Y";
    while ((keepPlaying == "Y") || (keepPlaying == "y"))
    {
        reset_ans_list();
        string curr_word = getWord(num_words, arr);
        // cout << curr_word<< endl;
        bool f = startGuessing(curr_word);
        if (f)
        {
            cout << "You won!!  You guessed: " << curr_word << endl;
            cout << endl;
        }
        else
        {
            cout << "Sorry, you did not win.  The word was: " << curr_word << endl;
            cout << endl;
        }
        cout << "Play Again (Y\\N)?  ";
        cin >> keepPlaying;
    }
    cout << "Thanks for playing! " << endl;
}

bool startGuessing(string curr_word)
{
    bool flag = false;
    int i = 0;
    while (i < 5 && !flag)
    {
        string s;
        cout << "Guess a 5-letter word:   ";
        cin >> s;
        flag = checkWord(s, curr_word);
        i++;
    }
    return flag;
}

bool checkWord(string guess, string curr_word)
{
    if (doWordsMatch(guess, curr_word))
    {
        return true;
    }
    else
    {
        char ans[5] = {' ', ' ', ' ', ' ', ' '};
        // ans is 5 characters long, initialized to blank characters.
        // if the guessed word has a character identical to the curr word and in
        // the same place as the curr word, in Wordle the character would turn
        // green.  In our sad, lame interface, we'll print out the ans array of
        // characters, and that character's space will get a 'G'
        // If the guess has a character that is in the curr_word, but it isn't in
        // the correct location, in Wordle, the character would turn yellow.  In
        // our lame pathetic interface the corresponding space will get a 'Y'.
        // Example:
        //
        // curr_word: adept
        // guess:     sleep
        // ans:         G Y
        // (the characters you can't see in ans are spaces.  Technically the array is really,
        // ' ',' ','G',' ','Y'
        bool found[5] = {0, 0, 0, 0, 0};
        // The reason for this array is a tad complicated to explain, so bear with me.
        // You want to mark each letter in the curr_word that corresponds to a letter
        // in the guessed word with a 1.  You don't want to re-match the same letter
        // more than once.
        // Example:
        // curr_word: prose
        // guess:     sleep
        // ans:       Y Y Y
        // found:     1 1 1
        // Notice how found doesn't make the second e in sleep be an out of place letter in the curr_word.
        // there's only one e in prose, so both e's in sleep should not get a yellow 'Y' character.  I used
        // the found to help me make sure I didn't match a duplicate more than once.

        findGs(guess, curr_word, ans, found);

        findYs(guess, curr_word, ans, found);

        ans_list[ans_ct * 2] = guess;
        ans_list[ans_ct * 2 + 1] = ans;

        ans_ct++;

        printResults();
    }
    return false;
}

void printResults()
{
    for (int j = 0; j < ans_ct * 2; j += 2)
    {
        for (int i = 0; i < 5; i++)
        {
            if (ans_list[j + 1][i] == ' ')
            {
                system("Color EF");
                cout << ans_list[j][i] << " ";
            }
            else if (ans_list[j + 1][i] == 'G')
            {
                system("Color AE");
                cout << ans_list[j][i] << " ";
            }
            else
            {
                system("Color AD");
                cout << ans_list[j][i] << " ";
            }
        }

        cout << endl;
        for (int i = 0; i < 5; i++)
        {
            cout << ans_list[j + 1][i] << " ";
        }
        cout << endl;
    }
}

string getWord(int num, string arr[])
{
    int x = rand() % num;
    string word;
    word = arr[x];
    return word;
}

void readFile(string fn, string arr[], int num_words)
{
    ifstream infile(fn.c_str(), ios::in);
    string size;
    infile >> size;
    for (int i = 0; i < num_words; i++)
    {
        infile >> arr[i];
    }
    infile.close();
}

int getSize(string fn)
{
    ifstream infile(fn.c_str(), ios::in);
    string size;
    infile >> size;
    int size_int = stoi(size);
    infile.close();
    return size_int;
}

void reset_ans_list()
{
    for (int i = 0; i < 12; i++)
    {
        ans_list[i] = "";
    }
    ans_ct = 0;
}
