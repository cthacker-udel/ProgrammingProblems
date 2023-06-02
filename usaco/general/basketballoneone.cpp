#include <vector>
#include <string>
#include <iostream>

int main(void) {
    std::string score;
    std::cin >> score;
    int aScore = 0;
    int bScore = 0;
    for (int i = 0; i < score.length(); i += 2) {
        aScore += score[i] == 'A' ? score[i + 1] - '0' : 0;
        bScore += score[i] == 'B' ? score[i + 1] - '0' : 0;
    }
    std::cout << (aScore > bScore ? "A" : "B") << std::endl;
}