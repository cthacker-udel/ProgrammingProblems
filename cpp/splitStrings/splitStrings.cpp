#include <vector>
#include <string>

/**
 * @brief Splits a string into two character snippets, if one of the two-character pairs is one character short, we substitute that with an underscore
 *
 * @param s - The string we are splitting into pairs of two
 * @return std::vector<std::string> The pairs
 */
std::vector<std::string> splitStrings(const std::string &s)
{

    const std::vector<string> pairs;
    const std::string currentPair;
    for (int i = 0; i < s.length(); i++)
    {
        if (currentPair.length() == 2)
        {
            pairs.push_back(currentPair);
            currentPair = "";
        }
        currentPair += s.at(i);
    }
    if (currentPair.length() > 0)
    {
        switch (currentPair.length())
        {
        case 2:
            pairs.push_back(currentPair);
            break;
        case 1:
            const std::string newPair = currentPair + "_";
            pairs.push_back(newPair);
            break;
        default:
            break;
        }
    }
    return pairs;
}